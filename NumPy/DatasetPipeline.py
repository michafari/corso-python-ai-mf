from __future__ import annotations
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple
import numpy as np

RAW_RECORDS: List[Dict[str, Any]] = [{"age": " 25", "income": "€30.000", "debts": "2",   "credit_score": "650", "approved": "yes"},
{"age": "45",  "income": "80000",   "debts": "1",   "credit_score": "720", "approved": "1"},
{"age": "N/A", "income": "€50.000", "debts": "5",   "credit_score": "580", "approved": "no"},
{"age": "23",  "income": " 25k ",   "debts": "3",   "credit_score": "600", "approved": "0"},
{"age": "52",  "income": "120000",  "debts": "0",   "credit_score": "800", "approved": "yes"},
{"age": "40",  "income": "70k",     "debts": "4",   "credit_score": "610", "approved": "no"},
{"age": "??",  "income": "40000",   "debts": "",    "credit_score": None,  "approved": "yes"},
{"age": "31",  "income": "€-1000",  "debts": "2",   "credit_score": "690", "approved": "no"},
{"age": "34 ", "income": "45000",   "debts": "two", "credit_score": "710", "approved": "yes"},
{"age": "29",  "income": " 60000 ", "debts": "1",   "credit_score": "680", "approved": "YES"}
                                     ]
#creo un modello dati
@dataclass
class CleanRecord:
    age: int
    income: float
    debts: int
    credit_score: int
    approved: int #in machine learning non ho true e false, ma 0 e 1

#Classe per parsing/sanificazione
class FieldParser:

    def parse_int(self, value: Any) -> Optional[int]:#questo metodo dovrebbe restituirmi un intero, altrimenti potrebbe restituirmi None
        if value is None:
            return None

        if isinstance(value, str):
            txt = value.strip()
            if txt == "" or txt.lower() in {"n/a", "na","??"}:
                return None

            txt = re.sub(r"[^\d\-]", "", txt) #rejects

            if txt == "" or txt =="-":
                return None

            try:
                return int(txt)
            except ValueError:
                return None

        if isinstance(value, (int, np.integer)):
            return int(value)

        return None

    def parse_income(self, value: Any) -> Optional[float]:
        if value is None:
            return None

        if isinstance(value, (int, float, np.integer, np.floating)):
            income = float(value)
            return income

        if not isinstance(value, str):
            return None

        txt = value.strip().lower()

        if txt == "" or txt in {"n/a", "na","??"}:
            return None

        k_match = re.fullmatch(r"([-+]?\d+)\s*k", txt)
        if k_match:
            return float(k_match.group(1))*1000.0 #group1 prende tutto prima della k (nella reject)

        txt = txt.replace("€", "").replace(" ","").replace(".","")

        try:
            return float(txt)
        except ValueError:
            return None


    def parse_approved(self, value: Any) -> Optional[int]:

        if not isinstance(value, str):
            return None

        txt = value.strip().lower()

        if txt in {"1","yes", "y", "si", "sì", "t", "true"}:
            return 1

        if txt in {"0","no", "n", "f", "false"}:
            return 0

        return None


#validatore
class RecordValidator:

    def is_valid(self, rec: CleanRecord) -> bool:

        if rec.age <18 or rec.age > 99:
            return False

        if rec.income <= 0:
            return False

        if rec.debts < 0:
            return False

        if rec.debts < 0 or rec.debts > 50:
            return False

        if rec.credit_score < 300 or rec.credit_score > 850:
            return False

        if rec.approved not in (0,1):
            return False

        return True


class PreprocessingPipeline:

    def __init__(self, parser: FieldParser,validator: RecordValidator):
        self.parser = parser
        self.validator = validator
        self.dropped_records: int = 0
        self.kept_records: int = 0

    def clean_records(self, raw_records: List[CleanRecord]) -> List[CleanRecord]:
        cleaned: List[CleanRecord] = []

        for row in raw_records:
            age = self.parser.parse_int(row.get("age")) #get protegge se age non esiste
            income = self.parser.parse_income(row.get("income"))
            debts = self.parser.parse_int(row.get("debts"))
            credit_score = self.parser.parse_int(row.get("credit_score"))
            approved = self.parser.parse_approved(row.get("approved"))

            if None in (age, income, debts, credit_score, approved):
                self.dropped_records +=1
                continue

            rec = CleanRecord(
                age = age,
                income = income,
                debts = debts,
                credit_score = credit_score,
                approved = approved
            )


            if not self.validator.is_valid(rec):
                self.dropped_records +=1
                continue

            cleaned.append(rec)
            self.kept_records +=1

        return cleaned

    def build_xy(self, cleaned: List[CleanRecord]) -> Tuple[np.ndarray, np.ndarray]:
        X = np.array(
            [[r.age, r.income, r.debts, r.credit_score] for r in cleaned],
        dtype = float
        )


        y = np.array(
            [r.approved for r in cleaned],
            dtype = int
        )

        return X, y

    def add_feature_engineering(self, X: np.ndarray) ->np.ndarray:
        income = X[:,1]
        debts = X[:,2]

        debt_to_income = debts/income

        debt_to_income = debt_to_income.reshape(-1, 1)

        X_enhanced = np.hstack((X, debt_to_income))
        return X_enhanced

    def minmax_normalize(self, X: np.ndarray) -> np.ndarray:

        min_col = np.min(X, axis = 0)
        max_col = np.max(X, axis = 0)

        denom = (max_col - min_col)

        denom[denom == 0] = 1.0

        X_norm = (X - min_col)/ denom
        return X_norm

    def train_test_split(self,
                         X: np.ndarray,
                         y: np.ndarray,
                         train_ratio: float = 0.8,
                         seed: int = 42
                         ) -> Tuple[np.ndarray, np.ndarray,np.ndarray,np.ndarray]:#se quando chiamo la funzione non passo train_ratio e seed prende quelli di default

        idx = np.arange(len(X))
        rng = np.random.default_rng(seed)
        rng.shuffle(idx)

        train_size = int(len(idx)*train_ratio)
        train_idx = idx[:train_size]
        test_idx = idx[train_size:]
        X_train = X[train_idx]
        X_test = X[test_idx]

        y_train = y[train_idx]
        y_test = y[test_idx]

        return X_train, X_test, y_train, y_test






