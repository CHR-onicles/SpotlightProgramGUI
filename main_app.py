# from getpass import getuser
import os, sys, send2trash
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot

# Local Imports
from UI_main_window import MainWindow
from custom_widgets import Label, QHSeparationLine
from spotlight import Spotlight
import style




class RenameDialogWindow(QDialog):
    """
    class for Renaming Dialog Box
    """

    signal_new_name = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rename')
        self.setObjectName('RenameDialogWindow')
        self.setWindowIcon(QIcon(':/icons/cat'))
        self.setStyleSheet(style.DialogStyle())
        self.setModal(True)  # deactivates other windows till this window is interacted with

        self.DIALOG_WIDTH, self.DIALOG_HEIGHT = 400, 200
        self.D_WIDTH, self.D_HEIGHT = main_.DESKTOP_WIDTH, main_.DESKTOP_HEIGHT
        # print(self.D_WIDTH, self.D_HEIGHT)

        self.xpos = (self.D_WIDTH / 2) - (self.DIALOG_WIDTH / 2)
        self.ypos = (self.D_HEIGHT / 2) - (self.DIALOG_HEIGHT / 2)

        # Positioning at center of screen
        self.setGeometry(int(self.xpos), int(self.ypos), self.DIALOG_WIDTH, self.DIALOG_HEIGHT)
        self.setFixedSize(self.size())

        self.default_prefix = 'spotlight_photos_'

        self.UI()


    def UI(self):
        self.widgets()
        self.layouts()


    def widgets(self):
        # BUTTONS ----------------------------------------------------------------------------------------
        self.btn_submit = QPushButton('Submit')
        self.btn_submit.clicked.connect(self.submitNewName)
        self.btn_submit.setObjectName('btn_submit')
        self.btn_cancel = QPushButton('Cancel')
        self.btn_cancel.clicked.connect(self.closeWindow)

        # LABELS -----------------------------------------------------------------------------------------
        self.lbl_rename = QLabel('')
        self.lbl_rename.setObjectName('lbl_rename')
        # self.lbl_rename.setAlignment(Qt.AlignCenter)
        main_.signal_photo_name.connect(self.getPhotoName)

        # ENTRIES ---------------------------------------------------------------------------------------
        self.entry_prefix = QLineEdit(self.default_prefix)
        self.entry_prefix.setToolTip('<b>Default</b> prefix for all photos')
        self.entry_new_name = QLineEdit(self)
        self.entry_new_name.setToolTip('<b>Short</b> description about photo')
        self.entry_new_name.setFocus()

        # SEPARATION LINE ------------------------------------------------------------------------------
        self.hline = QHSeparationLine()
        self.hline.setObjectName('hline')

    def layouts(self):
        # DEFINING LAYOUTS ------------------------------------------------------------------------------
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QFormLayout()
        self.button_layout = QHBoxLayout()

        # Adding Widgets to Top Layout -----------------------------------------------------------------
        self.top_layout.addWidget(self.lbl_rename)

        # Adding Buttons to Button Layout --------------------------------------------------------------
        self.button_layout.addWidget(self.btn_submit)
        self.button_layout.addWidget(self.btn_cancel)

        # Adding Widgets to Bottom Layout ---------------------------------------------------------------
        self.bottom_layout.addRow(QLabel('Prefix:'), self.entry_prefix)
        self.bottom_layout.addRow(QLabel('New Name:'), self.entry_new_name)
        self.bottom_layout.addRow('', self.button_layout)

        # Adding Layouts and Widgets to Main Layout ----------------------------------------------------
        self.main_layout.addLayout(self.top_layout, 10)
        self.main_layout.addWidget(self.hline)
        self.main_layout.addLayout(self.bottom_layout, 90)
        self.setLayout(self.main_layout)

    @pyqtSlot(str)
    def getPhotoName(self, pic):
        self.photoname = pic
        if len(self.photoname) > 21:
            self.photoname = self.photoname[0:4] + '...' + self.photoname[-15:]
        self.lbl_rename.setText(f'Renaming photo <i>\'{self.photoname}\'</i> to: ')

    def closeWindow(self):
        self.close()

    def submitNewName(self):
        prefix = self.entry_prefix.text()
        name = self.entry_new_name.text()

        if name == '':
            QMessageBox.critical(self, 'Rename Failed', 'New Name has <b>NOT</b> been provided!')

        else:
            self.signal_new_name.emit(prefix, name)
            self.close()




class MainApp(MainWindow, QWidget):
    """
    class for main app which makes use of main window UI
    """

    signal_photo_name = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # Positioning window at center of screen
        d = QDesktopWidget().screenGeometry()
        self.DESKTOP_WIDTH, self.DESKTOP_HEIGHT = d.width(), d.height()
        self.APP_WIDTH, self.APP_HEIGHT = 1200, 800
        self.app_x_pos = (self.DESKTOP_WIDTH / 2) - (self.APP_WIDTH / 2)
        self.app_y_pos = (self.DESKTOP_HEIGHT / 2) - (self.APP_HEIGHT / 2)
        # print(self.DESKTOP_HEIGHT, self.DESKTOP_WIDTH)
        self.setGeometry(int(self.app_x_pos), int(self.app_y_pos), self.APP_WIDTH, self.APP_HEIGHT)
        self.setMinimumSize(600, 555)

        # Object Attributes
        self.images = []
        self.image_index = 0
        self.app_dir = os.getcwd()


        self.UI()


    def UI(self):
        self.app_widgets()


    def app_widgets(self):
        # BUTTONS ---------------------------------------------------------------------------
        self.btn_load_in.clicked.connect(self.retrieveSpotlightPhotos)  # add shortcut Ctrl+D

        self.btn_next.clicked.connect(self.nextImage)
        self.btn_next.setShortcut('Right')

        self.btn_previous.clicked.connect(self.previousImage)
        self.btn_previous.setShortcut('Left')

        self.btn_delete.clicked.connect(self.deleteImage)
        self.btn_delete.setShortcut('Del')

        self.btn_save.clicked.connect(self.saveImage)
        self.btn_save.setShortcut('Return')



    def retrieveSpotlightPhotos(self):
        self.image_index = 0
        self.spotlight = Spotlight(desktop_resolution=(self.DESKTOP_WIDTH, self.DESKTOP_HEIGHT))
        print(self.spotlight.selected_new_win_files)
        self.lbl_counter.setText(str(len(self.spotlight.selected_new_win_files)) + ' items')
        self.lbl_counter.setToolTip('Number of <b>selected</b> img')
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
            print(self.images)
            self.lbl_image.close()
            self.lbl_image = QLabel()
            self.lbl_image.setPixmap(QPixmap(':/icons/no_image'))
            self.lbl_image.setAlignment(Qt.AlignCenter)
            self.top_layout.addWidget(self.lbl_image)
            self.lbl_counter.setText('')
            self.setWindowTitle(self.title)

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
        self.save_dialog = RenameDialogWindow()
        # self.signal_coords.emit(self.pos().x(), self.pos().y())
        self.signal_photo_name.emit(self.images[self.image_index])
        # TODO: Implement later (Rename dialog to appear at the middle of app screen relatively not using signals.)
        self.save_dialog.show()
        self.save_dialog.signal_new_name.connect(self.getNewName)

    @pyqtSlot(str, str)
    def getNewName(self, prefix, name):
        self.new_prefix = prefix
        self.new_name = name
        print('\nOld name: ' + self.images[self.image_index])
        print(self.new_prefix + self.new_name)

        old_file = self.images[self.image_index]
        os.rename(old_file, self.new_prefix+self.new_name+'.png')
        self.images.remove(old_file)
        self.images = os.listdir()
        # print(self.images.index('.png'))  # Doesn't work...have no idea why
        for count, item in enumerate(self.images):
            if self.new_name in item:
                print('Renamed image at:', count)
                break
        self.image_index = count
        self.setWindowTitle(self.title + ' - ' + self.new_prefix+self.new_name+'.png')
        print('New Images:', self.images)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    main_ = MainApp()
    sys.exit(app.exec_())



    # TODO: 1. Add settings button to configure destination or temp folder and prefix.
    #   2. Option for user to delete temp storage or specify his own storage.
    #   3 Decouple custom widgets from main app.
    #   4. Export renamed photos to specific folder on desktop.
    #      (moves renamed pics to specified dir, and updates the list and image index).
    #   5. Another dialog when 'Load in' is clicked to set directories and temp storage etc.
    #   6. Add more vivid description to README.
