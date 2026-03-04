import pandas as pd

dati = {
    "nome": ["Ciccio", "anna", " Marcello", "Francesca", "PAOLO"],
    "email":["ciccio@email.it", " anna@email.com", "marcello@redyard.com ", "francesca@email.com", "paolo@paolo.it"],
    "eta": [25,22,38, 20,21],
    "stipendio": [1200,1800, 1900, 2100, 1750],
    "citta": ["Roma", "Milano", "Firenze", "Roma", "Roma"],
    "categoria": ["A","A","B", "A", "B"],
    "vendite": [240,250,190,310,370]
}

df = pd.DataFrame(dati)

#pulizia nome
df["nome"] = df["nome"].str.strip().str.title()
df["email"] = df["email"].str.strip().str.lower()

#pulizia email
df = df.dropna(subset = ["email"])
df = df[df["email"].str.contains("@")]

#pulizia eta e popolamento con la media
df["eta"] = pd.to_numeric(df["eta"], errors="coerce")
df  =df.dropna(subset=["eta"])
df["eta"] = df["eta"].fillna(df["eta"].mean())
df["eta"] = df["eta"].astype(int)

#popolamento stipendio con la media
df["stipendio"] = df["stipendio"].fillna(df["stipendio"].mean())


#raggruppare vendite per citta
print(df.groupby("categoria")["vendite"].agg(["sum", "count", "mean"]))


#print(df)
