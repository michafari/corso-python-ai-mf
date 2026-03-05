import re

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
dataset = pd.read_csv("NetFlix.csv")

dataset["director"] = dataset["director"].fillna("")
dataset["cast"] = dataset["cast"].fillna("")
dataset["genres"] = dataset["genres"].fillna("")
dataset["description"] = dataset["description"].fillna("")
dataset["soup"] = dataset["director"]+" " +dataset["cast"]+ " " +dataset["genres"]+ " " + dataset["description"]
new_dataset = dataset[["title","soup"]]

def prepare_descr(item):
    item = item.astype(str)
    item = item.str.replace("-", "")
    item = item.str.replace(",", " ")
    item = item.str.replace(".", "" )
    return item

new_dataset["soup"] = prepare_descr(new_dataset["soup"])
print(new_dataset.head(50))

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(new_dataset["soup"])

print(tfidf_matrix.shape)
print(tfidf_matrix.nnz)

nn_model = NearestNeighbors(metric='cosine', algorithm='brute')
nn_model.fit(tfidf_matrix)

title = "Peaky Blinders"
row = new_dataset.iloc[new_dataset["title"] == title]
value = row["soup"].values[0]

input_vec = vectorizer.transform([value])
distances, indices = nn_model.kneighbors(input_vec, n_neighbors=30)

for i, idx in enumerate(indices[0]):
    print(f"{i+1}: {new_dataset.iloc[idx]['title']} (distance: {distances[0][i]:.3f})")
