import sys  # sys нужен для передачи argv в QApplication
import os
import numpy as np
from os.path import expanduser
from PyQt5 import QtWidgets, QtCore
import design, design_p, design_c
import matplotlib.pyplot as plt
import pandas as pd
import spline

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


class Param(QtWidgets.QDialog, design_p.Ui_Dialog):
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


class Couchy(QtWidgets.QDialog, design_c.Ui_Dialog):
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


class Main(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.Param = None
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.rho_a = 0
        self.rho_b = 0
        self.s_k = 0
        self.s_m = 0
        self.s_n = 0
        self.z_p = 0
        self.z_q = 0
        self.z_r = 0
        self.x0 = 0
        self.y0 = 0
        self.t = 0
        self.beta = 0
        self.rho_grid = None
        self.s_grid = None
        self.z_grid = None
        self.setup_signals()

    def setup_signals(self):
        # Connect button to openSisterWin
        self.pushButton_rho_g.clicked.connect(lambda: self.browse_folder("rho"))
        self.pushButton_s_g.clicked.connect(lambda: self.browse_folder("s"))
        self.pushButton_z_g.clicked.connect(lambda: self.browse_folder("z"))
        self.pushButton_p.clicked.connect(self.params)
        # self.pushButton_s_p.clicked.connect(self.params)
        # self.pushButton_z_p.clicked.connect(self.params)
        self.pushButton_cauchy.clicked.connect(self.couchy)

    def params(self, checked=None):
        if checked is None: return
        # dialog = QtWidgets.QDialog()
        # dialog.ui = Param()
        # dialog.ui.setupUi(dialog)

        dialog = Param()
        # dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        result = dialog.exec_()
        # self.rho_a = dialog.ui.doubleSpinBox_rho_a.value()
        # self.rho_b = dialog.ui.doubleSpinBox_rho_b.value()
        # self.s_k = dialog.ui.doubleSpinBox_s_k.value()
        # self.s_m = dialog.ui.doubleSpinBox_s_m.value()
        # self.s_n = dialog.ui.doubleSpinBox_s_n.value()
        # self.z_p = dialog.ui.doubleSpinBox_z_p.value()
        # self.z_q = dialog.ui.doubleSpinBox_z_q.value()
        # self.z_r = dialog.ui.doubleSpinBox_z_r.value()
        if result:
            self.rho_a = dialog.doubleSpinBox_rho_a.value()
            self.rho_b = dialog.doubleSpinBox_rho_b.value()
            self.s_k = dialog.doubleSpinBox_s_k.value()
            self.s_m = dialog.doubleSpinBox_s_m.value()
            self.s_n = dialog.doubleSpinBox_s_n.value()
            self.z_p = dialog.doubleSpinBox_z_p.value()
            self.z_q = dialog.doubleSpinBox_z_q.value()
            self.z_r = dialog.doubleSpinBox_z_r.value()
            self.plots()

    def couchy(self, checked=None):
        if checked is None:
            return
        dialog = Couchy()
        result = dialog.exec_()
        if result:
            self.x0 = dialog.doubleSpinBox_x0.value()
            self.y0 = dialog.doubleSpinBox_y0.value()
            self.t = dialog.doubleSpinBox_t.value()
            self.beta = dialog.doubleSpinBox_beta.value()

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
        directory = QtWidgets.QFileDialog.getOpenFileName(self, directory=home, filter="Array files (*.csv)")
        # print(type(button))
        if directory[0] == '':
            return
        if button == "rho":
            self.rho_grid = directory[0]
            self.grid_handler(self.rho_grid, "rho")
            # print(directory[0])
        if button == "s":
            self.s_grid = directory[0]
            self.grid_handler(self.s_grid, "s")
            # print(directory[0])
        if button == "z":
            self.z_grid = directory[0]
            self.grid_handler(self.z_grid, "z")
            # print(directory[0])
        # self.files.append(directory[0])

    def plots(self):
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
    # def s(self, checked=None):
        # dialog = QtWidgets.QApplication()
        # dialog.ui = Grid()
        # dialog.ui.setupUi(dialog)
        # # dialog.setAttribute(QtCore.Q)
        # dialog.exec_()
        # if checked is None:
        #     return

        # if checked == None: return
        # dialog = QtWidgets.QMainWindow()
        # dialog.ui = Grid()
        # dialog.ui.setupUi(dialog)
        # dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # dialog.exec_()

        #app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        # window = Grid()  # Создаём объект класса ExampleApp
        # window.show()  # Показываем окно
        # window.exec_()
        # dialog = Grid()
        #app.exec_()
        # app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        # window = ExampleAppS()  # Создаём объект класса ExampleApp_s
        # window.show()  # Показываем окно
        # app.exec_()

    # def browse_folder(self):
    #     self.listWidget.clear()  # На случай, если в списке уже есть элементы
    #     file_dialog = QtWidgets.QFileDialog(self)
    #     file_dialog.setNameFilters(["Array files (*.csv)"])
    #     directory = file_dialog.getSaveFileName(self, "Choose file")
    #     # открыть диалог выбора директории и установить значение переменной
    #     # равной пути к выбранной директории
    #
    #     if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
    #         for file_name in os.listdir(directory):  # для каждого файла в директории
    #             self.listWidget.addItem(file_name)   # добавить файл в listWidget

# def main():
#     app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
#     window = ExampleApp()  # Создаём объект класса ExampleApp
#     window.show()  # Показываем окно
#     app.exec_()  # и запускаем приложение
#
# if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#     main()  # то запускаем функцию main()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Main()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
