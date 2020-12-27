from getpass import getuser
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import QSize, Qt

# Local Imports
from UI_main_window import MainWindow
from spotlight import Spotlight



class MainApp(MainWindow, QWidget):
    def __init__(self):
        super(MainApp, self).__init__()

        self.images = []
        self.image_index = 0

        # QApplication::setAttribute(Qt::AA_DisableWindowContextHelpButton);  # to remove ? from dialog box

        self.UI()
        self.show()

    def UI(self):
        self.app_widgets()

    def app_widgets(self):
        # BUTTONS ---------------------------------------------------------------------------
        self.btn_load_in.clicked.connect(self.retrieveSpotlightPhotos)

        self.btn_next.clicked.connect(self.nextImage)

        self.btn_previous.setEnabled(False)
        self.btn_previous.clicked.connect(self.previousImage)

        self.btn_delete.setEnabled(False)
        self.btn_delete.clicked.connect(self.deleteImage)

    def retrieveSpotlightPhotos(self):
        self.image_index = 0
        self.spotlight = Spotlight()
        print(len(self.spotlight.selected_new_win_files), self.spotlight.selected_new_win_files)
        self.lbl_counter.setText(str(len(self.spotlight.selected_new_win_files)) + ' items')
        self.lbl_counter.setToolTip('Number of <b>selected</b> images')
        self.images = self.spotlight.selected_new_win_files
        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index]))
                                 .scaled(1024, 576))
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])
        self.btn_delete.setEnabled(True)

    def nextImage(self):
        self.image_index += 1
        if self.image_index == len(self.images):
            self.image_index -= 1
            self.btn_next.setEnabled(False)

        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index]))
                                 .scaled(1024, 576))
        self.btn_previous.setEnabled(True)
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])

    def previousImage(self):
        self.image_index -= 1
        if self.image_index < 0:
            self.image_index += 1
            self.btn_previous.setEnabled(False)

        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index]))
                                 .scaled(1024, 576))
        self.btn_next.setEnabled(True)
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])

    def deleteImage(self):
        self.lbl_counter.setText(str(len(self.spotlight.selected_new_win_files)-1) + ' items')
        self.images.remove(self.images[self.image_index])
        print(self.images)
        # Use send2Trash here...
        self.image_index += 1
        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index]))
                                 .scaled(1024, 576))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())

    # TODO: 1. Add settings button
    #   2. Option for user to delete temp storage or specify his own storage.
