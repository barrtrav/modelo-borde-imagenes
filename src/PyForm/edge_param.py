from PyUi import Ui_Dialog_Edge
from PyQt5.QtWidgets import QDialog

class EdgeParam(QDialog, Ui_Dialog_Edge):
    '''
    Clase encargada de recopilar los parametros para aplicar el filtro edge.
    '''
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.ftype = None
        self.filter = None
        self.ksize = None
        
        self.comboBox.currentIndexChanged.connect(self.TypeEdgeAction)
        self.buttonBox.accepted.connect(self.AcceptedAction)

    def TypeEdgeAction(self):
        edgetype = self.comboBox.currentText()

        if edgetype == 'Roberts':
            self.radioButton_1.setEnabled(True)
            self.radioButton_2.setEnabled(True)
            self.radioButton_3.setEnabled(True)
            self.radioButton_2.setText('&Positive')
            self.radioButton_3.setText('&Negative')        
        elif edgetype == 'Laplace':
            self.radioButton_1.setDisabled(True)
            self.radioButton_2.setDisabled(True)
            self.radioButton_3.setDisabled(True)
            self.spinBox.setEnabled(True)
        else:
            self.radioButton_1.setEnabled(True)
            self.radioButton_2.setEnabled(True)
            self.radioButton_3.setEnabled(True)
            self.radioButton_2.setText('&Horizontal')
            self.radioButton_3.setText('Ve&rtical')
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