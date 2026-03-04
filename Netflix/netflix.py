import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
dataset = pd.read_csv("NetFlix.csv")


dataset["soup"] = dataset["director"]+" " +dataset["cast"]+" " +dataset["genres"]+ " " + dataset["description"]
new_dataset = dataset[["title","soup"]]
new_dataset["soup"] = new_dataset["soup"].str.split()
new_dataset["soup"] = new_dataset["soup"].astype(str).str.replace(" ", "")
#new_dataset = new_dataset.fillna("")
print(new_dataset.head(20))

tfidf = TfidfVectorizer()
new_dataset["matrix"] = tfidf.fit_transform(new_dataset["soup"])

new_dataset_final = np.hstack((new_dataset["title"], new_dataset["matrix"]))
# Modello NearestNeighbors standard
model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(new_dataset_final)

def recommend_netflix_series(title, df, model, k=10):

    seed = df[df["title"] == title]

    if seed.empty:
        raise ValueError("Title doesn't exist")

    seed_row = seed.iloc[0]
    seed_num = seed["soup"]
    seed_num_scaled = tfidf.transform(seed_num)

    distances, indices = model.kneighbors(seed_num_scaled, n_neighbors=k + 1)

    recs = df.iloc[indices[0]].copy()
    recs = recs[recs["title"] != title]

    recs = recs.head(k)
    recs['similarity_distance'] = distances[0][1:]

    return recs[["title", "similarity_distance"]]

##
print(recommend_netflix_series("Stranger Things", new_dataset, model_knn))