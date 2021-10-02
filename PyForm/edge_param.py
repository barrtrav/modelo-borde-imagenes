from PyQt5.QtWidgets import QDialog
from PyUi import Ui_Dialog_Edge

class EdgeParam(QDialog, Ui_Dialog_Edge):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.ftype = None
        self.filter = None
        self.ksize = None
        
        self.comboBox.currentIndexChanged.connect(self.TypeEdgeAction)
        self.buttonBox.accepted.connect(self.AcceptedAction)

    def TypeEdgeAction(self):
        filter = self.comboBox.currentText()

        if filter == 'Roberts':
            self.radioButton_1.setEnabled(True)
            self.radioButton_2.setEnabled(True)
            self.radioButton_3.setEnabled(True)

            self.radioButton_2.setText('Positive')
            self.radioButton_3.setText('Negative')
        
        elif filter == 'Laplace':
            self.radioButton_1.setDisabled(True)
            self.radioButton_2.setDisabled(True)
            self.radioButton_3.setDisabled(True)

            self.spinBox.setEnabled(True)
        
        else:
            self.radioButton_1.setEnabled(True)
            self.radioButton_2.setEnabled(True)
            self.radioButton_3.setEnabled(True)

            self.radioButton_2.setText('Horizontal')
            self.radioButton_3.setText('Vertical')

            self.spinBox.setDisabled(True)

    def AcceptedAction(self):
        self.filter = self.comboBox.currentText()
        
        if self.radioButton_1.isChecked():
            self.ftype = self.radioButton_1.text()
        elif self.radioButton_2.isChecked():
            self.ftype = self.radioButton_2.text()
        else:
            self.ftype = self.radioButton_3.text()
        
        self.ksize = int(self.spinBox.text())