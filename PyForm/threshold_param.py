from PyQt5.QtWidgets import QDialog
from PyUi import Ui_Dialog_Threshold

class ThresholdParam(QDialog, Ui_Dialog_Threshold):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.type = None
        self.block_size = None
        self.method = None
        self.offset = None
        self.mode = None
        self.scalar = None

        self.comboBox.currentIndexChanged.connect(self.TypeThresholdAction)
        self.buttonBox.accepted.connect(self.AcceptedAction)

    def TypeThresholdAction(self):
        threshtype = self.comboBox.currentText()

        if threshtype == 'Local':
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(True)
            self.doubleSpinBox.setEnabled(True)
            self.label_3.setEnabled(True)
            self.label_4.setEnabled(True)
            self.label_5.setEnabled(True)

            self.label_2.setText('Block Size')
            self.label_6.setText('Scalr')
        
        else:
            self.comboBox_2.setEnabled(False)
            self.comboBox_3.setEnabled(False)
            self.doubleSpinBox.setEnabled(False)
            self.label_3.setEnabled(False)
            self.label_4.setEnabled(False)
            self.label_5.setEnabled(False)

            self.label_2.setText('Window Size')
            self.label_6.setText('k')

    def AcceptedAction(self):
        self.type = self.comboBox.currentText()
        self.block_size = int(self.spinBox.text())
        self.method = self.comboBox_2.currentText()
        self.offset = float(self.doubleSpinBox.text())
        self.mode = self.comboBox_3.currentText()
        self.scalar = float(self.doubleSpinBox_2.text())