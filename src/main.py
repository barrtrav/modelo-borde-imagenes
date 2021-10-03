from PyForm.main_windo import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])

    gui = MainWindow()
    gui.show()

    app.exec_()