# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UiForm/about_app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutApp(object):
    def setupUi(self, AboutApp):
        AboutApp.setObjectName("AboutApp")
        AboutApp.resize(619, 370)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UiForm/../../icons/python.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutApp.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(AboutApp)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutApp)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(AboutApp)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(AboutApp)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(AboutApp)
        self.buttonBox.accepted.connect(AboutApp.accept)
        self.buttonBox.rejected.connect(AboutApp.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutApp)

    def retranslateUi(self, AboutApp):
        _translate = QtCore.QCoreApplication.translate
        AboutApp.setWindowTitle(_translate("AboutApp", "About App"))
        self.textBrowser.setHtml(_translate("AboutApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; color:#000000;\">Hablar un poco de la aplicacion, decir para que esta hecha, algunas de sus funcionalidades, por supuesto en ingles. Lo de abajo tambien en ingles.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; color:#000000;\">Esta aplicación corre tanto en Window como en Linux, siempre y cuando esté instalado </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; color:#000000;\">python3</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; color:#000000;\"> y </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; color:#000000;\">PyQt5</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; color:#000000;\">.</span></p></body></html>"))
        self.label.setText(_translate("AboutApp", "<html><head/><body><p align=\"center\">About App</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutApp = QtWidgets.QDialog()
    ui = Ui_AboutApp()
    ui.setupUi(AboutApp)
    AboutApp.show()
    sys.exit(app.exec_())
