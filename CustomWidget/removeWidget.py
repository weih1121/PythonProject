import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from  CustomWidget import CustomWidget

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()

        layout = QVBoxLayout(self)
        button = CustomWidget("Target", self)
        button_remove = QPushButton("remove", self)
        layout.addWidget(button)
        layout.addWidget(button_remove)

        button_remove.clicked.connect(button.close)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())