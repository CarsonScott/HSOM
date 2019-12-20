import numpy as np


def logistic(x):
    return np.exp(-np.logaddexp(0, -x))


def sign(x):
    return -1 if x < 0 else 1 if x > 0 else 0


def ith_if_iterable(obj, i):
    if isinstance(obj, list) or isinstance(obj, tuple):
        return obj[i]
    else:
        return obj
