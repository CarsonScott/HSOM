from random import uniform, sample
import numpy as np

def logistic(x):  
    return np.exp(-np.logaddexp(0, -x))

def sign(x):
	return -1 if x < 0 else 1 if x > 0 else 0

def sort(X):
	Y=[]
	X=list(X)
	I=[i for i in range(len(X))]
	while len(X) > 0:
		index=X.index(min(X))
		Y.append(I[index])
		del X[index]
		del I[index]
	return Y

def reverse(X):
	return [X[i] for i in range(len(X)-1,-1,-1)]