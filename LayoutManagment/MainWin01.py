# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin01.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 50, 173, 58))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 370, 195, 128))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit_16)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_17)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_4)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(30, 160, 395, 135))
        self.widget2.setObjectName("widget2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 1, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 2, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 2, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 2, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 2, 3, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 3, 3, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 3, 0, 1, 3)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(10, 10, 310, 30))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "确定"))
        self.pushButton_3.setText(_translate("MainWindow", "确定"))
        self.pushButton_4.setText(_translate("MainWindow", "取消"))
        self.pushButton_5.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "9"))
        self.pushButton_8.setText(_translate("MainWindow", "+"))
        self.pushButton_9.setText(_translate("MainWindow", "4"))
        self.pushButton_11.setText(_translate("MainWindow", "5"))
        self.pushButton_12.setText(_translate("MainWindow", "6"))
        self.pushButton_10.setText(_translate("MainWindow", "-"))
        self.pushButton_16.setText(_translate("MainWindow", "1"))
        self.pushButton_13.setText(_translate("MainWindow", "2"))
        self.pushButton_14.setText(_translate("MainWindow", "3"))
        self.pushButton_15.setText(_translate("MainWindow", "*"))
        self.pushButton_19.setText(_translate("MainWindow", "/"))
        self.pushButton_20.setText(_translate("MainWindow", "计算"))
        self.label.setText(_translate("MainWindow", "姓名"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

