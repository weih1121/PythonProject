# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1008, 622)
        self.scrollArea_student = QtWidgets.QScrollArea(Form)
        self.scrollArea_student.setGeometry(QtCore.QRect(89, 60, 801, 431))
        self.scrollArea_student.setWidgetResizable(True)
        self.scrollArea_student.setObjectName("scrollArea_student")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_student.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 917, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_RowAndCol = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_RowAndCol.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_RowAndCol.setObjectName("horizontalLayout_RowAndCol")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_RowAndCol.addItem(spacerItem)
        self.horizontalLayout_row = QtWidgets.QHBoxLayout()
        self.horizontalLayout_row.setObjectName("horizontalLayout_row")
        self.label_row = QtWidgets.QLabel(self.layoutWidget)
        self.label_row.setObjectName("label_row")
        self.horizontalLayout_row.addWidget(self.label_row)
        self.spinBox_row = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_row.setObjectName("spinBox_row")
        self.horizontalLayout_row.addWidget(self.spinBox_row)
        self.horizontalLayout_RowAndCol.addLayout(self.horizontalLayout_row)
        self.horizontalLayout_col = QtWidgets.QHBoxLayout()
        self.horizontalLayout_col.setObjectName("horizontalLayout_col")
        self.label_col = QtWidgets.QLabel(self.layoutWidget)
        self.label_col.setObjectName("label_col")
        self.horizontalLayout_col.addWidget(self.label_col)
        self.spinBox_col = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_col.setObjectName("spinBox_col")
        self.horizontalLayout_col.addWidget(self.spinBox_col)
        self.horizontalLayout_RowAndCol.addLayout(self.horizontalLayout_col)
        spacerItem1 = QtWidgets.QSpacerItem(698, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_RowAndCol.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_row.setText(_translate("Form", "行:"))
        self.label_col.setText(_translate("Form", "列:"))

