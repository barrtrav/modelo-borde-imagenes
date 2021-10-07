from PyUi import Ui_Dialog_Edge
from PyQt5.QtWidgets import QDialog

class EdgeParam(QDialog, Ui_Dialog_Edge):
    '''
    Clase encargada de recopilar los parametros para aplicar el filtro edge.
    '''
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.ksize = None
        self.ftype = None
        self.filter = None
        
        self.buttonBox.accepted.connect(self.AcceptedAction)
        self.comboBox.currentIndexChanged.connect(self.TypeEdgeAction)

        self.label_2.setHidden(True)
        self.spinBox.setHidden(True) 

    def TypeEdgeAction(self):
        edgetype = self.comboBox.currentText()

        if edgetype == 'Roberts':
            self.radioButton_3.setText('&Positive')
            self.radioButton_2.setText('&Negative')
        else:
            self.radioButton_3.setText('Ve&rtical')
            self.radioButton_2.setText('&Horizontal')
      
        if edgetype == 'Laplace':
            self.radioButton_1.setHidden(True)
            self.radioButton_2.setHidden(True)
            self.radioButton_3.setHidden(True)
            self.label_2.setHidden(False)
            self.spinBox.setHidden(False) 
        else:
            self.radioButton_1.setHidden(False)
            self.radioButton_2.setHidden(False)
            self.radioButton_3.setHidden(False)
            self.label_2.setHidden(True)
            self.spinBox.setHidden(True) 

    def AcceptedAction(self):
        self.filter = self.comboBox.currentText()
        
        if self.radioButton_1.isChecked():
            self.ftype = self.radioButton_1.text()
        elif self.radioButton_2.isChecked():
            self.ftype = self.radioButton_2.text()
        else:
            self.ftype = self.radioButton_3.text()
        
        self.ksize = int(self.spinBox.text())