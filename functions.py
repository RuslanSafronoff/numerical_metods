import numpy as np


def f_(x):
    if x > 0.5:
        return x ** 2 + np.log(x)
    else:
        return x ** 2


def g(x):
    return 100 * np.sin(x)


def h(x):
    if x < 0.5:
        return x ** 4 - 5 * x ** 3
    else:
        return 2 * np.log(x)


def l(x):
    return x * (x - 1) * (x - 0.7) + 0.01 * np.sin(70 * x)


def S(t):
    return 3 * t + np.sin(t)


def z(t):
    return 4 * t + np.cos(t)


def rho(omega):
    return 6 * omega * (1 - omega)


def f(z, x, S, beta):
    return beta * (x - z)

