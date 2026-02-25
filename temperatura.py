temperature = [18,22,30,12,15,32,27,19,28,20]

#creare una nuova lista con le temperature superiori a 20

temperatureVentiPiu = []

for temp in temperature:
    if temp > 20:
        temperatureVentiPiu.append(temp)

print(temperatureVentiPiu)
