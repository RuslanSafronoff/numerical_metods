import numpy as np
import matplotlib.pyplot as plt
from math import ceil
import functions

def cubic_spline_coefs(grid):
    t = grid[0]
    f = grid[1]
    N = t.shape[0]
    tau = t[1:] - t[:-1]
    fau = f[1:] - f[:-1]
    A = tau[1:] / 6
    B = (tau[1:] + tau[:-1]) / 3
    C = np.copy(A)
    F = fau[1:] / tau[1:] - fau[:-1] / tau[:-1]
    alpha = np.full(N-2, np.float32(0.))
    beta = np.full(N-2, np.float32(0.))
    m = np.full(N, np.float32(0.))
    alpha[1] = - B[0] / C[0]
    beta[1] = F[0] / C[0]
    for i in range(2, N-2):
        alpha[i] = - B[i - 1] / (A[i - 1] * alpha[i - 1] + C[i - 1])
        beta[i] = (F[i - 1] - A[i - 1] * beta[i - 1]) / (A[i - 1] * alpha[i - 1] + C[i - 1])
    m[0], m[-1] = 0., 0.
    m[-2] = (F[-1] - A[-1] * beta[-1]) / (C[-1] + A[-1] * alpha[-1])
    for i in range(N-3):
        m[N - 3 - i] = alpha[N - 3 - i] * m[N - 3 - i] + beta[N - 3 - i]
    mau = m[1:] - m[:-1]
    P = fau / tau - (tau * mau) / 6
    Q = f[:-1] - m[:-1] * (tau ** 2) / 6 - P * t[:-1]
    tau2 = 2 * tau
    t3 = mau / (tau2 * 3)
    t2 = (t[1:] * m[:-1] - t[:-1] * m[1:]) / tau2
    t1 = ((t[:-1] ** 2) * m[1:] - (t[1:] ** 2) * m[:-1]) / tau2 + P
    t0 = ((t[1:] ** 3) * m[:-1] - (t[:-1] ** 3) * m[1:]) / (tau2 * 3) + Q
    cubic_splines = np.hstack((np.expand_dims(t3, axis=1),
                               np.expand_dims(t2, axis=1),
                               np.expand_dims(t1, axis=1),
                               np.expand_dims(t0, axis=1)))
    return cubic_splines


def cubic_spline_coefs_wiki(grid):
    t = grid[0]
    f = grid[1]
    N = t.shape[0]
    A = np.copy(f)
    B = np.full(N, np.float32(0.))
    C = np.full(N, np.float32(0.))
    D = np.full(N, np.float32(0.))
    # h =  np.ones(N)
    h = t[1:] - t[:-1]
    Ah = h[:-1]
    Ch = 2 * (h[:-1] + h[1:])
    Bh = h[1:]
    Fh = 3 * ((A[2:] - A[1:-1]) / h[1:] - (A[1:-1] - A[:-2]) / h[:-1])
    alpha = np.full(N - 2, np.float32(0.))
    beta = np.full(N - 2, np.float32(0.))
    alpha[1] = - Bh[0] / Ch[0]
    beta[1] = Fh[0] / Ch[0]
    for i in range(2, N - 2):
        alpha[i] = - Bh[i - 1] / (Ah[i - 1] * alpha[i - 1] + Ch[i - 1])
        beta[i] = (Fh[i - 1] - Ah[i - 1] * beta[i - 1]) / (Ah[i - 1] * alpha[i - 1] + Ch[i - 1])
    C[0], C[-1] = 0., 0.
    C[-2] = (Fh[-1] - Ah[-1] * beta[-1]) / (Ch[-1] + Ah[-1] * alpha[-1])
    for i in range(N - 3):
        C[N - 3 - i] = alpha[N - 3 - i] * C[N - 3 - i] + beta[N - 3 - i]
    B[1:] = (A[1:] - A[:-1]) / h + (2 * C[1:] + C[:-1]) * h / 3
    D[1:] = (C[1:] - C[:-1]) / h / 3
    cubic_splines = np.hstack((np.expand_dims(A[1:], axis=1),
                               np.expand_dims(B[1:], axis=1),
                               np.expand_dims(C[1:], axis=1),
                               np.expand_dims(D[1:], axis=1),
                               np.expand_dims(t[1:], axis=1)))
    return cubic_splines


def get_cubic_poly_value(t, coefs):
    T = np.vstack((t ** 3, t ** 2, t, np.ones(t.shape[0])))
    return np.dot(coefs, T)


def get_cubic_poly_value_wiki(t, coefs):
    T = np.vstack((np.ones(t.shape[0]), (t - coefs[-1]), (t - coefs[-1]) ** 2, (t - coefs[-1]) ** 3))
    return np.dot(coefs[:-1], T)


def cubic_spline_grid(grid, eps=np.float32(0.1)):
    t = grid[0]
    N = t.shape[0]
    grid_t_extended = np.array([])
    grid_f_spline = np.array([])
    cubic_splines = cubic_spline_coefs(grid)
    for i in range(N - 1):
        # print(N)
        x = np.linspace(t[i], t[i+1], int(ceil((t[i+1] - t[i]) / eps)))
        y = get_cubic_poly_value(x, cubic_splines[i])
        grid_t_extended = np.append(grid_t_extended, x)
        # print(grid_t_extended)
        grid_f_spline = np.append(grid_f_spline, y)
    return np.vstack((grid_t_extended, grid_f_spline))


def cubic_spline_grid_wiki(grid, eps=np.float32(0.1)):
    t = grid[0]
    N = t.shape[0]
    grid_t_extended = np.array([])
    grid_f_spline = np.array([])
    cubic_splines = cubic_spline_coefs_wiki(grid)
    for i in range(N - 1):
        # print(N)
        x = np.linspace(t[i], t[i+1], int(ceil((t[i+1] - t[i]) / eps)))
        y = get_cubic_poly_value_wiki(x, cubic_splines[i])
        grid_t_extended = np.append(grid_t_extended, x)
        # print(grid_t_extended)
        grid_f_spline = np.append(grid_f_spline, y)
    return np.vstack((grid_t_extended, grid_f_spline))


def cubic_spline_plot(grid, eps=None):
    if eps is not None:
        grid_spline = cubic_spline_grid(grid, eps)
    else:
        grid_spline = cubic_spline_grid(grid)
    # print(grid_spline)
    plt.plot(grid_spline[0], grid_spline[1])
    plt.title("Cubic spline")
    plt.grid(True)
    plt.show()


def example(func, a, b, n, N):
    func_v = np.vectorize(func, otypes=[np.float32])
    x = np.linspace(a, b, N)
    y = func_v(x)
    x_ = np.linspace(a, b, n)
    y_ = func_v(x_)
    grid = np.vstack((x_, y_))
    grid_spline = cubic_spline_grid_wiki(grid)
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    ax1.set_title(r'$Real$')
    ax1.plot(x, y)
    ax2.set_title(r'$Welcome \ my \ Spline$')
    ax2.plot(grid_spline[0], grid_spline[1])
    f.show()


def error(func, a, b, n):
    func_v = np.vectorize(func, otypes=[np.float32])
    x_ = np.linspace(a, b, n)
    y_ = func_v(x_)
    grid = np.vstack((x_, y_))
    grid_spline = cubic_spline_grid_wiki(grid)
    y = func_v(grid_spline[0])
    plt.figure(figsize=(20, 10))
    plt.plot(grid_spline[0], np.abs((grid_spline[1] - y) / y) * 100)
    plt.title("Error", fontsize=20)
    plt.xlabel("Grid", fontsize=15)
    plt.ylabel("Error percentage", fontsize=15)
    plt.grid(True)
    plt.show()


def example_compare(func, label, a, b, n):
    func_v = np.vectorize(func, otypes=[np.float32])
    x_ = np.linspace(a, b, n)
    y_ = func_v(x_)
    grid = np.vstack((x_, y_))
    grid_spline = cubic_spline_grid_wiki(grid)
    plt.figure(figsize=(20, 10))
    y = func_v(grid_spline[0])
    plt.plot(grid_spline[0], y, label="Real function{}".format(label))
    plt.plot(grid_spline[0], grid_spline[1], label="Spline function of mine")
    plt.plot(grid_spline[0], np.abs((grid_spline[1] - y) / y) * 100, label="Error percentage")
    plt.title("Comparison", fontsize=18)
    # plt.xlabel("Grid", fontsize=15)
    # plt.ylabel("Error", fontsize=15)
    plt.grid(True)
    plt.legend(fontsize=18)
    plt.show()


func = functions.f, functions.g, functions.h
labels = ['f', 'g', 'h']
for f, label in zip(func, labels):
    example_compare(f, label, -5, 5, 20)
