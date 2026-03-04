import numpy as np

np.random.seed(42)

#eta #reddito annuo #numero debiti #credit score #approvazione
dataset = np.array([
    [25,30000, 2, 650, 1],
    [45,80000,1,720,1],
    [35,50000,5,580,0],
    [23,25000,3,600,0],
    [52,120000,0,800,1],
    [40,70000,4,610,0]
])

X = dataset[:,:-1]
Y = dataset[:,-1]

minimo = np.min(X, axis = 0)
massimo = np.max(X, axis = 0)

X_norm = (X-minimo)/(massimo-minimo)
#print(X_norm)

reddito = X[:,1]
debito = X[:,2]
rapporto_debiti = debito/reddito

rapporto_debiti = rapporto_debiti.reshape(-1,1)
#print(rapporto_debiti)

X_enhanced = np.hstack((X_norm,rapporto_debiti))
#print(X_enhanced)

indices = np.arange(len(X_enhanced))
np.random.shuffle(indices)
#print(indices)

train_size = int(len(indices)*0.8)
train_idx = indices[:train_size]
test_idx = indices[train_size:]

X_train = X_enhanced[train_idx]
X_test = X_enhanced[test_idx]

y_train = Y[train_idx]
y_test = Y[test_idx]


print(X_train)
print(y_train)


