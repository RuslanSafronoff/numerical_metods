import sys  # sys нужен для передачи argv в QApplication
import os
import numpy as np
import pandas as pd
import pyqtgraph as pg
import random
from os.path import expanduser
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout,\
    QSizePolicy, QMessageBox, QWidget, QPushButton, QDialog, QFileDialog, QGraphicsScene, QDesktopWidget
from PyQt5.QtGui import QIcon
import design, design_p, design_c
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import spline
import functions
import synthesis
import integration
import differentiation

# class ExampleApp_s(QtWidgets.QMainWindow, design_s.Ui_MainWindow):
#     def __init__(self):
#         # Это здесь нужно для доступа к переменным, методам
#         # и т.д. в файле design.py
#         super().__init__()
#         self.setupUi(self)  # Это нужно для инициализации нашего дизайна
#         self.btnBrowse.clicked.connect(self.browse_folder())
#
#     def browse_folder(self):
#         self.listWidget.clear()  # На случай, если в списке уже есть элементы
#         file_dialog = QtWidgets.QFileDialog(self)
#         file_dialog.setNameFilters(["Array files (*.csv)"])
#         directory = file_dialog.getSaveFileName(self, "Choose file")
#         # открыть диалог выбора директории и установить значение переменной
#         # равной пути к выбранной директории
#
#         if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
#             for file_name in os.listdir(directory):  # для каждого файла в директории
#                 self.listWidget.addItem(file_name)   # добавить файл в listWidget
#
#


class Params(QDialog, design_p.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        # self.btnBrowse.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки
        # self.buttonBox.clicked.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)
        # self.accepted.connect(self.accept)
        # self.rejected.connect(self.reject)
        # self.rho_a = self.doubleSpinBox_rho_a.value()
        # self.rho_b = self.doubleSpinBox_rho_b.value()
        # self.s_k = self.doubleSpinBox_s_k.value()
        # self.s_m = self.doubleSpinBox_s_m.value()
        # self.s_n = self.doubleSpinBox_s_n.value()
        # self.z_p = self.doubleSpinBox_z_p.value()
        # self.z_q = self.doubleSpinBox_z_q.value()
        # self.z_r = self.doubleSpinBox_z_r.value()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
    
    def show(self): return

    def GetArray(self, func): return
    # def browse_folder(self):
        # self.listWidget.clear()  # На случай, если в списке уже есть элементы
        # directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose file")

        # file_dialog = QtWidgets.QFileDialog(self)
        # the name filters must be a list
        # file_dialog.setNameFilters(["Array files (*.csv)"])
        # file_dialog.selectNameFilter("Array files (*.csv)")
        # show the dialog
        # file_dialog.exec_()
        # home = expanduser("~")
        # directory = QtWidgets.QFileDialog.getOpenFileName(self, directory=home, filter="Array files (*.csv)")
        # self.files.append(directory[0])
        # print(directory[0])
        # file_dialog = QtWidgets.QFileDialog(self)
        # file_dialog.setNameFilters(["Array files (*.csv)"])
        # directory = file_dialog.getExistingDirectory(self, "Choose file")

        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        # if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
        #     for file_name in os.listdir(directory):  # для каждого файла в директории
        #         self.listWidget.addItem(file_name)   # добавить файл в listWidget


class CauchyDialog(QDialog, design_c.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        # self.btnBrowse.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки
        # self.buttonBox.clicked.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)
        # self.accepted.connect(self.accept)
        # self.rejected.connect(self.reject)
        # self.rho_a = self.doubleSpinBox_rho_a.value()
        # self.rho_b = self.doubleSpinBox_rho_b.value()
        # self.s_k = self.doubleSpinBox_s_k.value()
        # self.s_m = self.doubleSpinBox_s_m.value()
        # self.s_n = self.doubleSpinBox_s_n.value()
        # self.z_p = self.doubleSpinBox_z_p.value()
        # self.z_q = self.doubleSpinBox_z_q.value()
        # self.z_r = self.doubleSpinBox_z_r.value()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        # self.rho_a = self.doubleSpinBox_rho_a.value()
        # self.rho_b = self.doubleSpinBox_rho_b.value()
        # self.s_k = self.doubleSpinBox_s_k.value()
        # self.s_m = self.doubleSpinBox_s_m.value()
        # s_n = self.doubleSpinBox_s_n.value()
        # z_p = self.doubleSpinBox_z_p.value()
        # z_q = self.doubleSpinBox_z_q.value()
        # z_r = self.doubleSpinBox_z_r.value()


class Cauchy:
    def __init__(self, x0=None, y0=None, T=None, beta=None):
        self.x0 = x0
        self.y0 = y0
        self.T = T
        self.beta = beta


class S:
    def __init__(self, mode="default", s_k=None, s_m=None, s_n=None, grid=None, N=5000):
        self.mode = mode
        if self.mode is not "default":
            self.grid = grid
        else:
            self.N = N
            self.s_k = s_k
            self.s_m = s_m
            self.s_n = s_n


class Z:
    def __init__(self, mode="default", z_p=None, z_q=None, z_r=None, grid=None, N=5000):
        self.mode = mode
        if self.mode is not "default":
            self.grid = grid
        else:
            self.N = N
            self.z_p = z_p
            self.z_q = z_q
            self.z_r = z_r


class Rho:
    def __init__(self, mode="default", rho_a=None, rho_b=None, grid=None, N=5000):
        self.mode = mode
        if self.mode is not "default":
            self.grid = grid
        else:
            self.N = N
            self.rho_a = rho_a
            self.rho_b = rho_b



class Main(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.Param = None
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.Cauchy = None
        self.S = None
        self.Rho = None
        self.Z = None
        self.files = None
        self.setup_signals()
        # width = self.graphicsView.viewport().width() / 8
        # height = self.graphicsView.viewport().height() / 8
        # print(self.graphicsView.adjustSize())
        # print(self.graphicsView.frameSize())
        # width = self.graphicsView.width() / 100
        # height = self.graphicsView.height() / 100
        # m = Dashboard(parent=self.graphicsView.scene(), width=4, height=5)
        # m.move(0, 0)
        # print(self.graphicsView.scene())
        # self.graphicsView.scene().clear()
        # app = App()
        # app.exec_()
        # directory = "tabulated"
        # if not os.path.exists(directory):
        #     os.makedirs(directory)

    def setup_signals(self):
        self.pushButton_rho_g.clicked.connect(lambda: self.browse_folder("rho"))
        self.pushButton_s_g.clicked.connect(lambda: self.browse_folder("s"))
        self.pushButton_z_g.clicked.connect(lambda: self.browse_folder("z"))
        self.pushButton_p.clicked.connect(self.params)
        self.pushButton_cauchy.clicked.connect(self.cauchy_dialog)
        self.pushButton_example.clicked.connect(self.default)


    def default(self):
        rho, S, z, f = functions.rho, functions.S, functions.z, functions.f
        scene = QGraphicsScene(self)
        self.graphicsView.scene = scene
        self.graphicsView.setScene(scene)
        # self.graphicsView.scene.clear()
        # self.graphicsView.viewport().update()

        # axes = figure.gca()
        figure, ax = plt.subplots(1, 3)
        # ax.set_title("S-x")
        # synthesis.optimizer(ax=ax)
        # ax.grid(True)
        txy = synthesis.odu()[0]
        S_v = np.vectorize(S, otypes=[np.float32])
        ax[1].set_title("S-x")
        ax[1].plot(txy[1], S_v(txy[0]), label='$S(x)$')
        # ax[1].legend(fontsize=15)
        ax[2].set_title("x-t, S-t")
        ax[2].plot(txy[0], txy[1], label='$x(t)$')
        ax[2].plot(txy[0], S_v(txy[0]), label='$S(t)$')
        ax[2].legend(fontsize=15)
        ax[0].set_title("y-t")
        ax[0].plot(txy[0], txy[2])
        # ax[0].legend(fontsize=15)
        ax[0].grid(True)
        ax[1].grid(True)
        ax[2].grid(True)
        canvas = FigureCanvas(figure)
        screen = QDesktopWidget().screenGeometry()
        canvas.setGeometry(0, 0, screen.width(), 400)  # screen.width()
        scene.addWidget(canvas)

    def params(self, checked=None):
        if checked is None:
            return
        dialog = Params()
        result = dialog.exec_()
        if result:
            if self.Rho is None:
                self.Rho = Rho()
                self.Rho.rho_a = dialog.doubleSpinBox_rho_a.value()
                self.Rho.rho_b = dialog.doubleSpinBox_rho_b.value()

            if self.S is None:
                self.S = S()
                self.S.s_k = dialog.doubleSpinBox_s_k.value()
                self.S.s_m = dialog.doubleSpinBox_s_m.value()
                self.S.s_n = dialog.doubleSpinBox_s_n.value()

            if self.Z is None:
                self.Z = Z()
                self.Z.z_p = dialog.doubleSpinBox_z_p.value()
                self.Z.z_q = dialog.doubleSpinBox_z_q.value()
                self.Z.z_r = dialog.doubleSpinBox_z_r.value()
            # self.plots()

    def cauchy_dialog(self, checked=None):
        if checked is None:
            return
        dialog = CauchyDialog()
        result = dialog.exec_()
        if result:
            self.Cauchy.x0 = dialog.doubleSpinBox_x0.value()
            self.Cauchy.y0 = dialog.doubleSpinBox_y0.value()
            self.Cauchy.T = dialog.doubleSpinBox_t.value()
            self.Cauchy.beta = dialog.doubleSpinBox_beta.value()
            scene = QGraphicsScene(self)
            self.graphicsView.scene = scene
            self.graphicsView.setScene(scene)
            figure, ax = plt.subplots(1, 3)
            txy = synthesis.odu(T=self.Cauchy.T, x0=self.Cauchy.x0, y0=self.Cauchy.y0, beta=self.Cauchy.beta)
            S_v = np.vectorize(S, otypes=[np.float32])
            ax[1].set_title("S-x")
            ax[1].plot(txy[1], S_v(txy[0]), label='$S(x)$')
            ax[1].legend(fontsize=15)
            ax[2].set_title("x-t, S-t")
            ax[2].plot(txy[0], txy[1], label='$x(t)$')
            ax[2].plot(txy[0], S_v(txy[0]), label='$S(t)$')
            ax[2].legend(fontsize=15)
            ax[0].set_title("y-t")
            ax[0].plot(txy[0], txy[2])
            ax[0].legend(fontsize=15)
            ax[0].grid(True)
            ax[1].grid(True)
            ax[2].grid(True)
            canvas = FigureCanvas(figure)
            screen = QDesktopWidget().screenGeometry()
            canvas.setGeometry(0, 0, screen.width(), 400)  # screen.width()
            scene.addWidget(canvas)


    # def openSisterWin(self):
    #     # grid = design_s.Ui_MainWindow()
    #     # grid.setupUi(self)
    #     # grid.exec()
    #     if not self:
    #         self.Param = Param()
    #     if self.Param.isVisible():
    #         print('Hiding')
    #         self.Param.hide()
    #         # hide or close, it's your choice
    #         # self.sisterWin.close()
    #     else:
    #         print('Showing')
    #         self.Param.show()

    def browse_folder(self, button):
        home = expanduser("~")
        directory = QFileDialog.getOpenFileName(self, directory=home, filter="Array files (*.csv)")
        if directory[0] == '':
            return
        if self.Rho is not None and button == "rho":
            self.Rho = Rho(mode="grid")
            self.Rho.grid = directory[0]
        if self.S is not None and button == "s":
            self.S = S(mode="grid")
            self.S.grid = directory[0]
        if self.Z is not None and button == "z":
            self.Z = Z(mode="grid")
            self.Z.grid = directory[0]

    def plots(self):
        scene = QGraphicsScene(self)
        self.graphicsView.scene = scene
        self.graphicsView.setScene(scene)
        # self.graphicsView.scene.clear()
        # self.graphicsView.viewport().update()

        # axes = figure.gca()
        figure, ax = plt.subplots(2, 2)
        ax[0, 0].set_title("title")
        xx = [random.random() for i in range(25)]
        yy = [random.random() for i in range(25)]
        # Z = np.ones(25, 25)
        # axes.plot(plt.contourf(xx, yy, Z, cmap=plt.cm.autumn, alpha=0.8))
        ax[0, 0].plot(xx, yy)
        canvas = FigureCanvas(figure)
        screen = QDesktopWidget().screenGeometry()
        canvas.setGeometry(0, 0, screen.width(), 1000)
        scene.addWidget(canvas)
        return

    def plots_(self):
        a, b, k, m, n, p, q, r = self.rho_a, self.rho_b, self.s_k,\
                                        self.s_m, self.s_n, self.z_p, self.z_q,\
                                        self.z_r
        f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 10))
        sp = np.linspace(-10, 10, 100)
        rho = a * sp * (b - sp)
        s = k * sp + m * np.sin(n * sp)
        z = p * sp + q * np.cos(r * sp)
        #     print(a, b, k, m, n, p, q, r, sep=' ')
        #     print(rho, s, z)
        ax1.set_title(r'$\rho(\omega) = a \omega (b - \omega)$', fontsize=18)
        ax2.set_title(r'$S(t) = kt + m \sin (nt)$', fontsize=18)
        ax3.set_title(r'$z(t) = pt + q \cos (rt)$', fontsize=18)
        ax1.grid()
        ax2.grid()
        ax3.grid()
        ax1.plot(sp, rho)
        ax2.plot(sp, s)
        ax3.plot(sp, z)
        plt.show()
        # print(self.rho_grid, self.s_grid, self.z_grid)

    def default_handler_s(self, ax, a, b, N, grid_t = None):
        rho_a, rho_b, k, m, n, p, q, r = self.rho_a, self.rho_b, self.s_k, \
                                 self.s_m, self.s_n, self.z_p, self.z_q, \
                                 self.z_r
        f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 10))
        sp = np.linspace(-10, 10, 100)
        rho = rho_a * sp * (rho_b - sp)
        s = k * sp + m * np.sin(n * sp)
        z = p * sp + q * np.cos(r * sp)
        #     print(a, b, k, m, n, p, q, r, sep=' ')
        #     print(rho, s, z)
        ax1.set_title(r'$\rho(\omega) = a \omega (b - \omega)$', fontsize=18)
        ax2.set_title(r'$S(t) = kt + m \sin (nt)$', fontsize=18)
        ax3.set_title(r'$z(t) = pt + q \cos (rt)$', fontsize=18)
        ax1.grid()
        ax2.grid()
        ax3.grid()
        ax1.plot(sp, rho)
        ax2.plot(sp, s)
        ax3.plot(sp, z)
        plt.show()


    def default_handler_z(self, ax, a, b, N, grid_t = None,):
        rho_a, rho_b, k, m, n, p, q, r = self.rho_a, self.rho_b, self.s_k, \
                                 self.s_m, self.s_n, self.z_p, self.z_q, \
                                 self.z_r
        f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 10))
        sp = np.linspace(-10, 10, 100)
        rho = rho_a * sp * (rho_b - sp)
        s = k * sp + m * np.sin(n * sp)
        z = p * sp + q * np.cos(r * sp)
        #     print(a, b, k, m, n, p, q, r, sep=' ')
        #     print(rho, s, z)
        ax1.set_title(r'$\rho(\omega) = a \omega (b - \omega)$', fontsize=18)
        ax2.set_title(r'$S(t) = kt + m \sin (nt)$', fontsize=18)
        ax3.set_title(r'$z(t) = pt + q \cos (rt)$', fontsize=18)
        ax1.grid()
        ax2.grid()
        ax3.grid()
        ax1.plot(sp, rho)
        ax2.plot(sp, s)
        ax3.plot(sp, z)
        plt.show()


    def default_handler_rho(self, ax, grid_t = None, N=100):
        rho_a, rho_b, k, m, n, p, q, r = self.rho_a, self.rho_b, self.s_k, \
                                 self.s_m, self.s_n, self.z_p, self.z_q, \
                                 self.z_r
        # f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 10))
        if grid_t is None:
            sp = np.linspace(0, 1, N)
            rho = rho_a * sp * (rho_b - sp)
            ax.set_title(r'$\rho(\omega) = a \omega (b - \omega)$', fontsize=18)
            ax.grid()
            ax.plot(sp, rho)
            plt.show()
        else: return




    def grid_handler(self, dir, info="Smth"):
        df = pd.read_csv(dir, index_col=0)
        grid = df.values
        # print(grid.shape)
        if grid.shape[0] == 2:
            # print("YAY")
            if info == "rho":
                # plt.title(r'$\rho(\omega)$', fontsize=18)
                plt.xlabel(r'$\omega$', fontsize=15)
                plt.ylabel(r'$\rho(\omega)$', fontsize=15)
                plt.plot(grid[0], grid[1])
            elif info == "s":
                # plt.title(r'$S(t)$', fontsize=18)
                plt.xlabel(r'$t$', fontsize=15)
                plt.ylabel(r'$S(t)$', fontsize=15)
                plt.plot(grid[0], grid[1])
            elif info == "z":
                plt.xlabel(r'$t$', fontsize=15)
                plt.ylabel(r'$z(t)$', fontsize=15)
                plt.plot(grid[0], grid[1])
            plt.grid()
            plt.show()
            spline.cubic_spline_plot(grid)


class App(QDialog):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = Dashboard(self, width=5, height=4)
        m.move(0, 0)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500, 0)
        button.resize(140, 100)

        self.show()


class Dashboard(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax1, ax2 = self.figure.subplots(2, 1)
        ax1.plot(data, 'r-')
        ax2.plot(data, 'r-')
        ax1.set_title('PyQt Matplotlib Example')
        self.draw()


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Main()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
