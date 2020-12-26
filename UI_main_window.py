from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import QSize, Qt

# Local Imports
import style


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spotty')
        self.setWindowIcon(QIcon('icons/cat.ico'))
        self.setGeometry(250, 150, 1200, 800)
        self.setObjectName('MainWindow')
        self.setStyleSheet(style.mainWindowStyle())

        print(self.screen().size())

        self.UIComponents()


    def UIComponents(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # BUTTONS ------------------------------------------------------------------------------------------------------
        #TODO: Set all buttons to disabled upon startup
        self.btn_save = QToolButton()
        self.btn_save.setIcon(QIcon('icons/wheart.png'))
        self.btn_save.setIconSize(QSize(50, 50))
        self.btn_save.setStyleSheet(style.toolButtonStyle())
        self.btn_save.setToolTip('<b>Save</b> Image')
        # self.btn_save.setEnabled(False)

        self.btn_next = QToolButton()
        self.btn_next.setIcon(QIcon('icons/wnext.png'))
        self.btn_next.setIconSize(QSize(50, 50))
        self.btn_next.setStyleSheet(style.toolButtonStyle())
        self.btn_next.setToolTip('<b>Next</b> Image')
        # self.btn_next.setEnabled(False)

        self.btn_previous = QToolButton()
        self.btn_previous.setIcon(QIcon('icons/wback.png'))
        self.btn_previous.setIconSize(QSize(50, 50))
        self.btn_previous.setStyleSheet(style.toolButtonStyle())
        self.btn_previous.setToolTip('<b>Previous</b> Image')
        # self.btn_previous.setEnabled(False)

        self.btn_delete = QToolButton()
        self.btn_delete.setIcon(QIcon('icons/wgarbage.png'))
        self.btn_delete.setIconSize(QSize(50,50))
        self.btn_delete.setStyleSheet(style.toolButtonStyle())
        self.btn_delete.setToolTip('<b>Delete</b> Image')
        # self.btn_delete.setEnabled(False)

        self.btn_load_in = QToolButton()
        self.btn_load_in.setIcon(QIcon('icons/wdownload.png'))
        self.btn_load_in.setIconSize(QSize(50, 50))
        self.btn_load_in.setStyleSheet(style.toolButtonStyle())
        self.btn_load_in.setToolTip('<b>Retrieve</b> Spotlight Images')

        # IMAGE LABEL --------------------------------------------------------------------------------------------------
        self.lbl_image = QLabel()
        self.lbl_image.setPixmap(QPixmap('icons/2.jpg').scaled(1024, 576))  # change to 1280, 720 later
        self.lbl_image.setAlignment(Qt.AlignCenter)


    def layouts(self):
        # DEFINING LAYOUTS -------------------------------------------------------------------------
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_button_layout = QHBoxLayout()
        self.main_bottom_layout = QHBoxLayout()

        self.button_group_box = QGroupBox()
        self.button_group_box.setObjectName('button_group_box')
        self.button_group_box.setStyleSheet(style.buttonGroupBoxStyle())
        self.image_frame = QFrame()
        self.left_bottom_box = QFrame()
        self.right_bottom_box = QFrame()

        # TOP LAYOUT --------------------------------------------------------------------------------
        self.top_layout.addWidget(self.lbl_image)
        self.image_frame.setLayout(self.top_layout)

        # BOTTOM LAYOUT -----------------------------------------------------------------------------
        self.bottom_button_layout.addWidget(self.btn_load_in)
        self.bottom_button_layout.addWidget(self.btn_previous)
        self.bottom_button_layout.addWidget(self.btn_save)
        self.bottom_button_layout.addWidget(self.btn_next)
        self.bottom_button_layout.addWidget(self.btn_delete)
        self.button_group_box.setLayout(self.bottom_button_layout)

        # CONFIGURING MAIN LAYOUT -------------------------------------------------------------------
        self.main_bottom_layout.addWidget(self.left_bottom_box, 35)
        self.main_bottom_layout.addWidget(self.button_group_box, 30)
        self.main_bottom_layout.addWidget(self.right_bottom_box, 35)

        self.main_layout.addWidget(self.image_frame, 90)
        self.main_layout.addLayout(self.main_bottom_layout, 10)
        self.setLayout(self.main_layout)
