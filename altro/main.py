#This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import utils


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#print(utils.divisione(2,0))


#IT26D0538777340000000554593


'''scrivere programma che riceve una lista di stringhe numeriche (numeri come stringa),
 li converte in interi gestendo gli errori, restituisce solo i maggiori di 10, calcola la somma'''



'''
def riceve_numeri_come_stringhe():
    lista_numeri = []
    while True:
        numeroComeStringa = input("Inserisci numero:")

        if numeroComeStringa == "00":
                break
        else: lista_numeri.append(numeroComeStringa)

    return lista_numeri


def converte_in_interi(lista):
    lista_interi =[]
    for num in lista:
        try:
            intero = int(num)
            if intero > 10:
                lista_interi.append(intero)
        except ValueError:
            pass

    return lista_interi

def somma_lista(lista):
    somma = sum(lista)
    return somma



#lista_numeri1 =riceve_numeri_come_stringhe()
#print(lista_numeri1)
#lista_interi1 = converte_in_interi(lista_numeri1)
#print(lista_interi1)
somma1 = somma_lista(converte_in_interi(riceve_numeri_come_stringhe()))
print(somma1)


'''






