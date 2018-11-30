import numpy as np


def f(x):
    return x ** 2


def g(x):
    return np.sin(x)


def h(x):
    if 0 < x < 5:
        return np.log(x)
    elif x <= 0:
        return x ** 2
    else:
        return np.exp(x)
