def somma(a, b):
    return a + b

def sottrazione(a,b):
    return a - b

def moltiplicazione(a,b):
    return a * b

def divisione(a,b):
    try:
        risultato = a / b
        return risultato
    except ZeroDivisionError:
        return "non puoi dividere per 0!"
