# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        MainWindow.setMinimumSize(QtCore.QSize(100, 533))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_s = QtWidgets.QLabel(self.centralwidget)
        self.label_s.setObjectName("label_s")
        self.verticalLayout_2.addWidget(self.label_s, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_s_g = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_s_g.setObjectName("pushButton_s_g")
        self.verticalLayout_2.addWidget(self.pushButton_s_g)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_rho = QtWidgets.QLabel(self.centralwidget)
        self.label_rho.setObjectName("label_rho")
        self.verticalLayout.addWidget(self.label_rho, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_rho_g = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rho_g.setObjectName("pushButton_rho_g")
        self.verticalLayout.addWidget(self.pushButton_rho_g)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_z = QtWidgets.QLabel(self.centralwidget)
        self.label_z.setObjectName("label_z")
        self.verticalLayout_3.addWidget(self.label_z, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_z_g = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_z_g.setObjectName("pushButton_z_g")
        self.verticalLayout_3.addWidget(self.pushButton_z_g)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.pushButton_p = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_p.setObjectName("pushButton_p")
        self.verticalLayout_4.addWidget(self.pushButton_p)
        self.pushButton_cauchy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cauchy.setObjectName("pushButton_cauchy")
        self.verticalLayout_4.addWidget(self.pushButton_cauchy)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(400, 400))
        self.graphicsView.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_4.addWidget(self.graphicsView)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">Scopes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Untitled0x.png\" /></p></td>\n"
"<td></td></tr></table>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Untitled1x.png\" /></p></td>\n"
"<td></td></tr></table>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Untitled2x.png\" /></p></td>\n"
"<td></td></tr></table></body></html>"))
        self.label_s.setText(_translate("MainWindow", "<html><head/><body><p>Enter grid of S(t)</p></body></html>"))
        self.pushButton_s_g.setText(_translate("MainWindow", "Load"))
        self.label_rho.setText(_translate("MainWindow", "<html><head/><body><p>Enter grid of ρ(ω)</p></body></html>"))
        self.pushButton_rho_g.setText(_translate("MainWindow", "Load"))
        self.label_z.setText(_translate("MainWindow", "<html><head/><body><p>Enter grid of z(t)</p></body></html>"))
        self.pushButton_z_g.setText(_translate("MainWindow", "Load"))
        self.pushButton_p.setText(_translate("MainWindow", "Enter parameters of default functions"))
        self.pushButton_cauchy.setText(_translate("MainWindow", "Enter parameters for Cauchy problem "))

