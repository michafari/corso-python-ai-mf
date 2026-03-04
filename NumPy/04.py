import numpy as np

dataset = np.random.uniform(0,10,(5,3))
#print(dataset)

dataset_originale = dataset.copy()

features_ds = dataset[:,1:]

minimo = np.min(features_ds, axis=0)
massimo = np.max(features_ds, axis=0)
features_norm = (features_ds - minimo)/(massimo - minimo)

dataset[:,1:] = features_norm
print(dataset)

media_feature = np.mean(dataset[:,1:], axis = 1)
media_feature= media_feature.reshape(-1,1)
print(media_feature)

dataset_con_media = np.hstack((dataset,media_feature))
print(dataset_con_media)


