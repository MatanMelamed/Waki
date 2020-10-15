from PyQt5 import QtWidgets

from View.main_window import Ui_MainWindow
import sys


class ViewManager:

    def __init__(self):
        self.ui = Ui_MainWindow()
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui.setupUi(self.main_window)

    def run_ui(self):
        self.main_window.show()
        sys.exit(self.app.exec_())

    def r(self):
        self.main_window.hide()
    
