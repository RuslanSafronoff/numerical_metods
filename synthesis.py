import numpy as np
import matplotlib.pyplot as plt
import spline
import integration
import differentiation
import functions
import time

CONST = 100
T = 1
x0, y0 = 0, 0
beta = -0.01


def get_poly_value(polys, t, x):
    N = t.shape[0]
    index = 0
    while index < N and t[index] < x:
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
    N = t.shape[0]
    index = 0
    while index < N and t[index] < x:
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


def S(t):
    return 3 * t + np.sin(t)


def z(t):
    return 4 * t + np.cos(t)


def rho(omega):
    return 6 * omega * (1 - omega)


def f(z, x, S, beta):
    return beta * (x - S)


def odu(rho=rho, S=S, z=z, T=T, x0=x0, y0=y0, beta=beta):
    # gpv = np.vectorize(get_poly_value, otypes=[np.float32])
    # gppv = np.vectorize(get_poly_point_value, otypes=[np.float32])
    # S_v = np.vectorize(S, otypes=[np.float32])
    t_ = np.linspace(0, T, CONST)
    z_poly = spline.cubic_spline_coefs(np.vstack((t_, z(t_))))
    rho_poly = integration.integrate_plus_spline(rho, t_)

    def f_(t, x, y):
        return get_poly_value(rho_poly, t_, y) * get_poly_point_value(z_poly, t_, t)

    def g_(t, x, y):
        return f(z(t), x, S(t), beta)

    solution = differentiation.differentiate(f_, g_, 0, T, CONST, x0, y0)
    x_poly = spline.cubic_spline_coefs(np.vstack((t_, solution[1])))

    def rho_integrate(t):
        return get_poly_value(rho_poly, t_, t)

    def x_point(t):
        return get_poly_point_value(x_poly, t_, t)

    def smth(t):
        return x_point(t) * rho_integrate(t)

    def C1():
        return 1 - integration.integrate_simpson_func(smth, 0, T) / (solution[1][-1] - solution[1][0])

    def C2():
        return (solution[1][-1] - S(T)) / S(T)
    # plt.plot(t_, solution[1])
    # plt.show()
    return solution, C1(), C2()


def optimizer(ax, A=1, B=10, N=3, S=S):
    S_v = np.vectorize(S, otypes=[np.float32])
    beta = np.linspace(0, 1, N)
    functionals = np.zeros(N)
    odus = [0] * N
    for i in range(N):
        odus[i] = odu(beta=beta[i])
        C1 = odus[i][1]
        C2 = odus[i][2]
        # sol, C1, C2 = odu(beta=beta[i])
        # ax.plot(S_v(sol[0]), sol[1], label='$/beta = ${}'.format(i))
        functionals[i] = A * C1 + B * C2
    beta_best = beta[np.argmin(functionals)]
    for i in range(N):
        if odus[i] != beta_best:
            ax.plot(odus[i][0][1], S_v(odus[i][0][0]), label='$beta = $' + '%f' % beta[i])
        else:
            ax.plot(odus[i][0][1], S_v(odus[i][0][0]), label='$beta = $' + '%f' % beta[i], color='r')
    ax.legend()
    return beta


# print(integration.integrate_trapezoidal_func(functions.g, 0, np.pi / 2))

# t1 = time.clock()
# print(odu(rho, S, z, 1, 0, 0, 0.01))
# t2 = time.clock()
# print(t2-t1)

#  pyuic5 untitled.ui -o design.py
# a = np.array([1, 2, 3])
# a_ = np.expand_dims(a, axis=1)
# print(a_)
# b = np.array([1, 1])
# b_ = np.expand_dims(b, axis=0)
# print(b_)
# print(np.dot(a_, b_).sum(axis=1))
