from getpass import getuser
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import QSize, Qt

from UI_main_window import MainWindow



class MainApp(MainWindow, QWidget):
    def __init__(self):
        super(MainApp, self).__init__()

        print(getuser())

        self.UI()

    def UI(self):
        self.widgets()

    def app_widgets(self):
        # BUTTONS ---------------------------------------------------------------------------
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_app = MainApp()
    sys.exit(app.exec_())
