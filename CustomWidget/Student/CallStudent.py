import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from CustomWidget import CustomWidget
from Student.student_form import Ui_Form


class Student_Form(QWidget, Ui_Form):
    __positions = None
    __names = None
    CustomWidgetList = []                                       #定义一个列表，用来存储学生列表中CustomWidget的控件
    def __init__(self):
        super(Student_Form, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.layout_students = QGridLayout()
        self.ui.scrollArea_student.setLayout(self.layout_students)
        scrollArea_student_widget = QWidget()
        self.ui.spinBox_row.setMinimum(1)
        self.ui.spinBox_col.setMinimum(1)


        self.ui.spinBox_row.valueChanged.connect(self.updateWin)
        self.ui.spinBox_col.valueChanged.connect(self.updateWin)

    def updateWin(self):
        row = self.ui.spinBox_row.value()
        col = self.ui.spinBox_col.value()

        if self.CustomWidgetList != None:
            for widgets in self.CustomWidgetList:
                widgets.close()

        positions = [(i, j) for i in range(row) for j in range(col)]
        names = []

        for x in range(row * col):
            names.append("Student" + str(x))

        for position, name in zip(positions, names):
            widget = CustomWidget(name, self)
            self.layout_students.addWidget(widget, *position)
            self.CustomWidgetList.append(widget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Student_Form()
    win.show()
    sys.exit(app.exec_())
