from PyQt5.QtWidgets import QWidget, QToolButton, QHBoxLayout, QVBoxLayout, QFrame, QLabel, QGroupBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt, QEvent

# Local Imports
import style, icons_rc
from custom_widgets import QVSeparationLine



class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'SpottyApp'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(':/icons/cat'))

        self.setObjectName('MainWindow')
        self.setStyleSheet(style.mainWindowStyle())
        self.button_icon_size_x, self.button_icon_size_y = 30, 30
        self.fav_icon_size_x, self.fav_icon_size_y = 30, 30

        self.UIComponents()
        self.show()


    def UIComponents(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # BUTTONS ------------------------------------------------------------------------------
        self.btn_save = QToolButton()
        save_icon = QIcon()
        save_icon.addPixmap(QPixmap(':/icons/save_icon'), QIcon.Normal)
        save_icon.addPixmap(QPixmap(':/icons/save_icon_disabled'), QIcon.Disabled)
        self.btn_save.setIcon(QIcon(save_icon))
        self.btn_save.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_save.setStyleSheet(style.toolButtonStyle())
        self.btn_save.setToolTip('Add to <b>favorites</b> (Enter)')
        self.btn_save.setEnabled(False)

        self.btn_next = QToolButton()
        next_icon = QIcon()
        next_icon.addPixmap(QPixmap(':/icons/next_icon'), QIcon.Normal)
        next_icon.addPixmap(QPixmap(':/icons/next_icon_disabled'), QIcon.Disabled)
        self.btn_next.setIcon(QIcon(next_icon))
        self.btn_next.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_next.setStyleSheet(style.toolButtonStyle())
        self.btn_next.setToolTip('<b>Next</b> Image')
        self.btn_next.setEnabled(False)

        self.btn_previous = QToolButton()
        back_icon = QIcon()
        back_icon.addPixmap(QPixmap(':/icons/back_icon'), QIcon.Normal)
        back_icon.addPixmap(QPixmap(':/icons/back_icon_disabled'), QIcon.Disabled)
        self.btn_previous.setIcon(QIcon(back_icon))
        self.btn_previous.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_previous.setStyleSheet(style.toolButtonStyle())
        self.btn_previous.setToolTip('<b>Previous</b> Image')
        self.btn_previous.setEnabled(False)

        self.btn_delete = QToolButton()
        delete_icon = QIcon()
        delete_icon.addPixmap(QPixmap(':/icons/trash_icon'), QIcon.Normal)
        delete_icon.addPixmap(QPixmap(':/icons/trash_icon_disabled'), QIcon.Disabled)
        self.btn_delete.setIcon(QIcon(delete_icon))
        self.btn_delete.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_delete.setStyleSheet(style.toolButtonStyle())
        self.btn_delete.setToolTip('<b>Delete</b> Image (Del)')
        self.btn_delete.setEnabled(False)

        self.btn_load_in = QToolButton()
        load_in_icon = QIcon()
        load_in_icon.addPixmap(QPixmap(':/icons/download_icon'), QIcon.Normal)
        # load_in_icon.addPixmap(QPixmap(':/icons/download_icon_disabled'), QIcon.Disabled)  # Don't need this now
        self.btn_load_in.setIcon(QIcon(load_in_icon))
        self.btn_load_in.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_load_in.setStyleSheet(style.toolButtonStyle())
        self.btn_load_in.setToolTip('<b>Retrieve</b> Spotlight Images')

        self.btn_export = QToolButton()
        export_icon = QIcon()
        export_icon.addPixmap(QPixmap(':/icons/export_icon'), QIcon.Normal)
        export_icon.addPixmap(QPixmap(':/icons/export_icon_disabled'), QIcon.Disabled)
        self.btn_export.setIcon(export_icon)
        self.btn_export.setIconSize(QSize(self.button_icon_size_x, self.button_icon_size_y))
        self.btn_export.setStyleSheet(style.toolButtonStyle())
        self.btn_export.setToolTip('<b>Export</b> images to specified destination')
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

        # FAVORITED ICON LABEL --------------------------------------------------------------------
        self.lbl_fav_icon = QLabel()  # todo: change to flat button for smoother edges when scaled
        self.lbl_fav_icon.setPixmap(QPixmap(':/icons/save_icon').scaled(self.fav_icon_size_x, self.fav_icon_size_y))
        self.lbl_fav_icon.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

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
        self.left_bottom_layout = QHBoxLayout()
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

        # BOTTOM LEFT LAYOUT AND FRAME ---------------------------------------------------------------
        self.left_bottom_box.setLayout(self.left_bottom_layout)

        # BOTTOM RIGHT LAYOUT AND FRAME --------------------------------------------------------------
        self.right_bottom_layout.addWidget(self.lbl_counter)
        self.right_bottom_box.setLayout(self.right_bottom_layout)

        # CONFIGURING BOTTOM LAYOUT -------------------------------------------------------------------
        self.main_bottom_layout.addWidget(self.left_bottom_box, 30)
        self.main_bottom_layout.addWidget(self.button_group_box, 40)
        self.main_bottom_layout.addWidget(self.right_bottom_box, 30)


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
                self.main_bottom_layout.addWidget(self.left_bottom_box, 30)
                self.main_bottom_layout.addWidget(self.button_group_box, 40)
                self.main_bottom_layout.addWidget(self.right_bottom_box, 30)
