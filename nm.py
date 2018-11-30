import design
import sys
import os
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
import numpy as np
import design
from scipy import integrate

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.parametres_button.clicked.connect(self.parametres_done)
        self.ro_choose_file_button.clicked.connect(self.choose_file)
        self.s_choose_file_button.clicked.connect(self.choose_file)
        self.z_choose_file_button.clicked.connect(self.choose_file)
        self.input_koshi_button.clicked.connect(self.koshi)


    def parametres_done(self):
        a = self.function_ro_a_input.toPlainText()
        b = self.function_ro_b_input.toPlainText()
        m = self.function_S_m_input.toPlainText()
        n = self.function_S_n_input.toPlainText()
        k = self.function_S_k_input.toPlainText()
        p = self.function_z_p_input.toPlainText()
        q = self.textEdit_2.toPlainText()
        r = self.function_z_r_input.toPlainText()
        a = float(a)
        b = float(b)
        m = float(m)
        n = float(n)
        k = float(k)
        p = float(p)
        q = float(q)
        r = float(r)
        print(a)
        res = 0
        if a and b and m and n and k and p and q and r:
            self.build_plot_ro(a, b)
            self.build_plot_s(m, n, k)
            self.build_plot_z(p, q, r)
        else:
            return res

    def build_plot_ro(self, a, b):
        s = []
        p = [i for i in range(1, 1000)]
        for i in p:
            s.append(a * i * (b - i))
        plt.title("p(w)")
        plt.plot(p, s)
        plt.xlabel("w")
        plt.ylabel("p(w)")
        plt.show()

    def build_plot_s(self, m, n, k):
        s = []
        p = [i for i in range(1, 1000)]
        for i in p:
            s.append(m * i + n * np.sin(k * i))
        plt.title("S(t)")
        plt.plot(p, s)
        plt.xlabel("t")
        plt.ylabel("S(t)")
        plt.show()


    def build_plot_z(self, p, q, r):
        s = []
        p1 = [i for i in range(1, 1000)]
        for i in p1:
            s.append(p * i + q * np.cos(r * i))
        plt.title("Z(t)")
        plt.plot(p1, s)
        plt.xlabel("t")
        plt.ylabel("Z(t)")
        plt.show()


    def choose_file(self):
        pass


    def koshi(self):
        x = self.x0_koshi_input.toPlainText()
        y = self.y0_koshi_input.toPlainText()
        t = self.t_koshi_input.toPlainText()
        beta = self.beta_koshi_input.toPlainText()


    def build_greed(self, a, b, m, n, k, p, q, r):
        pass


def gen_smooth_curve(a, b, n):
    x = np.linspace(a, b, n)
    y = []
    for i in x:
        y.append(i**2)
    res = []
    res.append(x)
    res.append(y)
    return res


def gen_bursting_curve(a, b, n):
    x = np.linspace(a, b, n)
    y = []
    for i in x:
        if i == 5:
            y.append(0)
        else:
            y.append(1/(i - 5))
    res = []
    res.append(x)
    res.append(y)
    return res


def gen_oscillation(a, b, n):
    x = np.linspace(a, b, n)
    y = []
    for i in x:
        y.append(np.sin(i))
    res = []
    res.append(x)
    res.append(y)
    return res


def integrate_newtone_k(grid):
    res = 0
    for i in range(0, len(grid) - 1):
        cur = ((grid[1][i] + grid[1][i + 1])*(grid[0][i + 1] - grid[0][i])) / 2
        res = res + cur
    e = 0
    for i in range(0, len(grid) - 2):
        cur = ((grid[1][i] + grid[1][i + 2]) * (grid[0][i + 2] - grid[0][i])) / 2
        e = e + cur
    e = e/3
    return res, e


def compare_sc():
    x1 =  lambda x: (x**2)
    a = -10
    b = 10
    res1 = []
    res2 = []
    res3 = []
    x = []
    for i in range(10, 110):
        grid = gen_smooth_curve(a, b, i)
        res1.append(integrate_newtone_k(grid)[0])
        grid = gen_bursting_curve(a, b, i)
        res2.append(integrate_newtone_k(grid)[0])
        grid = gen_oscillation(a, b, i)
        res3.append(integrate_newtone_k(grid)[0])
        x.append(i)
    res_real1 = (a, integrate.quad(x1, a, b))[0]
    # x2 = lambda x: 0 if x - 5 == 0 else (1 / x - 5)
    # res_real2 = (a, integrate.quad(x2, a, b))
    x3 = lambda x: np.sin(x)
    res_real3 = (a, integrate.quad(x3, a, b))[0]
    e1 = []
    e2 = []
    e3 = []
    for i in range(len(x)):
        e1.append(abs(res1[i] - res_real1))
        # e2.append(abs(res2[i] - res_real2))
        e3.append(abs(res3[i] - res_real3))
    plt.plot(x, e1, label="Smooth")
    #plt.plot(x_s, e2, label="Bursting")
    plt.plot(x, e3, label="Oscillation")
    plt.legend()
    plt.xlabel("number of iterations")
    plt.ylabel("Error")
    plt.title("Своими руками vs scipy")
    plt.show()


def count_error():
    a = -1
    b = 1
    x = []
    e1 = []
    e2 = []
    e3 = []
    for i in range(100, 10000, 100):
        grid = gen_smooth_curve(a, b, i)
        e1.append(integrate_newtone_k(grid)[1])
        grid = gen_bursting_curve(a, b, i)
        e2.append(integrate_newtone_k(grid)[1])
        grid = gen_oscillation(a, b, i)
        e3.append(integrate_newtone_k(grid)[1])
        x.append(i)
    plt.plot(x, e1, label="Smooth")
    plt.plot(x, e2, label="Bursting")
    plt.plot(x, e3, label="Oscillation")
    plt.legend()
    plt.xlabel("number of iterations")
    plt.ylabel("Error")
    plt.title("Runge_error")
    plt.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    #main()  # - для показа gui
    compare_sc()
    count_error()