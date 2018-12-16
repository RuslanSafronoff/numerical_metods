import numpy as np
import matplotlib.pyplot as plt
from math import ceil
import functions


def cubic_spline_coefs(grid):
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
    Fh = 3 * ((A[2:] - A[1:-1]) / h[1:] - (A[1:-1] - A[:-2]) / h[:-1])  # N-2 shape
    alpha = np.full(N - 2, np.float32(0.))
    beta = np.full(N - 2, np.float32(0.))
    alpha[1] = - Bh[0] / Ch[0]
    beta[1] = Fh[0] / Ch[0]
    for i in range(2, N - 2):
        alpha[i] = - Bh[i - 1] / (Ah[i - 1] * alpha[i - 1] + Ch[i - 1])
        beta[i] = (Fh[i - 1] - Ah[i - 1] * beta[i - 1]) / (Ah[i - 1] * alpha[i - 1] + Ch[i - 1])
    C[-2] = (Fh[-1] - Ah[-1] * beta[-1]) / (Ch[-1] + Ah[-1] * alpha[-1])
    for i in range(N - 3):
        C[N - 3 - i] = alpha[N - 3 - i] * C[N - 2 - i] + beta[N - 3 - i]
    B[1:] = (A[1:] - A[:-1]) / h + (2 * C[1:] + C[:-1]) * h / 3
    D[1:] = (C[1:] - C[:-1]) / h / 3
    cubic_splines = np.hstack((np.expand_dims(A[1:], axis=1),
                               np.expand_dims(B[1:], axis=1),
                               np.expand_dims(C[1:], axis=1),
                               np.expand_dims(D[1:], axis=1),
                               np.expand_dims(t[1:], axis=1)))
    # print(cubic_splines)
    return cubic_splines


def get_cubic_poly_value(t, coefs):
    # print(t.shape)
    T = np.vstack((np.ones(t.shape[0]), (t - coefs[-1]), (t - coefs[-1]) ** 2, (t - coefs[-1]) ** 3))
    # print(T.shape)
    return np.dot(coefs[:-1], T)


def get_poly_offset(t, t0):
    return t - t0


def cubic_spline_grid(grid, eps=np.float32(10e-5)):
    t = grid[0]
    N = t.shape[0]
    grid_t_extended = np.array([])
    grid_f_spline = np.array([])
    cubic_splines = cubic_spline_coefs(grid)
    for i in range(N - 1):
        # print(N)
        x = np.linspace(t[i], t[i+1], int(ceil((t[i+1] - t[i]) / eps)))
        # print(t)
        # print(N)
        y = get_cubic_poly_value(x, cubic_splines[i])
        grid_t_extended = np.append(grid_t_extended, x)
        # print(grid_t_extended)
        grid_f_spline = np.append(grid_f_spline, y)
    return np.vstack((grid_t_extended, grid_f_spline))


def example_compare(func, label, a, b, n, N):
    func_v = np.vectorize(func, otypes=[np.float32])
    x_ = np.linspace(a, b, n)
    y_ = func_v(x_)
    grid = np.vstack((x_, y_))
    grid_spline = cubic_spline_grid(grid)
    plt.figure(figsize=(20, 10))
    x = np.linspace(a, b, N)
    y = func_v(x)
    y_spline = func_v(grid_spline[0])
    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 20))
    ax1.plot(x, y, label=label)
    ax1.plot(grid_spline[0], grid_spline[1], label="Spline function of mine")
    ax2.plot(grid_spline[0], np.abs(grid_spline[1] - y_spline), label="Error abs.")
    ax1.set_title("Comparison", fontsize=18)
    ax2.set_title("Error", fontsize=18)
    # plt.xlabel("Grid", fontsize=15)
    # plt.ylabel("Error", fontsize=15)
    ax1.grid(True)
    ax1.legend(fontsize=18)
    ax2.grid(True)
    ax2.legend(fontsize=18)
    f.show()


def cubic_spline_plot(grid):
    grid_spline = cubic_spline_grid(grid)
    plt.plot(grid_spline[0], grid_spline[1], label="Spline function")
    plt.legend(fontsize=15)
    plt.grid()
    plt.show()


def example(a=0, b=1, n=20, N=5000):
    func = functions.f_, functions.g, functions.h, functions.l
    # example_compare(func[-1], 'l', 0, 1, 20, 5000)
    with open('description.txt', 'r', encoding='utf-8') as g:
        labels = g.readlines()
    for f, label in zip(func, labels):
        example_compare(f, label, a, b, n, N)
    # a = np.array([1, 2, 3])
    # b = np.array([4, 5, 6])
    # c = np.array([7, 8, 9])
    # d = np.hstack((np.expand_dims(a, axis=1),
    #                            np.expand_dims(b, axis=1),
    #                            np.expand_dims(c, axis=1)))
    # print(d[0])


if __name__ == '__main__':
    example()
