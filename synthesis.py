import numpy as np
import matplotlib.pyplot as plt
import spline
import integration
import differentiation

CONST = 5000


def offset(x, x0):
    return x - x0


def get_poly_value(polys, t, x):
    index = 0
    while t[index] < x:
        index = index + 1
    if index == 0:
        coefs = polys[0]
    else:
        coefs = polys[index - 1]
    x0 = coefs[-1]
    a = coefs[0]
    b = coefs[1]
    c = coefs[2]
    d = coefs[3]
    return a + b * (x - x0) + c * (x - x0) ** 2 + d * (x - x0) ** 3
    # return np.dot(np.expand_dims(offset(x, x0), axis=1),
    #               np.expand_dims(coefs[:-1], axis=0)).sum(axis=1)


def get_poly_point_value(polys, t, x):
    index = 0
    while t[index] < x:
        index = index + 1
    if index == 0:
        coefs = polys[0]
    else:
        coefs = polys[index - 1]
    x0 = coefs[-1]
    a = coefs[0]
    b = coefs[1]
    c = coefs[2]
    d = coefs[3]
    return b + 2 * c * (x - x0) + 3 * d * (x - x0) ** 2
    # return np.dot(np.expand_dims(offset(x, x0), axis=1),
    #               np.expand_dims(coefs[1:-1] * mask, axis=0)).sum(axis=1)


def z_point_spline(z, T, N = CONST): return


def S(t):
    return 3 * t + np.sin(t)


def z(t):
    return 4 * t + np.cos(t)


def rho(omega):
    return 6 * omega * (1 - omega)


def f(z, x, S, beta):
    return beta * (x - z)


def odu(rho, S, z, T, x0, y0, beta):
    # gpv = np.vectorize(get_poly_value, otypes=[np.float32])
    # gppv = np.vectorize(get_poly_point_value, otypes=[np.float32])
    t_ = np.linspace(0, T, CONST)
    z_poly = spline.cubic_spline_coefs(np.vstack((t_, z(t_))))
    rho_poly = integration.integrate_plus_spline(rho, t_)

    def f_(t, x, y):
        return get_poly_value(rho_poly, t_, y) * get_poly_point_value(z_poly, t_, t)

    def g_(t, x, y):
        return f(z(t), x, S(t), beta)

    solution = differentiation.differentiate(f_, g_, 0, T, CONST, x0, y0)
    plt.plot(t_, solution[-1])
    plt.show()
    return solution


print(odu(rho, S, z, 1, 0, 0, 0.01))


# a = np.array([1, 2, 3])
# a_ = np.expand_dims(a, axis=1)
# print(a_)
# b = np.array([1, 1])
# b_ = np.expand_dims(b, axis=0)
# print(b_)
# print(np.dot(a_, b_).sum(axis=1))
