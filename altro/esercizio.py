#aggiungere una colonna categoria
#se eta >= 27 categoria "Senior", se no "Junior"

import csv
import json
''''
with open("dati.csv") as f:
    reader = csv.DictReader(f)
    dict_nomi = list(reader)

#print(dict_nomi)

for riga in dict_nomi:
    if int(riga["eta"]) >= 27:
        riga["categoria"] = "Senior"
    else:
        riga["categoria"] = "Junior"

#print(dict_nomi)

with open("nuovo file.csv", 'w', newline = '') as nf:
    #colonne = ["nome", "eta", "citta", "categoria"]
    colonne = dict_nomi[0].keys()
    writer = csv.DictWriter(nf, fieldnames = colonne)
    writer.writeheader()
    writer.writerows(dict_nomi)


a partire da questo csv, effettuare la sanificazione dei dati, aggiungere una colonna seniority (junior, mid, senior) ed esportare:

utenti_validi.csv
utenti_non_validi.csv
utenti.json (solo validi)
'''
with open("dati.csv") as f:
    reader = csv.DictReader(f)
    dict_nomi = list(reader)

utenti_validi = []
utenti_non_validi = []

for riga in dict_nomi:
    for value in riga.values():
        if value == None or value == "":
            utenti_non_validi.append(riga)
    try:

        if int(riga["eta"]) >= 29:
            riga["categoria"] = "Senior"

        elif int(riga["eta"]) >= 26:
            riga["categoria"] = "Mid Level"
        else:
            riga["categoria"] = "Junior"
    except ValueError:
        utenti_non_validi.append(riga)
        pass

print(utenti_non_validi)

for riga in dict_nomi:
    if riga not in utenti_non_validi:
        utenti_validi.append(riga)

print(utenti_validi)

with open("utenti_validi.csv", 'w', newline ='') as uv:
    colonne = utenti_validi[0].keys()
    writer = csv.DictWriter(uv, fieldnames=colonne)
    writer.writeheader()
    writer.writerows(utenti_validi)

with open("utenti_non_validi.csv", 'w', newline ='') as unv:
    colonne = utenti_validi[0].keys()
    writer = csv.DictWriter(unv, fieldnames=colonne)
    writer.writeheader()
    writer.writerows(utenti_non_validi)

with open("utenti_validi.json", 'w', newline ='') as uv:
    json.dump(utenti_validi, uv, indent=4)
