numeri = [5,12,26,30,20,9,14,209]
#crea nuova lista solo con i numeri maggiori di 10
# e divisi per due

numeri_tsf = []

for numero in numeri:
    if numero > 10:
        numeri_tsf.append(numero/2)

print(numeri_tsf)