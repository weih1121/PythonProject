import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from Student.student import Ui_Form
from CustomWidget import CustomWidget


class TestForm(QWidget, Ui_Form):
    def __init__(self):
        super(TestForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.layout = QGridLayout()
        self.ui.widget_student.setLayout(self.layout)
        self.ui.spinBox_col.setMinimum(1)
        self.ui.spinBox_row.setMinimum(1)

        self.ui.spinBox_row.valueChanged.connect(self.updateWin)
        self.ui.spinBox_col.valueChanged.connect(self.updateWin)

    def updateWin(self):
        row = self.ui.spinBox_row.value()
        col = self.ui.spinBox_col.value()

        positions = [(i, j)for i in range(row) for j in range(col)]
        names = []

        for x in range(row * col):
            names.append("Stuednt" + str(x + 1))

        for name, position in zip(names, positions):
            widget = CustomWidget(name, self)
            self.layout.addWidget(widget, *position)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = TestForm()
    form.show()
    sys.exit(app.exec_())