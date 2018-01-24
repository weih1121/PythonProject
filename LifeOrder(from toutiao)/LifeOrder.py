# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LifeOrder.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStatusTip("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setStatusTip("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_LifeStyle = QtWidgets.QPushButton(Form)
        self.pushButton_LifeStyle.setStyleSheet("color:rgb(170, 0, 0);background-color:rgb(212, 212, 212)")
        self.pushButton_LifeStyle.setObjectName("pushButton_LifeStyle")
        self.horizontalLayout.addWidget(self.pushButton_LifeStyle)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "人生信条"))
        self.pushButton_LifeStyle.setText(_translate("Form", "人生信条"))

