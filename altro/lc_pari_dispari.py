numeri = [5,12,7,20,3,18]

'''
creare una lista che divida per due i numeri maggiori
di dieci, e lasci invariati gli altri
'''

numeri_tsf = [numero/2 if numero > 10 else numero for numero in numeri]
print(numeri_tsf)