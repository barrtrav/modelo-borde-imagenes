from PyForm.main_windo import MainWindow
from PyForm.present import Present
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])

    p = Present()
    p.exec()
    
    gui = MainWindow()
    gui.show()

    app.exec_()