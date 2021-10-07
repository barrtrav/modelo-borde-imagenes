# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UiForm/edge_param.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(259, 102)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UiForm/../../icons/python.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 70, 170, 30))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(110, 10, 140, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setEnabled(True)
        self.spinBox.setGeometry(QtCore.QRect(180, 40, 70, 20))
        self.spinBox.setMinimum(3)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(100, 40, 50, 20))
        self.label_2.setObjectName("label_2")
        self.radioButton_1 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_1.setGeometry(QtCore.QRect(10, 40, 70, 20))
        self.radioButton_1.setCheckable(True)
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 40, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 40, 80, 20))
        self.radioButton_3.setObjectName("radioButton_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edges Type"))
        self.comboBox.setItemText(0, _translate("Dialog", "Farid"))
        self.comboBox.setItemText(1, _translate("Dialog", "Laplace"))
        self.comboBox.setItemText(2, _translate("Dialog", "Prewitt"))
        self.comboBox.setItemText(3, _translate("Dialog", "Roberts"))
        self.comboBox.setItemText(4, _translate("Dialog", "Sobel"))
        self.comboBox.setItemText(5, _translate("Dialog", "Scahrr"))
        self.label.setText(_translate("Dialog", "Edges Filters"))
        self.label_2.setText(_translate("Dialog", "K-Size"))
        self.radioButton_1.setText(_translate("Dialog", "&Simple"))
        self.radioButton_2.setText(_translate("Dialog", "&Horizontal"))
        self.radioButton_3.setText(_translate("Dialog", "Ve&rtical"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
