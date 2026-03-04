prodotti = [
    {"id" : 1, "nome": "PC", "prezzo": 999.00},
    {"id" : 2, "nome": "Monitor", "prezzo": 699.00},
    {"id" : 3, "nome": "Mouse", "prezzo": 99.00},
    {"id" : 4, "nome": "Tastiera", "prezzo": 129.00}
]

'''

'''
numeri = [3,6,9,12,15,18,21,24,27,30]

#creare un dizionario con chiave numero e valore numero/3

nomi = ["Anna", "Ciccio", "Francesca", "Annibale"]

#creare dizionario con chiave nome e valore "Lungo" se lunghezza > 5 alrimenti "Corto"

num_dict = {n : n/3 for n in numeri}

nomi_dict = {nome : "Lungo" if len(nome) > 5 else "Corto" for nome in nomi}

print(num_dict)
print(nomi_dict)
