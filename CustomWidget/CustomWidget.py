from PyQt5.QtWidgets import QLabel, QCheckBox, QWidget, QVBoxLayout
from PyQt5.Qt import QPixmap


class CustomWidget(QWidget):
    def __init__(self, title, parent):
        super(CustomWidget, self).__init__(parent=None)
        self.initUI(title)

    def initUI(self, title):
        layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setStyleSheet("QLabel{border-image:url(./images/nullImage.jpg);}")
        self.label.setFixedSize(100, 100)
        self.checkBox = QCheckBox(title, self)
        self.label.setMinimumSize(100, 100)

        layout.addWidget(self.label)
        layout.addWidget(self.checkBox)
        self.setLayout(layout)

    def close(self):
        self.label.close()
        self.checkBox.close()





