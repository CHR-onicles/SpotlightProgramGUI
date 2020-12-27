from getpass import getuser
import os, sys, send2trash
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt

# Local Imports
from UI_main_window import MainWindow, Label
from spotlight import Spotlight



class MainApp(MainWindow, QWidget):
    def __init__(self):
        super(MainApp, self).__init__()

        self.images = []
        self.image_index = 0
        self.app_dir = os.getcwd()

        # QApplication::setAttribute(Qt::AA_DisableWindowContextHelpButton);  # to remove ? from dialog box

        self.UI()
        self.show()

    def UI(self):
        self.app_widgets()

    def app_widgets(self):
        # BUTTONS ---------------------------------------------------------------------------
        self.btn_load_in.clicked.connect(self.retrieveSpotlightPhotos)

        self.btn_next.clicked.connect(self.nextImage)

        self.btn_previous.clicked.connect(self.previousImage)

        self.btn_delete.clicked.connect(self.deleteImage)

        self.btn_save.clicked.connect(self.saveImage)

    def retrieveSpotlightPhotos(self):
        self.image_index = 0
        self.spotlight = Spotlight()
        print(self.spotlight.selected_new_win_files)
        self.lbl_counter.setText(str(len(self.spotlight.selected_new_win_files)) + ' items')
        self.lbl_counter.setToolTip('Number of <b>selected</b> images')
        self.images = self.spotlight.selected_new_win_files
        self.lbl_image.close()
        self.lbl_image = Label()
        self.top_layout.addWidget(self.lbl_image)
        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index])))
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])

        # Enable buttons
        self.btn_delete.setEnabled(True)
        self.btn_next.setEnabled(True)
        self.btn_previous.setEnabled(True)
        self.btn_save.setEnabled(True)

    def nextImage(self):
        self.image_index += 1
        if self.image_index == len(self.images):
            self.image_index -= 1
            self.btn_next.setEnabled(False)

        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index])))
        self.btn_previous.setEnabled(True)
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])

    def previousImage(self):
        self.image_index -= 1
        if self.image_index < 0:
            self.image_index += 1
            self.btn_previous.setEnabled(False)

        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index])))
        self.btn_next.setEnabled(True)
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])

    def deleteImage(self):
        if len(self.images) == 1:
            send2trash.send2trash(self.images[self.image_index])
            self.images.remove(self.images[self.image_index])
            os.chdir(self.app_dir)
            self.lbl_image.close()
            self.lbl_image = QLabel()
            self.lbl_image.setPixmap(QPixmap('icons/no_image_2.png'))
            self.lbl_image.setAlignment(Qt.AlignCenter)
            self.top_layout.addWidget(self.lbl_image)
            self.lbl_counter.setText('')
            print(self.images)

            # Disable buttons to prevent crash
            self.btn_next.setEnabled(False)
            self.btn_previous.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.btn_delete.setEnabled(False)
            return


        if self.image_index == len(self.images)-1:
            send2trash.send2trash(self.images[self.image_index])
            self.images.remove(self.images[self.image_index])
            self.image_index -= 1
            print(self.images)

        elif self.image_index <= 0:
            send2trash.send2trash(self.images[self.image_index])
            self.images.remove(self.images[self.image_index])
            if len(self.images) == 1:
                pass
            else:
                self.image_index += 1
            print(self.images)

        else:
            send2trash.send2trash(self.images[self.image_index])
            self.images.remove(self.images[self.image_index])
            self.image_index -= 1
            print(self.images)

        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index])))
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])
        self.lbl_counter.setText(str(len(self.images)) + ' items')

    def saveImage(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())

    # TODO: 1. Add settings button
    #   2. Option for user to delete temp storage or specify his own storage.
