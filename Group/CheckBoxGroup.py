# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckBoxGroup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(703, 537)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.pushButton_Group = QtWidgets.QPushButton(Form)
        self.pushButton_Group.setGeometry(QtCore.QRect(580, 500, 93, 28))
        self.pushButton_Group.setObjectName("pushButton_Group")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(390, 60, 261, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Group = QtWidgets.QLabel(self.widget)
        self.label_Group.setObjectName("label_Group")
        self.horizontalLayout.addWidget(self.label_Group)
        self.comboBox_Group = QtWidgets.QComboBox(self.widget)
        self.comboBox_Group.setObjectName("comboBox_Group")
        self.comboBox_Group.addItem("")
        self.comboBox_Group.addItem("")
        self.comboBox_Group.addItem("")
        self.comboBox_Group.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_Group)
        self.pushButton_add = QtWidgets.QPushButton(self.widget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(self.widget)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.horizontalLayout.addWidget(self.pushButton_remove)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(20, 20, 217, 340))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setMinimumSize(QtCore.QSize(40, 80))
        self.label.setStyleSheet("border-image:url(:/Michelangelo/Michelangelo.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.checkBox_name = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_name.setCheckable(False)
        self.checkBox_name.setChecked(False)
        self.checkBox_name.setObjectName("checkBox_name")
        self.verticalLayout.addWidget(self.checkBox_name)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setMinimumSize(QtCore.QSize(40, 80))
        self.label_3.setStyleSheet("border-image:url(:/Michelangelo/Michelangelo.jpg)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.checkBox_name_2 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_name_2.setCheckable(False)
        self.checkBox_name_2.setChecked(False)
        self.checkBox_name_2.setObjectName("checkBox_name_2")
        self.verticalLayout_2.addWidget(self.checkBox_name_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setMinimumSize(QtCore.QSize(40, 80))
        self.label_4.setStyleSheet("border-image:url(:/Michelangelo/Michelangelo.jpg)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.checkBox_name_3 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_name_3.setCheckable(False)
        self.checkBox_name_3.setChecked(False)
        self.checkBox_name_3.setObjectName("checkBox_name_3")
        self.verticalLayout_3.addWidget(self.checkBox_name_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setMinimumSize(QtCore.QSize(40, 80))
        self.label_5.setStyleSheet("border-image:url(:/Michelangelo/Michelangelo.jpg)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.checkBox_name_4 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_name_4.setCheckable(False)
        self.checkBox_name_4.setChecked(False)
        self.checkBox_name_4.setObjectName("checkBox_name_4")
        self.verticalLayout_4.addWidget(self.checkBox_name_4)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setMinimumSize(QtCore.QSize(40, 80))
        self.label_6.setStyleSheet("border-image:url(:/Michelangelo/Michelangelo.jpg)")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.checkBox_name_5 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_name_5.setCheckable(False)
        self.checkBox_name_5.setChecked(False)
        self.checkBox_name_5.setObjectName("checkBox_name_5")
        self.verticalLayout_5.addWidget(self.checkBox_name_5)
        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setMinimumSize(QtCore.QSize(40, 80))
        self.label_7.setStyleSheet("border-image:url(:/Michelangelo/Michelangelo.jpg)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.checkBox_name_6 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_name_6.setCheckable(False)
        self.checkBox_name_6.setChecked(False)
        self.checkBox_name_6.setObjectName("checkBox_name_6")
        self.verticalLayout_6.addWidget(self.checkBox_name_6)
        self.gridLayout.addLayout(self.verticalLayout_6, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Group.setText(_translate("Form", "分组"))
        self.label_Group.setText(_translate("Form", "组一"))
        self.comboBox_Group.setItemText(0, _translate("Form", "Teacher"))
        self.comboBox_Group.setItemText(1, _translate("Form", "student1"))
        self.comboBox_Group.setItemText(2, _translate("Form", "student2"))
        self.comboBox_Group.setItemText(3, _translate("Form", "student3"))
        self.pushButton_add.setText(_translate("Form", "添加"))
        self.pushButton_remove.setText(_translate("Form", "移除"))
        self.checkBox_name.setText(_translate("Form", "米开朗基罗"))
        self.checkBox_name_2.setText(_translate("Form", "米开朗基罗"))
        self.checkBox_name_3.setText(_translate("Form", "米开朗基罗"))
        self.checkBox_name_4.setText(_translate("Form", "米开朗基罗"))
        self.checkBox_name_5.setText(_translate("Form", "米开朗基罗"))
        self.checkBox_name_6.setText(_translate("Form", "米开朗基罗"))

import test_rc