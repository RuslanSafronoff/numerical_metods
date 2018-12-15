import numpy as np
import spline


def integrate_trapezoidal(grid):
    x = grid[0]
    y = grid[1]
    return (((y[1:] + y[:-1]) / 2) * (x[1:] - x[:-1])).sum()


def integrate_trapezoidal_func(f, a, b, N):
    f_v = np.vectorize(f, otypes=[np.float32])
    x = np.linspace(a, b, N)
    y = f_v(x)
    return (((y[1:] + y[:-1]) / 2) * (x[1:] - x[:-1])).sum()


def integrate_simpson(grid):
    x = grid[0]
    y = grid[1]
    h = x[1] - x[0]
    return h / 3 * (y[0] + y[-1] + 4 * y[1::2] + 2 * y[2::3])


def integrate_simpson_func(f, a, b, N):
    f_v = np.vectorize(f, otypes=[np.float32])
    x = np.linspace(a, b, N)
    y = f_v(x)
    h = x[1] - x[0]
    return h / 3 * (y[0].sum() + y[-1].sum() + 4 * y[1::2].sum() + 2 * y[2::3].sum())


def integrate_plus_spline(f, t, n=1000):
    N = t.shape[0]
    I = np.zeros(N)
    I[0] = 0
    for i in range(N-1):
        I[i + 1] = I[i] + integrate_simpson_func(f, t[i], t[i + 1], n)
    return spline.cubic_spline_coefs(np.vstack((t, I)))


def integrate(grid, method="simpson"):
    if method is "simpson":
        return integrate_simpson(grid)
    elif method is "trapezoidal":
        return integrate_trapezoidal(grid)

