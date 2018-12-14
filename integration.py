def integrate_trapezoidal(grid):
    x = grid[0]
    y = grid[1]
    return (((y[1:] + y[:-1]) / 2) * (x[1:] - x[:-1])).sum()
