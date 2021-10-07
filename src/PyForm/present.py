from PyUi import Ui_Dialog_Present
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QTimer, Qt

class Present(QDialog, Ui_Dialog_Present):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.maxvalue = 100

        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(self.maxvalue)

        self.step = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)
        self.timer.start(self.maxvalue)

    def update_func(self):
        self.step += 1
        self.progressBar.setValue(self.step)

        if self.step > self.maxvalue:
            self.close()
