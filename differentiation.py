import numpy as np


def differentiate(f, g, a, b, N, x0, y0):
    t = np.linspace(a, b, N)
    h = (b - a) / N
    X = np.zeros(N)
    Y = np.zeros(N)
    X[0] = x0
    Y[0] = y0
    for i in range(N-1):
        k1 = f(t[i], X[i], Y[i]) * h
        m1 = g(t[i], X[i], Y[i]) * h
        k2 = f(t[i] + h / 2, X[i] + k1 / 2, Y[i] + m1 / 2)
        m2 = g(t[i] + h / 2, X[i] + k1 / 2, Y[i] + m1 / 2)
        k3 = f(t[i] + h / 2, X[i] + k2 / 2, Y[i] + m2 / 2)
        m3 = g(t[i] + h / 2, X[i] + k2 / 2, Y[i] + m2 / 2)
        k4 = f(t[i] + h, X[i] + k3, Y[i] + m3)
        m4 = g(t[i] + h, X[i] + k3, Y[i] + m3)
        X[i + 1] = X[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        Y[i + 1] = Y[i] + (m1 + 2 * m2 + 2 * m3 + m4) / 6
    return np.vstack((t, X, Y))
