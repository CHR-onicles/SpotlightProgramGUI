from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QWindowStateChangeEvent
from PyQt5.QtCore import *

# Local Imports
import style, icons_rc
from custom_widgets import QVSeparationLine



class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Spotty'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(':/icons/cat'))

        self.setObjectName('MainWindow')
        self.setStyleSheet(style.mainWindowStyle())
        self.button_icon_size_x, self.button_icon_size_y = 30, 30


        self.UIComponents()
        self.show()


    def UIComponents(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # BUTTONS ------------------------------------------------------------------------------
        self.btn_save = QToolButton()
        self.btn_save.setIcon(QIcon(':/icons/save_icon'))
        self.btn_save.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_save.setStyleSheet(style.toolButtonStyle())
        self.btn_save.setToolTip('<b>Save</b> Image')
        self.btn_save.setEnabled(False)

        self.btn_next = QToolButton()
        self.btn_next.setIcon(QIcon(':/icons/next_icon'))
        self.btn_next.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_next.setStyleSheet(style.toolButtonStyle())
        self.btn_next.setToolTip('<b>Next</b> Image')
        self.btn_next.setEnabled(False)

        self.btn_previous = QToolButton()
        self.btn_previous.setIcon(QIcon(':/icons/back_icon'))
        self.btn_previous.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_previous.setStyleSheet(style.toolButtonStyle())
        self.btn_previous.setToolTip('<b>Previous</b> Image')
        self.btn_previous.setEnabled(False)

        self.btn_delete = QToolButton()
        self.btn_delete.setIcon(QIcon(':/icons/trash_icon'))
        self.btn_delete.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_delete.setStyleSheet(style.toolButtonStyle())
        self.btn_delete.setToolTip('<b>Delete</b> Image')
        self.btn_delete.setEnabled(False)

        self.btn_load_in = QToolButton()
        self.btn_load_in.setIcon(QIcon(':/icons/download_icon'))
        self.btn_load_in.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_load_in.setStyleSheet(style.toolButtonStyle())
        self.btn_load_in.setToolTip('<b>Retrieve</b> Spotlight Images')

        self.btn_export = QToolButton()
        self.btn_export.setIcon(QIcon(':/icons/export_icon'))
        self.btn_export.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_export.setStyleSheet(style.toolButtonStyle())
        self.btn_export.setToolTip('<b>Export</b> to specified destination')
        self.btn_export.setEnabled(False)

        self.btn_settings = QToolButton()
        self.btn_settings.setIcon(QIcon(':/icons/settings_icon'))
        self.btn_settings.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_settings.setStyleSheet(style.toolButtonStyle())
        self.btn_settings.setToolTip('<b>Settings</b>')


        # IMAGE LABEL ----------------------------------------------------------------------------
        self.lbl_image = QLabel()
        self.lbl_image.setPixmap(QPixmap(':/icons/no_image'))  # change to 1024, 576 later
        self.lbl_image.setAlignment(Qt.AlignCenter)

        # COUNTER LABEL ---------------------------------------------------------------------------
        self.lbl_counter = QLabel('')
        self.lbl_counter.setObjectName('lbl_counter')
        self.lbl_counter.setStyleSheet(style.labelStyle())
        self.lbl_counter.setAlignment(Qt.AlignBottom | Qt.AlignRight)

        # SEPARATION LINES -------------------------------------------------------------------------
        self.vline_1 = QVSeparationLine()
        self.vline_1.setObjectName('vline_1')
        self.vline_2 = QVSeparationLine()
        self.vline_2.setObjectName('vline_2')


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
        self.right_bottom_layout = QHBoxLayout()
        self.left_bottom_box = QFrame()
        self.right_bottom_box = QFrame()

        # TOP LAYOUT --------------------------------------------------------------------------------
        self.top_layout.addWidget(self.lbl_image)
        self.image_frame.setLayout(self.top_layout)

        # BOTTOM LAYOUT -----------------------------------------------------------------------------
        self.bottom_button_layout.addWidget(self.btn_settings)
        self.bottom_button_layout.addWidget(self.btn_load_in)
        self.bottom_button_layout.addWidget(self.vline_1)
        self.bottom_button_layout.addWidget(self.btn_previous)
        self.bottom_button_layout.addWidget(self.btn_save)
        self.bottom_button_layout.addWidget(self.btn_next)
        self.bottom_button_layout.addWidget(self.vline_2)
        self.bottom_button_layout.addWidget(self.btn_delete)
        self.bottom_button_layout.addWidget(self.btn_export)
        self.button_group_box.setLayout(self.bottom_button_layout)

        # BOTTOM RIGHT LAYOUT AND FRAME --------------------------------------------------------------
        self.right_bottom_layout.addWidget(self.lbl_counter)
        self.right_bottom_box.setLayout(self.right_bottom_layout)

        # CONFIGURING BOTTOM LAYOUT -------------------------------------------------------------------
        self.main_bottom_layout.addWidget(self.left_bottom_box, 40)
        self.main_bottom_layout.addWidget(self.button_group_box, 20)
        self.main_bottom_layout.addWidget(self.right_bottom_box, 40)


        self.main_layout.addWidget(self.image_frame, 90)
        self.main_layout.addLayout(self.main_bottom_layout, 10)
        self.setLayout(self.main_layout)


    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            # e = QWindowStateChangeEvent()
            # if e.oldState() & Qt.WindowMinimized:
            #     print("Window restored (to normal or maximized state)!")
            # elif e.oldState() == Qt.WindowNoState and self.windowState() == Qt.WindowMaximized:
            #     print('Window maximized')
            if self.isMaximized():
                print('Window maximized')
                # CONFIGURING BOTTOM LAYOUT MAXIMIZED WINDOW --------------------------------------------------
                self.main_bottom_layout.addWidget(self.left_bottom_box, 35)
                self.main_bottom_layout.addWidget(self.button_group_box, 30)
                self.main_bottom_layout.addWidget(self.right_bottom_box, 35)
            else:
                print('Window is restored down')
                # CONFIGURING BOTTOM LAYOUT IN RESTORED WINDOW ------------------------------------------------
                self.main_bottom_layout.addWidget(self.left_bottom_box, 40)
                self.main_bottom_layout.addWidget(self.button_group_box, 20)
                self.main_bottom_layout.addWidget(self.right_bottom_box, 40)
