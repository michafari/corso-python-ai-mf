numeri = [5,12,26,30,20,9,14,209]
#crea nuova lista solo con i numeri maggiori di 10
# e divisi per due

numeri_filtr = []

for numero in numeri:
    if numero > 10:
        numeri_filtr.append(numero)

numeri_tsf = []
for nom in numeri_filtr:
    nom_tsf = nom/2
    numeri_tsf.append(nom_tsf)



print(numeri_tsf)