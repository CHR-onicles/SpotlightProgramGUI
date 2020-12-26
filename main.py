import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from getpass import getuser


import style


class MainApp(QApplication):
    def __init__(self, argv):
        super(MainApp, self).__init__(argv)

        # MAIN WINDOW INSTANCE -----------------------------------------------------------------------------------------
        self.main_window = MainWindow()



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spotty')
        self.setWindowIcon(QIcon('icons/cat.ico'))
        self.setGeometry(250, 150, 1400, 700)
        self.setObjectName('MainWindow')

        print(getuser())
        print(self.screen().size())
        self.setStyleSheet(style.mainWindowStyle())

        self.UIComponents()
        self.show()

    def UIComponents(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # BUTTONS ------------------------------------------------------------------------------------------------------
        #TODO: Set all buttons to disabled upon startup
        self.btn_save = QPushButton('Save')

        self.btn_next = QPushButton('Next')

        self.btn_previous = QPushButton('Previous')

        self.btn_delete = QPushButton('Delete')

        self.btn_skip = QPushButton('Skip')

        # IMAGE LABEL --------------------------------------------------------------------------------------------------
        self.lbl_image = QLabel()
        self.lbl_image.setPixmap(QPixmap('icons/no_image_2.png').scaled(QSize(400, 300)))  # change to 1280, 720 later
        self.lbl_image.setAlignment(Qt.AlignCenter)




    def layouts(self):
        print('Entered layouts')
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()

        self.button_frame = QFrame()
        self.image_frame = QFrame()

        # TOP LAYOUT ---------------------------------------------------------------------------------------------------
        self.top_layout.addWidget(self.lbl_image)
        self.image_frame.setLayout(self.top_layout)

        # BOTTOM LAYOUT -----------------------------------------------------------------------------
        self.bottom_layout.addStretch()
        self.bottom_layout.addWidget(self.btn_delete)
        self.bottom_layout.addWidget(self.btn_previous)
        self.bottom_layout.addWidget(self.btn_save)
        self.bottom_layout.addWidget(self.btn_next)
        self.bottom_layout.addWidget(self.btn_skip)
        self.bottom_layout.addStretch()
        self.button_frame.setLayout(self.bottom_layout)


        self.main_layout.addWidget(self.image_frame, 90)
        self.main_layout.addWidget(self.button_frame, 10)
        self.setLayout(self.main_layout)









if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())


