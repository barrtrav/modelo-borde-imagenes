import webbrowser

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

from PyUi import Ui_MainWindow
from Utils.digital_image import DigitalImage
from PyUi import Ui_About_App, Ui_About_Authors
from PyForm import EdgeParam, GaussParam, ThresholdParam

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.image = None
        self.imagesTree = dict()
        self.timecount = 0
        self.hide_console = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.TimerAction)

        self.menuFile.triggered[QAction].connect(self.MenuFile)
        self.menuFilter.triggered[QAction].connect(self.MenuFilter)
        self.menuOptions.triggered[QAction].connect(self.MenuOptions)
        self.treeWidget.clicked.connect(self.SelectItemAction)
        
        self.pushButton_Plus.clicked.connect(self.EnlargeAction)
        self.pushButton_Minus.clicked.connect(self.ShrinkAction)
        self.pushButton.clicked.connect(self.HideAction)
        self.pushButton_Plus.setHidden(True)
        self.pushButton_Minus.setHidden(True)       

        self.scrollArea.setWidget(self.label)
        self.treeWidget.expanded.connect(self.ExpandAction)

    def HideAction(self):
        if self.hide_console:
            self.hide_console = False
            self.tableWidget.setHidden(False)
            self.pushButton.setIcon(QIcon('../icons/hide.png'))
        else:
            self.hide_console = True
            self.tableWidget.setHidden(True)
            self.pushButton.setIcon(QIcon('../icons/no-hide.png'))
        
        self.resizeEvent(None)
    
    def ExpandAction(self):
        self.treeWidget.resizeColumnToContents(0)

    def MenuOptions(self, triggered):
        if triggered.text() == 'Help':
            self.HelpAction()
        if triggered.text() == 'Orientation':
            self.OrientationAction()
        if triggered.text() == 'Report':
            self.ReportAction()
        if triggered.text() == 'About the Authors':
            self.AboutAuthorsAction()
        if triggered.text() == 'About the App':
            self.AboutAppAction()

    def HelpAction(self):
        pass

    def OrientationAction(self):
        path = '../doc/Bordes Imagenes Medicas.pdf'
        webbrowser.open_new(path)

    def ReportAction(self):
        pass

    def AboutAuthorsAction(self):
        dialog = QDialog()
        ui_dialog = Ui_About_Authors()
        ui_dialog.setupUi(dialog)
        dialog.exec()

    def AboutAppAction(self):
        dialog = QDialog()
        ui_dialog = Ui_About_App()
        ui_dialog.setupUi(dialog)
        dialog.exec()

    def MenuFilter(self, triggered):
        if triggered.text() == 'Edges':
            self.EdgesAction()      
        if triggered.text() == 'Gaussian':
            self.GaussAction()       
        if triggered.text() == 'Threshold':
            self.ThresholdAction()
    
    def ThresholdAction(self):
        thresh = ThresholdParam()
        thresh.exec_()

        if not thresh.type:
            return
        image = self.image.ThresholdFilter(thresh)

        self.imagesTree[image.GetName] = image
        image.widget = QTreeWidgetItem(self.image.widget, [image.GetName])
        self.image = image
        self.UpdateFrame

    def GaussAction(self):
        gauss = GaussParam()
        gauss.exec_()

        if not gauss.sigma:
            return
        image = self.image.GaussFilter(gauss)

        self.imagesTree[image.GetName] = image
        image.widget = QTreeWidgetItem(self.image.widget, [image.GetName])
        self.image = image
        self.UpdateFrame

    def EdgesAction(self):
        edges = EdgeParam()
        edges.exec_()

        if not edges.filter:
            return
        image = self.image.EdgesFilter(edges)
        
        self.imagesTree[image.GetName] = image
        image.widget = QTreeWidgetItem(self.image.widget, [image.GetName])
        self.image = image
        self.UpdateFrame

    def TimerAction(self):
        self.timecount += 1
        if self.timecount > 50000:
            self.pushButton_Plus.setHidden(True)
            self.pushButton_Minus.setHidden(True)
            self.timer.stop()
            self.timecount = 0

    def mouseMoveEvent(self, event):
        if self.image and not self.timecount :
            self.pushButton_Plus.setHidden(False)
            self.pushButton_Minus.setHidden(False)
            self.timer.start()
        elif self.image:
            self.timecount = 0
    
    #def timerEvent(self, event):
    #    if not self.timecount:
    #       self.pushButton_Plus.setHidden(True)
    #        self.pushButton_Minus.setHidden(True)
    #        self.killTimer(event.timerId())
    #    elif self.timecount > 0:
    #        self.timecount -= 1
        
    def resizeEvent(self, event):
        if self.hide_console:
            self.treeWidget.setGeometry(0, 0, self.width()/4, self.height()-44-15)
            self.label.setGeometry(self.width()/4, 0, 3*self.width()/4, self.height()-44-15)
            self.scrollArea.setGeometry(self.width()/4, 0, 3*self.width()/4, self.height()-44-15)
            
            self.pushButton_Plus.setGeometry(self.width()/4 + 15, 15, 25, 25)
            self.pushButton_Minus.setGeometry(self.width()/4 + 45, 15, 25, 25)

            self.pushButton.setGeometry(0, self.height()-44-15, self.width(), 15)
            
        else:
            self.treeWidget.setGeometry(0, 0, self.width()/4, self.height()-44-60-15)
            self.label.setGeometry(self.width()/4, 0, 3*self.width()/4, self.height()-44-60-15)
            self.scrollArea.setGeometry(self.width()/4, 0, 3*self.width()/4, self.height()-44-60-15)
            
            self.pushButton_Plus.setGeometry(self.width()/4 + 15, 15, 25, 25)
            self.pushButton_Minus.setGeometry(self.width()/4 + 45, 15, 25, 25)

            self.pushButton.setGeometry(0, self.height()-44-60-15, self.width(), 15)
            
            self.tableWidget.setGeometry(0, self.height()-44-60, self.width(), 60)
            self.tableWidget.horizontalHeader().setDefaultSectionSize(self.width()/3-4)

    def MenuFile(self, triggered):
        if triggered.text() == 'Load Image':
            self.LoadImageAction()
        if triggered.text() == 'Remove Image':
            self.RemoveImageAction()
        if triggered.text() == 'Save Image':
            self.SaveAction()
        if triggered.text() == 'Save Images in Group':
            self.SaveGroupAction()
        if triggered.text() == 'Exit':
            self.ExitAction()

    def LoadImageAction(self):
        path = QFileDialog.getOpenFileName(self, directory='../img/', caption='Load Image', filter='Image File (*.jpg  *.png)')[0]
        
        if not path:
            return
        self.image = DigitalImage(path)
        
        try:
            self.imagesTree[self.image.GetName]
        except KeyError:
            self.imagesTree[self.image.GetName] = self.image
            self.image.widget = QTreeWidgetItem(self.treeWidget, [self.image.GetName])

        self.UpdateFrame
        self.SetEnable(True)

    def RemoveImageAction(self):
        MainWindow.RemoveChild(self.imagesTree, self.image)
        
        if self.image.parent:
            self.image.parent.widget.removeChild(self.image.widget)
            self.image = self.image.parent
        else:
            self.treeWidget.invisibleRootItem().removeChild(self.image.widget)
            self.SetEnable(False)
            self.image = None
        
        self.UpdateFrame

    def SelectItemAction(self):
        imagename =  self.treeWidget.currentItem().text(0)
        if imagename == self.image.GetName:
            return

        self.image = self.imagesTree[imagename]
        self.UpdateFrame

    def SaveAction(self):
        path = QFileDialog.getExistingDirectory(self, directory='../img/', caption='Save Image')
        
        if not path:
            return
        self.image.SaveImage(path)
    
    def SaveGroupAction(self):
        path = QFileDialog.getExistingDirectory(self, directory='../img/', caption='Save Images in Group')
        
        if not path:
            return
        self.image.SaveGroupImage(path)

    def EnlargeAction(self):
        bixmap = QPixmap(f'.temp/{self.image.filename}')
        
        self.image.width += 10
        self.image.height += 10

        self.timecount = 0
        self.label.setPixmap(bixmap.scaled(self.image.width, self.image.height, Qt.KeepAspectRatio))
    
    def ShrinkAction(self):
        bixmap = QPixmap(f'.temp/{self.image.filename}')
        
        self.image.width -= 10
        self.image.height -= 10
        
        self.timecount = 0
        self.label.setPixmap(bixmap.scaled(self.image.width, self.image.height, Qt.KeepAspectRatio))

    def ExitAction(self):
        self.close()

    def SetEnable(self, boolean):
        self.actionSave.setEnabled(boolean)
        self.actionSave_Group.setEnabled(boolean)
        self.actionRemove_Image.setEnabled(boolean)
        self.actionEdges.setEnabled(boolean)
        self.actionGaussian.setEnabled(boolean)
        self.actionThreshold.setEnabled(boolean)

    @property
    def UpdateFrame(self):
        if self.image:
            self.label.setPixmap(QPixmap(f'.temp/{self.image.filename}'))      
            measure = self.image.QualityMeasures
            self.tableWidget.item(0, 0).setText(f'{measure[0]}')
            self.tableWidget.item(0, 1).setText(f'{measure[1]}')
            self.tableWidget.item(0, 2).setText(f'{measure[2]}')
            self.image.widget.setStatusTip(0, f'RMSE:{measure[0]}\t\t\tPSNR:{measure[1]}\t\t\tSNR:{measure[2]}\t')
            self.label.setStatusTip(f'RMSE:{measure[0]}\t\t\tPSNR:{measure[1]}\t\t\tSNR:{measure[2]}\t')
        else:
            self.label.setPixmap(QPixmap())
    
    @staticmethod
    def RemoveChild(imagesTree, image):
        imagesTree.pop(image.GetName)

        for item in image.child:
            MainWindow.RemoveChild(imagesTree, item)
