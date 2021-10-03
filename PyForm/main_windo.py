from PyUi import Ui_MainWindow
from PyForm import EdgeParam, GaussParam, ThresholdParam

from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtWidgets import QFileDialog, QTreeWidgetItem

from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import Qt

from Utils.image import DigImage


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.image = None
        self.imagesTree = dict()
        self.timecount = 0

        self.menuFile.triggered[QAction].connect(self.MenuFile)
        self.menuFilter.triggered[QAction].connect(self.MenuFilter)
        self.treeWidget.clicked.connect(self.SelectItemAction)
        
        self.pushButton_Plus.clicked.connect(self.EnlargeAction)
        self.pushButton_Minus.clicked.connect(self.ShrinkAction)
        self.pushButton_Plus.setHidden(True)
        self.pushButton_Minus.setHidden(True)

        self.scrollArea.setWidget(self.label)
        self.treeWidget.expanded.connect(self.ExpandAction)

    def ExpandAction(self):
        self.treeWidget.resizeColumnToContents(0)

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

        if not thresh.type : return

        image = self.image.ThresholdFilter(thresh)

        self.imagesTree[image.GetName] = image
        image.widget = QTreeWidgetItem(self.image.widget, [image.GetName])
        self.image = image

        self.UpdateFrame

    def GaussAction(self):
        gauss = GaussParam()
        gauss.exec_()

        if not gauss.sigma : return

        image = self.image.GaussFilter(gauss)

        self.imagesTree[image.GetName] = image
        image.widget = QTreeWidgetItem(self.image.widget, [image.GetName])
        self.image = image

        self.UpdateFrame

    def EdgesAction(self):
        edges = EdgeParam()
        edges.exec_()

        if not edges.filter : return
        
        image = self.image.EdgesFilter(edges)
        
        self.imagesTree[image.GetName] = image
        image.widget = QTreeWidgetItem(self.image.widget, [image.GetName])
        self.image = image

        self.UpdateFrame

    def mouseMoveEvent(self, event):
        if self.image:
            if not self.timecount:
                self.pushButton_Plus.setHidden(False)
                self.pushButton_Minus.setHidden(False)
            self.timecount += 1
            self.startTimer(2000)
    
    def timerEvent(self, event):
        if not self.timecount:
            self.pushButton_Plus.setHidden(True)
            self.pushButton_Minus.setHidden(True)
            self.killTimer(event.timerId())
        elif self.timecount > 0:
            self.timecount -= 1
        
    def resizeEvent(self, event):
        self.treeWidget.setGeometry(0, 0, self.width()/4, self.height()-44)
        self.label.setGeometry(self.width()/4, 0, 3*self.width()/4, self.height()-44)
        self.scrollArea.setGeometry(self.width()/4, 0, 3*self.width()/4, self.height()-44)
        self.pushButton_Plus.setGeometry(self.width()/4 + 15, 15, 25, 25)
        self.pushButton_Minus.setGeometry(self.width()/4 + 45, 15, 25, 25)

    def MenuFile(self, triggered):
        if triggered.text() == 'Load':
            self.LoadImageAction()
        if triggered.text() == 'Remove':
            self.RemoveImageAction()
        if triggered.text() == 'Save':
            self.SaveAction()
        if triggered.text() == 'Save Group':
            self.SaveGroupAction()
        if triggered.text() == 'Exit':
            self.ExitAction()

    def LoadImageAction(self):
        path = QFileDialog.getOpenFileName(
            self, caption='Load Image', 
            filter='Image File (*.jpg  *.png)')[0]
        
        if not path : return

        self.image = DigImage(path)
        
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
        if imagename == self.image.GetName: return

        self.image = self.imagesTree[imagename]
        self.UpdateFrame

    def SaveAction(self):
        path = QFileDialog.getExistingDirectory(self,
            directory='./', caption='Save Image')
        
        if not path: return
        self.image.SaveImage(path)
    
    def SaveGroupAction(self):
        path = QFileDialog.getExistingDirectory(self,
            directory='./', caption='Save Images Group')
        
        if not path: return
        self.image.SaveGroupImage(path)

    def EnlargeAction(self):
        bixmap = QPixmap(f'.temp/{self.image.filename}')
        
        self.image.width += 10
        self.image.height += 10
        
        self.label.setPixmap(bixmap.scaled(self.image.width, self.image.height, Qt.KeepAspectRatio))
    
    def ShrinkAction(self):
        bixmap = QPixmap(f'.temp/{self.image.filename}')
        
        self.image.width -= 10
        self.image.height -= 10
        
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
        else:
            self.label.setPixmap(QPixmap())
    
    @staticmethod
    def RemoveChild(imagesTree, image):
        imagesTree.pop(image.GetName)

        for item in image.child:
            MainWindow.RemoveChild(imagesTree, item)