# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UiForm/threshold_param.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(354, 324)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 280, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 10, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 101, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 90, 161, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 67, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 140, 67, 21))
        self.label_4.setObjectName("label_4")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(260, 130, 69, 26))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 190, 67, 17))
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(175, 180, 161, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 240, 67, 17))
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(260, 230, 69, 26))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(280, 50, 48, 26))
        self.spinBox.setMinimum(1)
        self.spinBox.setSingleStep(2)
        self.spinBox.setObjectName("spinBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Threshold Param"))
        self.comboBox.setItemText(0, _translate("Dialog", "Local"))
        self.comboBox.setItemText(1, _translate("Dialog", "Niblack"))
        self.label.setText(_translate("Dialog", "Threshold Type"))
        self.label_2.setText(_translate("Dialog", "Block Size"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "gaussian"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "generic"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "mean"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "median"))
        self.label_3.setText(_translate("Dialog", "Method"))
        self.label_4.setText(_translate("Dialog", "Offset"))
        self.label_5.setText(_translate("Dialog", "Mode"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "reflect"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "constant"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "nearest"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "mirror"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "wrap"))
        self.label_6.setText(_translate("Dialog", "Scalar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
