# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/denissurin/Calc_method/calc_method.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 950)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.input_koshi_button = QtWidgets.QPushButton(self.centralwidget)
        self.input_koshi_button.setObjectName("input_koshi_button")
        self.gridLayout.addWidget(self.input_koshi_button, 4, 0, 1, 1)
        self.choose_parametres_grid = QtWidgets.QTabWidget(self.centralwidget)
        self.choose_parametres_grid.setMaximumSize(QtCore.QSize(951, 307))
        self.choose_parametres_grid.setMouseTracking(True)
        self.choose_parametres_grid.setTabletTracking(True)
        self.choose_parametres_grid.setTabBarAutoHide(False)
        self.choose_parametres_grid.setObjectName("choose_parametres_grid")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fuction_ro = QtWidgets.QTextBrowser(self.tab)
        self.fuction_ro.setMinimumSize(QtCore.QSize(0, 31))
        self.fuction_ro.setObjectName("fuction_ro")
        self.gridLayout_2.addWidget(self.fuction_ro, 0, 0, 1, 6)
        self.function_ro_a_button = QtWidgets.QTextBrowser(self.tab)
        self.function_ro_a_button.setObjectName("function_ro_a_button")
        self.gridLayout_2.addWidget(self.function_ro_a_button, 1, 0, 1, 1)
        self.function_ro_a_input = QtWidgets.QTextEdit(self.tab)
        self.function_ro_a_input.setObjectName("function_ro_a_input")
        self.gridLayout_2.addWidget(self.function_ro_a_input, 1, 1, 1, 1)
        self.function_ro_b_button = QtWidgets.QTextEdit(self.tab)
        self.function_ro_b_button.setObjectName("function_ro_b_button")
        self.gridLayout_2.addWidget(self.function_ro_b_button, 1, 2, 1, 1)
        self.function_ro_b_input = QtWidgets.QTextEdit(self.tab)
        self.function_ro_b_input.setObjectName("function_ro_b_input")
        self.gridLayout_2.addWidget(self.function_ro_b_input, 1, 3, 1, 1)
        self.function_S = QtWidgets.QTextBrowser(self.tab)
        self.function_S.setMinimumSize(QtCore.QSize(0, 31))
        self.function_S.setObjectName("function_S")
        self.gridLayout_2.addWidget(self.function_S, 2, 0, 1, 6)
        self.function_S_m_button = QtWidgets.QTextBrowser(self.tab)
        self.function_S_m_button.setObjectName("function_S_m_button")
        self.gridLayout_2.addWidget(self.function_S_m_button, 3, 0, 1, 1)
        self.function_S_m_input = QtWidgets.QTextEdit(self.tab)
        self.function_S_m_input.setObjectName("function_S_m_input")
        self.gridLayout_2.addWidget(self.function_S_m_input, 3, 1, 1, 1)
        self.function_S_n_input_2 = QtWidgets.QTextBrowser(self.tab)
        self.function_S_n_input_2.setObjectName("function_S_n_input_2")
        self.gridLayout_2.addWidget(self.function_S_n_input_2, 3, 2, 1, 1)
        self.function_S_n_input = QtWidgets.QTextEdit(self.tab)
        self.function_S_n_input.setObjectName("function_S_n_input")
        self.gridLayout_2.addWidget(self.function_S_n_input, 3, 3, 1, 1)
        self.function_S_k_input_2 = QtWidgets.QTextBrowser(self.tab)
        self.function_S_k_input_2.setObjectName("function_S_k_input_2")
        self.gridLayout_2.addWidget(self.function_S_k_input_2, 3, 4, 1, 1)
        self.function_S_k_input = QtWidgets.QTextEdit(self.tab)
        self.function_S_k_input.setObjectName("function_S_k_input")
        self.gridLayout_2.addWidget(self.function_S_k_input, 3, 5, 1, 1)
        self.function_z = QtWidgets.QTextBrowser(self.tab)
        self.function_z.setMinimumSize(QtCore.QSize(0, 31))
        self.function_z.setObjectName("function_z")
        self.gridLayout_2.addWidget(self.function_z, 4, 0, 1, 6)
        self.function_z_p_button = QtWidgets.QTextBrowser(self.tab)
        self.function_z_p_button.setObjectName("function_z_p_button")
        self.gridLayout_2.addWidget(self.function_z_p_button, 5, 0, 1, 1)
        self.function_z_p_input = QtWidgets.QTextEdit(self.tab)
        self.function_z_p_input.setObjectName("function_z_p_input")
        self.gridLayout_2.addWidget(self.function_z_p_input, 5, 1, 1, 1)
        self.function_z_q_button = QtWidgets.QTextBrowser(self.tab)
        self.function_z_q_button.setObjectName("function_z_q_button")
        self.gridLayout_2.addWidget(self.function_z_q_button, 5, 2, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 5, 3, 1, 1)
        self.function_z_r_button = QtWidgets.QTextBrowser(self.tab)
        self.function_z_r_button.setObjectName("function_z_r_button")
        self.gridLayout_2.addWidget(self.function_z_r_button, 5, 4, 1, 1)
        self.function_z_r_input = QtWidgets.QTextEdit(self.tab)
        self.function_z_r_input.setObjectName("function_z_r_input")
        self.gridLayout_2.addWidget(self.function_z_r_input, 5, 5, 1, 1)
        self.choose_parametres_grid.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Grid_common_phrase = QtWidgets.QTextBrowser(self.tab_2)
        self.Grid_common_phrase.setGeometry(QtCore.QRect(0, 10, 431, 31))
        self.Grid_common_phrase.setObjectName("Grid_common_phrase")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 70, 51, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 40, 51, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 100, 51, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.ro_choose_file_button = QtWidgets.QPushButton(self.tab_2)
        self.ro_choose_file_button.setGeometry(QtCore.QRect(50, 40, 113, 32))
        self.ro_choose_file_button.setObjectName("ro_choose_file_button")
        self.s_choose_file_button = QtWidgets.QPushButton(self.tab_2)
        self.s_choose_file_button.setGeometry(QtCore.QRect(50, 70, 113, 32))
        self.s_choose_file_button.setObjectName("s_choose_file_button")
        self.z_choose_file_button = QtWidgets.QPushButton(self.tab_2)
        self.z_choose_file_button.setGeometry(QtCore.QRect(50, 100, 113, 32))
        self.z_choose_file_button.setObjectName("z_choose_file_button")
        self.choose_parametres_grid.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.choose_parametres_grid, 1, 0, 1, 1)
        self.parametres_button = QtWidgets.QPushButton(self.centralwidget)
        self.parametres_button.setObjectName("parametres_button")
        self.gridLayout.addWidget(self.parametres_button, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(260, 241))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.x0_koshi_text = QtWidgets.QTextBrowser(self.groupBox)
        self.x0_koshi_text.setGeometry(QtCore.QRect(0, 30, 81, 51))
        self.x0_koshi_text.setObjectName("x0_koshi_text")
        self.x0_koshi_input = QtWidgets.QTextEdit(self.groupBox)
        self.x0_koshi_input.setGeometry(QtCore.QRect(80, 30, 104, 51))
        self.x0_koshi_input.setObjectName("x0_koshi_input")
        self.y0_koshi_text = QtWidgets.QTextBrowser(self.groupBox)
        self.y0_koshi_text.setGeometry(QtCore.QRect(0, 80, 81, 51))
        self.y0_koshi_text.setObjectName("y0_koshi_text")
        self.y0_koshi_input = QtWidgets.QTextEdit(self.groupBox)
        self.y0_koshi_input.setGeometry(QtCore.QRect(80, 80, 104, 51))
        self.y0_koshi_input.setObjectName("y0_koshi_input")
        self.t_koshi_text = QtWidgets.QTextBrowser(self.groupBox)
        self.t_koshi_text.setGeometry(QtCore.QRect(0, 130, 81, 51))
        self.t_koshi_text.setObjectName("t_koshi_text")
        self.t_koshi_input = QtWidgets.QTextEdit(self.groupBox)
        self.t_koshi_input.setGeometry(QtCore.QRect(80, 130, 101, 51))
        self.t_koshi_input.setObjectName("t_koshi_input")
        self.beta_koshi_text = QtWidgets.QTextBrowser(self.groupBox)
        self.beta_koshi_text.setGeometry(QtCore.QRect(0, 180, 81, 51))
        self.beta_koshi_text.setObjectName("beta_koshi_text")
        self.beta_koshi_input = QtWidgets.QTextEdit(self.groupBox)
        self.beta_koshi_input.setGeometry(QtCore.QRect(80, 180, 104, 51))
        self.beta_koshi_input.setObjectName("beta_koshi_input")
        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)
        self.Common_inforamtion = QtWidgets.QTextBrowser(self.centralwidget)
        self.Common_inforamtion.setObjectName("Common_inforamtion")
        self.gridLayout.addWidget(self.Common_inforamtion, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.choose_parametres_grid.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_koshi_button.setText(_translate("MainWindow", "input_koshi_done"))
        self.fuction_ro.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Задайте параметры функции p(w) = aw(b - w): </p></body></html>"))
        self.function_ro_a_button.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a</p></body></html>"))
        self.function_ro_b_button.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b</p></body></html>"))
        self.function_S.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Задайте параметры функции S(t) = mt + n*sin(kt): </p></body></html>"))
        self.function_S_m_button.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">m</p></body></html>"))
        self.function_S_n_input_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">n</p></body></html>"))
        self.function_S_k_input_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">k</p></body></html>"))
        self.function_z.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Задайте параметры функции z(t) = pt + q * cos(rt): </p></body></html>"))
        self.function_z_p_button.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">p</p></body></html>"))
        self.function_z_q_button.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">q</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.function_z_r_button.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">r</p></body></html>"))
        self.choose_parametres_grid.setTabText(self.choose_parametres_grid.indexOf(self.tab), _translate("MainWindow", "Parametres"))
        self.Grid_common_phrase.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Можно загрузить сетки для функций:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">S(t):</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">p(w):</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Z(t):</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ro_choose_file_button.setText(_translate("MainWindow", "Choose file"))
        self.s_choose_file_button.setText(_translate("MainWindow", "Choose file"))
        self.z_choose_file_button.setText(_translate("MainWindow", "Choose file"))
        self.choose_parametres_grid.setTabText(self.choose_parametres_grid.indexOf(self.tab_2), _translate("MainWindow", "Grid"))
        self.parametres_button.setText(_translate("MainWindow", "input_done"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры задачи Коши:"))
        self.x0_koshi_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X0:</p></body></html>"))
        self.y0_koshi_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Y0:</p></body></html>"))
        self.t_koshi_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">T:</p></body></html>"))
        self.beta_koshi_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">beta:</p></body></html>"))
        self.Common_inforamtion.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Дополнительные ограничения, накладываемые на задачу:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">0 &lt;= y &lt;=1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">S\'(t) &lt; z\'(t)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">integrate from 0 to 1: p(w)dw = 1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

