import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Spotty')
        self.setWindowIcon(QIcon('icons/cat.ico'))
        self.setGeometry(450, 150, 1200, 800)

        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        pass

    def layouts(self):
        pass





def main():
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()

