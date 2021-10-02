from PyUi import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtWidgets import QFileDialog, QTreeWidgetItem

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

from Utils.image import DigImage


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.image = None
        self.imagesTree = dict()

        self.menuFile.triggered[QAction].connect(self.MenuFile)

        self.treeWidget.clicked.connect(self.SelectItemAction)
        
        self.pushButton_Plus.clicked.connect(self.EnlargeAction)
        self.pushButton_Minus.clicked.connect(self.ShrinkAction)

    def MenuFile(self, triggered):
        if triggered.text() == 'Load Image':
            self.LoadImageAction()
        if triggered.text() == 'Remove Image':
            self.RemoveImageAction()
        if triggered.text() == 'Save':
            self.SaveAction()
        if triggered.text() == 'Save Group':
            self.SaveGroupAction()

    def LoadImageAction(self):
        path = QFileDialog.getOpenFileName(
            self, caption='Load Image', 
            filter='Image File (*.jpg  *.png)')[0]
        
        if not path : return

        self.image = DigImage(path)
        self.imagesTree[self.image.GetName] = self.image
        self.image.widget = QTreeWidgetItem(self.treeWidget, [self.image.GetName])

        self.UpdateFrame

    def RemoveImageAction(self):
        self.label.setPixmap(QPixmap())
        self.imagesTree.pop(self.image.GetName)
        self.treeWidget.invisibleRootItem().removeChild(self.image.widget)

    def SelectItemAction(self):
        imagename =  self.treeWidget.currentItem().text(0)
        if imagename == self.image.GetName: return

        self.image = self.imagesTree[imagename]
        self.UpdateFrame

    def SaveAction(self):
        path = QFileDialog.getSaveFileName(self, 
            directory=f'./{self.image.filename}', 
            filter='Image File (*.jpg, *.png)',
            caption='Save Image')[0]
        
        if not path: return
        self.image.SaveImage(path)
    
    def SaveGroupAction(self):
        path = QFileDialog.getExistingDirectory(self, 
            caption='Save Images Group')
        
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

    @property
    def UpdateFrame(self):
        self.label.setPixmap(QPixmap(f'.temp/{self.image.filename}'))