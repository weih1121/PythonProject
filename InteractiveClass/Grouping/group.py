# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_studentList = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_studentList.setGeometry(QtCore.QRect(20, 40, 471, 501))
        self.scrollArea_studentList.setWidgetResizable(True)
        self.scrollArea_studentList.setObjectName("scrollArea_studentList")
        self.scrollAreaWidgetContents_studentList = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_studentList.setGeometry(QtCore.QRect(0, 0, 469, 499))
        self.scrollAreaWidgetContents_studentList.setObjectName("scrollAreaWidgetContents_studentList")
        self.scrollArea_studentList.setWidget(self.scrollAreaWidgetContents_studentList)
        self.scrollArea_grouplist = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_grouplist.setGeometry(QtCore.QRect(510, 70, 131, 351))
        self.scrollArea_grouplist.setWidgetResizable(True)
        self.scrollArea_grouplist.setObjectName("scrollArea_grouplist")
        self.scrollAreaWidgetContents_groupList = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_groupList.setGeometry(QtCore.QRect(0, 0, 129, 349))
        self.scrollAreaWidgetContents_groupList.setObjectName("scrollAreaWidgetContents_groupList")
        self.scrollArea_grouplist.setWidget(self.scrollAreaWidgetContents_groupList)
        self.label_studentList = QtWidgets.QLabel(self.centralwidget)
        self.label_studentList.setGeometry(QtCore.QRect(20, 10, 54, 12))
        self.label_studentList.setObjectName("label_studentList")
        self.label_groupView = QtWidgets.QLabel(self.centralwidget)
        self.label_groupView.setGeometry(QtCore.QRect(510, 20, 54, 12))
        self.label_groupView.setObjectName("label_groupView")
        self.pushButton_grouping = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_grouping.setGeometry(QtCore.QRect(510, 520, 75, 23))
        self.pushButton_grouping.setObjectName("pushButton_grouping")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(510, 40, 134, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_group = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_group.setObjectName("comboBox_group")
        self.horizontalLayout.addWidget(self.comboBox_group)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 10, 208, 23))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_row = QtWidgets.QLabel(self.layoutWidget1)
        self.label_row.setObjectName("label_row")
        self.horizontalLayout_2.addWidget(self.label_row)
        self.spinBox_row = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_row.setMinimum(1)
        self.spinBox_row.setObjectName("spinBox_row")
        self.horizontalLayout_2.addWidget(self.spinBox_row)
        self.label_col = QtWidgets.QLabel(self.layoutWidget1)
        self.label_col.setObjectName("label_col")
        self.horizontalLayout_2.addWidget(self.label_col)
        self.spinBox_col = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_col.setMinimum(1)
        self.spinBox_col.setObjectName("spinBox_col")
        self.horizontalLayout_2.addWidget(self.spinBox_col)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(510, 430, 131, 23))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_groupNum = QtWidgets.QLabel(self.layoutWidget2)
        self.label_groupNum.setObjectName("label_groupNum")
        self.horizontalLayout_3.addWidget(self.label_groupNum)
        self.spinBox_groupNum = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spinBox_groupNum.setObjectName("spinBox_groupNum")
        self.horizontalLayout_3.addWidget(self.spinBox_groupNum)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar)
        self.action_surf = QtWidgets.QAction(MainWindow)
        self.action_surf.setObjectName("action_surf")
        self.action_grouping = QtWidgets.QAction(MainWindow)
        self.action_grouping.setObjectName("action_grouping")
        self.action_draw = QtWidgets.QAction(MainWindow)
        self.action_draw.setObjectName("action_draw")
        self.action_shortCut = QtWidgets.QAction(MainWindow)
        self.action_shortCut.setObjectName("action_shortCut")
        self.action_shareScreen = QtWidgets.QAction(MainWindow)
        self.action_shareScreen.setObjectName("action_shareScreen")
        self.action_contral = QtWidgets.QAction(MainWindow)
        self.action_contral.setObjectName("action_contral")
        self.toolBar.addAction(self.action_surf)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_grouping)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_draw)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_shortCut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_shareScreen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_contral)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_studentList.setText(_translate("MainWindow", "学生列表:"))
        self.label_groupView.setText(_translate("MainWindow", "小组展示:"))
        self.pushButton_grouping.setText(_translate("MainWindow", "分组"))
        self.label.setText(_translate("MainWindow", "组别:"))
        self.label_row.setText(_translate("MainWindow", "行:"))
        self.label_col.setText(_translate("MainWindow", "列:"))
        self.label_groupNum.setText(_translate("MainWindow", "组数:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_surf.setText(_translate("MainWindow", "上网"))
        self.action_surf.setToolTip(_translate("MainWindow", "<html><head/><body><p>上网</p></body></html>"))
        self.action_grouping.setText(_translate("MainWindow", "分组"))
        self.action_grouping.setToolTip(_translate("MainWindow", "<html><head/><body><p>分组</p></body></html>"))
        self.action_draw.setText(_translate("MainWindow", "画板"))
        self.action_draw.setToolTip(_translate("MainWindow", "<html><head/><body><p>画板</p></body></html>"))
        self.action_shortCut.setText(_translate("MainWindow", "截屏"))
        self.action_shortCut.setToolTip(_translate("MainWindow", "<html><head/><body><p>截屏</p></body></html>"))
        self.action_shareScreen.setText(_translate("MainWindow", "分屏"))
        self.action_shareScreen.setToolTip(_translate("MainWindow", "<html><head/><body><p>屏幕分享</p></body></html>"))
        self.action_contral.setText(_translate("MainWindow", "控制"))
        self.action_contral.setToolTip(_translate("MainWindow", "<html><head/><body><p>控制学生</p></body></html>"))

