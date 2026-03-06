import pandas as pd

pd.set_option("display.width", 180)
pd.set_option('display.max_columns', None)
df = pd.read_csv("epl_final.csv")
#print(df.tail())

#filtro dati (prendi dati da stagione 20-21 e eslcudi partite in cui ci sono cartellini rossi
df_original = df.copy()
df = df[df["Season"].isin(["2020/21", "2021/22", "2022/23", "2023/24", "2024/25"])]
df = df[(df["HomeRedCards"] == 0) & (df["AwayRedCards"] == 0)]
df = df.drop(["HomeFouls", "AwayFouls", "HomeYellowCards", "AwayYellowCards", "HomeRedCards", "AwayRedCards"], axis=1)
#print(df.head())

#costruire nuova feature differenza tra gol casa e gol trasferta
df["g_diff"] = df["FullTimeHomeGoals"] - df["FullTimeAwayGoals"]
print(df.head())