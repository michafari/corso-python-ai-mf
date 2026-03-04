import numpy as np

studenti = np.array([
    [80,79,90],
    [60,75,90],
    [88,93,90],
    [55,60,70]
])

media_per_studente = studenti.mean(axis=1)
print(media_per_studente)

media_per_materia = studenti.mean(axis=0)
print(media_per_materia)

media_alta = media_per_studente > 75
print(media_alta)

studenti_bravi = studenti[media_alta]
print(studenti_bravi)
