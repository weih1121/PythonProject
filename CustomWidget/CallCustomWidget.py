import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from CustomWidget import CustomWidget


class TestForm(QWidget):
    def __init__(self):
        super(TestForm, self).__init__()
        cusWidget = CustomWidget("test", self)
        layout = QHBoxLayout(self)
        layout.addWidget(cusWidget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = TestForm()
    form.show()
    sys.exit(app.exec_())