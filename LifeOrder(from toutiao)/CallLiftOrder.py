import sys
from LifeOrder import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget

class Lift(QWidget, Ui_Form):
    def __init__(self):
        super(Lift, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_LifeStyle.clicked.connect(self.write)


    def write(self):
        self.ui.textEdit.setText("Ten Rules:\nWorkSpace:First appreciate and then promoted\n"
                                 "Communicate:Seek the same before seeking difference\n"
                                 "Implement:Finish first and then perfect\n"
                                 "Study:First Record and then remember\n"
                                 "Design:First copy and then create\n"
                                 "Entrepreneurship:First grow and then succeed\n"
                                 "Devolopment:Stop and then stop high\n"
                                 "Person:First exchange and then pay attention\n"
                                 "Solve Things:First solve the mood and then solve things")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Lift()
    win.show()
    sys.exit(app.exec_())