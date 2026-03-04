# LIST COMPREHENSION

#trasf + filtraggio

#numeri pari moltiplicati per 10

numeri =[1,2,3,4,5,6,]

numeri_pari_x_10 = [numero * 10 for numero in numeri if numero % 2 == 0]

print(numeri_pari_x_10)