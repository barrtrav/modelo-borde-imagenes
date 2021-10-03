from PyQt5.QtWidgets import QDialog
from PyUi import Ui_Dialog_Gauss

class GaussParam(QDialog, Ui_Dialog_Gauss):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.sigma = None
        self.mode = None
        self.scalar = 0

        self.comboBox.currentIndexChanged.connect(self.ModelAction)
        self.buttonBox.accepted.connect(self.AcceptedAction)

    def ModelAction(self):
        mode = self.comboBox.currentText()

        if mode == 'constant':
            self.doubleSpinBox.setEnabled(True)
        else:
            self.doubleSpinBox.setDisabled(True)

    def AcceptedAction(self):
        self.sigma = int(self.spinBox.text())
        self.mode = self.comboBox.currentText()
        self.scalar = float(self.doubleSpinBox.text())