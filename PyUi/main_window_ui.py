# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UiForm/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 241, 581))
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(256, 10, 621, 561))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton_Plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Plus.setGeometry(QtCore.QRect(848, 540, 31, 25))
        self.pushButton_Plus.setObjectName("pushButton_Plus")
        self.pushButton_Minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Minus.setGeometry(QtCore.QRect(810, 540, 31, 25))
        self.pushButton_Minus.setObjectName("pushButton_Minus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Image = QtWidgets.QAction(MainWindow)
        self.actionLoad_Image.setStatusTip("")
        self.actionLoad_Image.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionLoad_Image.setObjectName("actionLoad_Image")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_Group = QtWidgets.QAction(MainWindow)
        self.actionSave_Group.setObjectName("actionSave_Group")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRemove_Image = QtWidgets.QAction(MainWindow)
        self.actionRemove_Image.setObjectName("actionRemove_Image")
        self.menuFile.addAction(self.actionLoad_Image)
        self.menuFile.addAction(self.actionRemove_Image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_Group)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Borde Imagenes"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        self.pushButton_Plus.setText(_translate("MainWindow", "+"))
        self.pushButton_Minus.setText(_translate("MainWindow", "-"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Image.setText(_translate("MainWindow", "Load Image"))
        self.actionLoad_Image.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_Group.setText(_translate("MainWindow", "Save Group"))
        self.actionSave_Group.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionRemove_Image.setText(_translate("MainWindow", "Remove Image"))
        self.actionRemove_Image.setShortcut(_translate("MainWindow", "Ctrl+R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
