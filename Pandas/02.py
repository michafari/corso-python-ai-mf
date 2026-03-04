import pandas as pd

dati = {
    "settore": ["Tech", "Retail", "Finance", "Tech", "Tech", "Retail", "Finance"],
    "dipendenti": [50,70,30,90,80,75,20],
    "fatturato": [50000, 60000, 33000, 120000, 90000, 85000, 18000]
}

df = pd.DataFrame(dati)

#fatturato medio per settore
#numero totale di dipendenti per settore
#settore con massimo fatturato totale

print(df)

fatt = df.groupby("settore")["fatturato"].mean()
print(fatt)

n_dip = df.groupby("settore")["dipendenti"].sum()
print(n_dip)

totali = df.groupby("settore")["fatturato"].sum()
smax = totali.idxmax()
print(smax)
