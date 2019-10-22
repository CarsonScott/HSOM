from configparser import ConfigParser
from random import uniform
import numpy as np

def logistic(x):  
    return np.exp(-np.logaddexp(0, -x))

def sign(x):
	return -1 if x < 0 else 1 if x > 0 else 0