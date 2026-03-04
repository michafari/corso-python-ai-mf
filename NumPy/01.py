import numpy as np

array = np.random.randint(1,101,10)
media = np.mean(array)
massimi = np.max(array)
nuovo_array = array * 3
array_filt = array[array > 50]

print(array, media, massimi, nuovo_array, array_filt)