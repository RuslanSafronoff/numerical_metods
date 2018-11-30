# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_c.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.doubleSpinBox_x0 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_x0.setObjectName("doubleSpinBox_x0")
        self.horizontalLayout.addWidget(self.doubleSpinBox_x0)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.doubleSpinBox_y0 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_y0.setObjectName("doubleSpinBox_y0")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_y0)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.doubleSpinBox_t = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_t.setObjectName("doubleSpinBox_t")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_t)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.doubleSpinBox_beta = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_beta.setObjectName("doubleSpinBox_beta")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_beta)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head><title>MathML in XHTML</title></head><body><p><span style=\" font-size:18pt;\">X</span><span style=\" font-size:18pt; vertical-align:sub;\">0</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head><title>MathML in XHTML</title></head><body><p><span style=\" font-size:18pt;\">Y</span><span style=\" font-size:18pt; vertical-align:sub;\">0</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head><title>MathML in XHTML</title></head><body><p><span style=\" font-size:18pt;\">T</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head><title>MathML in XHTML</title></head><body><p><span style=\" font-size:18pt;\">&beta;</span></p></body></html>"))

