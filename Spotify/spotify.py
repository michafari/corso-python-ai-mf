import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

#pd.set_option('display.max_columns', 21)

#df  = pd.read_csv("spotify_dataset.csv")

#print(df.head())
#print("Righe totali: ", len(df))
#print("Tracce uniche:", df["track_id"].nunique())
missing = df.isna().sum()
#print(missing)
missing_values = df.isnull().sum()
#print(missing_values)

features_num = [
            "energy",
            "tempo",
            "valence",
            "acousticness"
            ]

#print(df[features_num].describe())

df = df.sort_values("popularity", ascending=False)
df = df.drop_duplicates(subset = ["track_id"], keep = "first")

genre_ohe = pd.get_dummies(df["track_genre"], prefix = "genre")

X_num = df[features_num]
#X = pd.concat([X_num, genre_ohe], axis = 1)
scaler = StandardScaler()
X_num_scaled = scaler.fit_transform(X_num)


X_final = np.hstack((X_num_scaled, genre_ohe.values))

model = NearestNeighbors(n_neighbors=10+1, metric='euclidean')
model.fit(X_final)

print(X_final.shape)

def reccomend_by_track_id(
        track_id: str,
        k: int = 10,
        same_genre: bool = False,
)->pd.DataFrame:

    seed = df[df["track_id"] == track_id]
    if seed.empty:
        raise ValueError("Track ID doesn't exist")

    seed_row = seed.iloc[0]
    seed_num = seed[features_num]
    seed_num_scaled = scaler.fit_transform(seed_num)

    seed_genre = seed_row["track_genre"]
    seed_genre_ohe = np.zeros((1, genre_ohe.shape[1]))

    genre_col_name = f"genre_{seed_genre}"

    if genre_col_name in genre_ohe.columns:
        idx = list(genre_ohe.columns).index(genre_col_name)
        seed_genre_ohe[0,idx] = 1

    seed_vec = np.hstack([seed_num_scaled, seed_genre_ohe])

    distances, indices = model.kneighbors(seed_vec)

    recs = df.iloc[indices[0]].copy()
    recs = recs[recs["track_id"] != track_id]

    if same_genre:
        recs = recs[recs["track_genre"] == seed_row["track_genre"]]

    recs = recs.head(k)

    cols = [
        "track_id",
        "track_name",
        "artists",
        "track_genre",
        "popularity",
    ]

    return recs[cols]

test_id = "3gVhsZtseYtY1fMuyYq06F"

print("Traccia seed: \n")
print(df[df["track_id"] == test_id][["track_name","artists"]])

print("Tracce consigliate: \n")
print(reccomend_by_track_id(test_id, k=10, same_genre=True))