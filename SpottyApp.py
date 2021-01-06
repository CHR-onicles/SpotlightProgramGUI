# ------------------------------------------------------------------------------
#
# AUTHOR: CHR-onicles (GitHub)
# PROJECT MADE WITH: PyQt5
# Version: 0.1.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ------------------------------------------------------------------------------

import os, sys, send2trash, platform
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QFormLayout, QMessageBox, QRadioButton, QFileDialog, QSizePolicy, QDesktopWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QSettings, QPropertyAnimation, QSize, QEasingCurve, QTimer
from time import time

# Local Imports
from UI_main_window import MainWindow
from custom_widgets import Label, QHSeparationLine
from spotlight import Spotlight
import style

print('System: ', platform.system(), platform.release())

# PyInstaller function to help create exe file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

resource_path('UI_main_window.py')
resource_path('custom_widgets.py')
resource_path('spotlight.py')
resource_path('style.py')
resource_path('icons_rc.py')




class RenameDialogBox(QDialog):
    """
    class for Renaming Dialog Box.
    """
    signal_new_name = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rename')
        self.setObjectName('RenameDialogBox')
        self.setWindowIcon(QIcon(':/icons/cat'))
        self.setStyleSheet(style.RenameDialogStyle())
        self.setModal(True)  # deactivates other windows till this window is interacted with

        self.DIALOG_WIDTH, self.DIALOG_HEIGHT = 400, 200
        self.D_WIDTH, self.D_HEIGHT = main_.DESKTOP_WIDTH, main_.DESKTOP_HEIGHT
        self.xpos = (self.D_WIDTH / 2) - (self.DIALOG_WIDTH / 2)
        self.ypos = (self.D_HEIGHT / 2) - (self.DIALOG_HEIGHT / 2)

        # Positioning at center of screen
        self.setGeometry(int(self.xpos), int(self.ypos), self.DIALOG_WIDTH, self.DIALOG_HEIGHT)
        self.setFixedSize(self.size())

        # RENAME DIALOG SETTINGS ---------------------------------------------------------------
        # self.default_prefix = ''
        self.settings = QSettings('CHR-onicles', 'SpottyApp')
        self.default_prefix = self.settings.value('default prefix')
        try:
            self.move(self.settings.value('rename dialog position'))
        except:
            pass

        self.UI()

    def closeEvent(self, event):
        self.settings.setValue('rename dialog position', self.pos())

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # BUTTONS ----------------------------------------------------------------------------------------
        self.btn_submit = QPushButton('Submit')
        self.btn_submit.clicked.connect(self.submitNewName)
        self.btn_submit.setObjectName('btn_submit')
        self.btn_cancel = QPushButton('Cancel')
        self.btn_cancel.clicked.connect(self.close)

        # LABELS -----------------------------------------------------------------------------------------
        self.lbl_rename = QLabel('')
        self.lbl_rename.setObjectName('lbl_rename')

        self.lbl_prefix_options = QLabel('Name options')
        self.lbl_prefix_options.setStyleSheet('font: 9pt segoe UI; color: #3db7ff;')

        # ENTRIES ---------------------------------------------------------------------------------------
        self.entry_prefix = QLineEdit(self.default_prefix)
        self.entry_prefix.setToolTip('<b>Default</b> prefix for all photos')
        self.entry_new_name = QLineEdit(self)
        self.entry_new_name.setToolTip('<b>Short</b> description about photo')
        self.entry_new_name.setFocus()

        # SEPARATION LINE ------------------------------------------------------------------------------
        self.hline = QHSeparationLine()
        self.hline.setObjectName('hline')
        self.hline.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # SIGNALS --------------------------------------------------------------------------------------
        main_.signal_photo_name.connect(self.getPhotoName)

    def layouts(self):
        # DEFINING LAYOUTS ------------------------------------------------------------------------------
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_main_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.button_layout = QHBoxLayout()

        self.section_layout = QHBoxLayout()
        self.section_layout.addWidget(self.lbl_prefix_options)
        self.section_layout.addWidget(self.hline)

        # Adding Widgets to Top Layout -----------------------------------------------------------------
        self.top_layout.addWidget(self.lbl_rename)

        # Adding Buttons to Button Layout --------------------------------------------------------------
        self.button_layout.addWidget(self.btn_submit)
        self.button_layout.addWidget(self.btn_cancel)

        # Adding Widgets to Bottom Layout ---------------------------------------------------------------
        self.bottom_layout.setContentsMargins(10, 0, 0, 0)
        self.bottom_layout.addRow(QLabel('Prefix:'), self.entry_prefix)
        self.bottom_layout.addRow(QLabel('New Name:'), self.entry_new_name)
        self.bottom_layout.addRow('', self.button_layout)

        self.bottom_main_layout.setContentsMargins(0, 7, 0, 0)
        self.bottom_main_layout.addLayout(self.section_layout, 2)
        self.bottom_main_layout.addLayout(self.bottom_layout, 98)

        # Adding Layouts and Widgets to Main Layout ----------------------------------------------------
        self.main_layout.addLayout(self.top_layout, 10)
        self.main_layout.addLayout(self.bottom_main_layout, 90)
        self.setLayout(self.main_layout)


    @pyqtSlot(str)
    def getPhotoName(self, pic):
        # print('pic', pic)
        self.photoname = pic
        if len(self.photoname) > 21:
            new_photoname = self.photoname[0:4] + '...' + self.photoname[-15:]
            self.lbl_rename.setText(f'Renaming photo \'<i>{new_photoname}</i>\' to: ')
        else:
            self.lbl_rename.setText(f'Renaming photo \'<i>{self.photoname}</i>\' to: ')

    def submitNewName(self):
        prefix = self.entry_prefix.text()
        name = self.entry_new_name.text()
        if name in ['', ' ']:
            QMessageBox.critical(self, 'Rename Failed', 'Name provided is invalid!')
        elif (prefix + name + '.png') in main_.images:
            QMessageBox.critical(self, 'Rename Failed', 'Name provided already exists!')
        else:
            self.signal_new_name.emit(prefix, name)
            QMessageBox.information(self, 'Rename success', 'Image renamed successfully.')
            self.close()




class SettingsDialog(QDialog):
    """
    Class for Settings Dialog Box.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Settings')
        self.setObjectName('SettingsDialogBox')
        self.setWindowIcon(QIcon(':/icons/cat'))
        self.setStyleSheet(style.SettingsDialogStyle())
        self.setModal(True)  # deactivates other windows till this window is interacted with

        self.DIALOG_WIDTH, self.DIALOG_HEIGHT = 450, 100
        self.resize(self.DIALOG_WIDTH, self.DIALOG_HEIGHT)
        self.setStyleSheet(style.SettingsDialogStyle())

        # SETTINGS DIALOG SETTINGS lol --------------------------------------------------------------------
        self.default_prefix_text = 'sp_'
        self.temp_dir = ''
        self.target_dir = ''
        self.rbtn_fav_state = False
        self.rbtn_all_state = False
        self.rbtn_one_state = False

        self.settings = QSettings('CHR-onicles', 'SpottyApp')
        try:
            self.move(self.settings.value('settings dialog location'))
            if self.settings.value('default prefix') is None:
                pass
            else:
                self.default_prefix_text = self.settings.value('default prefix')
            self.temp_dir = str(self.settings.value('temporary directory'))
            self.target_dir = str(self.settings.value('target directory'))
            self.rbtn_fav_state = self.toBool(self.settings.value('fav button checked'))
            self.rbtn_all_state = self.toBool(self.settings.value('all button checked'))
            self.rbtn_one_state = self.toBool(self.settings.value('one button checked'))
        except:
            pass

        #  DIALOG ANIMATION SETTINGS ----------------------------------------------------------------------
        self.openingAnimation(self.DIALOG_WIDTH, self.DIALOG_HEIGHT + 300)

        self.UI()

    def closeEvent(self, event):
        self.settings.setValue('settings dialog location', self.pos())

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # TOP LAYOUT WIDGETS ------------------------------------------------------------------------------
        self.lbl_prefix_options = QLabel('Prefix options')
        self.lbl_prefix_options.setObjectName('lbl_options')
        self.hline_1 = QHSeparationLine()
        self.hline_1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.lbl_default_prefix = QLabel('Default Prefix')
        self.lbl_custom_prefix = QLabel('Custom Prefix')

        self.entry_default_prefix = QLineEdit(self.default_prefix_text)
        self.entry_default_prefix.setReadOnly(True)
        self.entry_default_prefix.setToolTip('<b>Current</b> default prefix for images')
        self.entry_custom_prefix = QLineEdit(self)
        self.entry_custom_prefix.setFocus()
        self.entry_custom_prefix.textEdited.connect(self.showHint)

        self.lbl_custom_prefix_hint = QLabel('')  # change to all time later
        self.lbl_custom_prefix_hint.setWordWrap(True)

        # MIDDLE LAYOUT WIDGETS ----------------------------------------------------------------------------
        self.lbl_dir_options = QLabel('Folder options')
        self.lbl_dir_options.setObjectName('lbl_options')
        self.hline_2 = QHSeparationLine()
        self.hline_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.lbl_temp_dir = QLabel('Temp. Folder')
        self.lbl_target_dir = QLabel('Target Folder')

        self.entry_temp_dir = QLineEdit(self.temp_dir)
        self.entry_temp_dir.setReadOnly(True)
        self.entry_temp_dir.setObjectName('entry_dir')
        self.entry_temp_dir.setToolTip('Folder path to keep retrieved Spotlight Photos for processing')
        self.entry_target_dir = QLineEdit(self.target_dir)
        self.entry_target_dir.setReadOnly(True)
        self.entry_target_dir.setObjectName('entry_dir')
        self.entry_target_dir.setToolTip('Folder path to <b>export</b> images to')

        self.btn_temp_dir_browse = QPushButton('Browse')
        self.btn_temp_dir_browse.setObjectName('btn_browse')
        self.btn_temp_dir_browse.setToolTip('Select folder for <b>temporary</b> storage of spotlight photos')
        self.btn_temp_dir_browse.clicked.connect(self.browseTempDirectory)
        self.btn_target_dir_browse = QPushButton('Browse')
        self.btn_target_dir_browse.setObjectName('btn_browse')
        self.btn_target_dir_browse.setToolTip('Select folder to <b>export</b> images to')
        self.btn_target_dir_browse.clicked.connect(self.browseTargetDirectory)

        # BOTTOM LAYOUT WIDGETS ----------------------------------------------------------------------------
        self.lbl_export_options = QLabel('Export options')
        self.lbl_export_options.setObjectName('lbl_options')
        self.hline_3 = QHSeparationLine()
        self.hline_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.rbtn_fav = QRadioButton('Favorite images only')
        self.rbtn_fav.setChecked(self.rbtn_fav_state)
        self.rbtn_all = QRadioButton('All images')
        self.rbtn_all.setChecked(self.rbtn_all_state)
        self.rbtn_one = QRadioButton('One at a time')
        self.rbtn_one.setChecked(self.rbtn_one_state)

        self.btn_ok = QPushButton('OK')
        self.btn_ok.setObjectName('btn_ok')
        self.btn_ok.clicked.connect(self.submitSettings)
        self.btn_cancel = QPushButton('Cancel')
        self.btn_cancel.clicked.connect(self.close)

    def layouts(self):
        # DEFINING LAYOUTS ---------------------------------------------------------------------------------
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.middle_layout = QVBoxLayout()
        self.bottom_layout = QVBoxLayout()

        self.prefix_options_layout = QHBoxLayout()
        self.dir_options_layout = QHBoxLayout()
        self.export_options_layout = QHBoxLayout()

        self.top_form_layout = QFormLayout()
        self.middle_form_layout = QFormLayout()
        self.bottom_rbtn_layout = QHBoxLayout()
        self.bottom_form_layout = QFormLayout()
        self.btn_ok_cancel_layout = QHBoxLayout()

        self.temp_dir_row_layout = QHBoxLayout()
        self.target_dir_row_layout = QHBoxLayout()

        # TOP LAYOUT --------------------------------------------------------------------------------------
        self.prefix_options_layout.addWidget(self.lbl_prefix_options)
        self.prefix_options_layout.addWidget(self.hline_1)
        self.top_form_layout.addRow(self.lbl_default_prefix, self.entry_default_prefix)
        self.top_form_layout.addRow(self.lbl_custom_prefix, self.entry_custom_prefix)
        self.top_form_layout.setContentsMargins(10, 0, 0, 0)
        self.top_layout.addLayout(self.prefix_options_layout)
        self.top_layout.addLayout(self.top_form_layout)

        # MIDDLE LAYOUT -----------------------------------------------------------------------------------
        self.dir_options_layout.addWidget(self.lbl_dir_options)
        self.dir_options_layout.addWidget(self.hline_2)
        self.temp_dir_row_layout.addWidget(self.entry_temp_dir)
        self.temp_dir_row_layout.addWidget(self.btn_temp_dir_browse)
        self.target_dir_row_layout.addWidget(self.entry_target_dir)
        self.target_dir_row_layout.addWidget(self.btn_target_dir_browse)
        self.middle_form_layout.addRow(self.lbl_temp_dir, self.temp_dir_row_layout)
        self.middle_form_layout.addRow(self.lbl_target_dir, self.target_dir_row_layout)
        self.middle_form_layout.setContentsMargins(10, 0, 0, 0)
        self.middle_layout.addLayout(self.dir_options_layout)
        self.middle_layout.addLayout(self.middle_form_layout)

        # BOTTOM LAYOUT -----------------------------------------------------------------------------------
        self.export_options_layout.addWidget(self.lbl_export_options)
        self.export_options_layout.addWidget(self.hline_3)
        self.bottom_rbtn_layout.addWidget(self.rbtn_fav)
        self.bottom_rbtn_layout.addWidget(self.rbtn_one)
        self.bottom_form_layout.addRow(self.rbtn_all, self.bottom_rbtn_layout)
        self.btn_ok_cancel_layout.addWidget(self.btn_ok)
        self.btn_ok_cancel_layout.addWidget(self.btn_cancel)
        self.btn_ok_cancel_layout.setContentsMargins(170, 0, 0, 0)
        self.bottom_form_layout.setContentsMargins(10, 0, 0, 0)
        self.bottom_layout.addLayout(self.export_options_layout)
        self.bottom_layout.addLayout(self.bottom_form_layout)

        # CONFIGURING MAIN LAYOUT ----------------------------------------------------------------------------
        self.main_layout.addLayout(self.top_layout, 35)
        self.main_layout.addLayout(self.middle_layout, 30)
        self.main_layout.addLayout(self.bottom_layout, 20)
        self.main_layout.addLayout(self.btn_ok_cancel_layout, 15)
        self.setLayout(self.main_layout)


    def showHint(self):
        if self.entry_custom_prefix.text() != '':
            # print('Typed something in custom prefix')
            self.lbl_custom_prefix_hint.setText(
                'This prefix will be used as the default prefix for all images from now on.')
            self.lbl_custom_prefix_hint.setStyleSheet('font: 8pt segoe UI; color: #3db7ff;')
            self.top_form_layout.addRow('', self.lbl_custom_prefix_hint)
        else:
            self.lbl_custom_prefix_hint.clear()

    def submitSettings(self):
        if self.entry_temp_dir.text() and self.entry_target_dir.text() != '':
            if self.entry_custom_prefix.text() == '':
                self.custom_prefix = self.entry_default_prefix.text()
                print('set custom prefix to default entry', self.entry_default_prefix.text())
            else:
                self.custom_prefix = self.entry_custom_prefix.text()
                print('set custom prefix to custom entry')
            self.temp_dir = self.entry_temp_dir.text()
            self.target_dir = self.entry_target_dir.text()
            self.settings.setValue('default prefix', self.custom_prefix)
            self.settings.setValue('temporary directory', self.temp_dir)
            self.settings.setValue('target directory', self.target_dir)
            self.settings.setValue('fav button checked', self.rbtn_fav.isChecked())
            self.settings.setValue('all button checked', self.rbtn_all.isChecked())
            self.settings.setValue('one button checked', self.rbtn_one.isChecked())
            QMessageBox.information(self, 'Settings saved', 'Settings have been updated!')
            self.close()
        else:
            QMessageBox.warning(self, 'Settings Warning', 'Please fill <b>all</b> required fields!')

    def browseTempDirectory(self):
        self.temp_dir = QFileDialog.getExistingDirectory(self, 'Select Temporary Folder for Images')
        if self.temp_dir != '' and self.temp_dir == self.target_dir:
            QMessageBox.critical(self, 'Invalid Folder Error',
                                 'You <b>cannot</b> use the same folder as the <b>Target Folder<b>!')
            return
        if self.temp_dir != '':
            print('temp dir: ', self.temp_dir)
            # if len(self.temp_dir) > 26:
            #     new_temp_dir = self.temp_dir[0:4] + '...' + self.temp_dir[-20:]
            #     self.entry_temp_dir.setText(new_temp_dir)
            # else:  # need to introduce new var to prevent this from affecting the real path used for processing
            self.entry_temp_dir.setText(self.temp_dir)

    def browseTargetDirectory(self):
        self.target_dir = QFileDialog.getExistingDirectory(self, 'Select Target Folder for Favorite/All Images')
        if self.target_dir != '' and self.target_dir == self.temp_dir:
            QMessageBox.critical(self, 'Invalid Folder Error',
                                 'You <b>cannot</b> use the same folder as the <b>Temporary Folder<b>!')
            return
        if self.target_dir != '':
            print('target dir: ', self.target_dir)
            self.entry_target_dir.setText(self.target_dir)

    def openingAnimation(self, width, height):
        self.open_animation = QPropertyAnimation(self, b'size')
        self.open_animation.setDuration(1000)
        self.open_animation.setEndValue(QSize(width, height))
        self.open_animation.setEasingCurve(QEasingCurve.Linear)
        self.open_animation.start()
        self.setMaximumSize(self.DIALOG_WIDTH, self.DIALOG_HEIGHT + 300)


    # CLASS HELPER FUNCTIONS ----------------------------------------------------------------------------
    def toBool(self, text):
        return text.lower() in ['true', 'True', 1]




class MainApp(MainWindow, QWidget):
    """
    class for main app which makes use of main window UI
    """

    signal_photo_name = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        if (platform.system() != 'Windows') or (platform.release() != '10'):
            mbox = QMessageBox(QMessageBox.Critical, 'App Error', 'Your platform does not support Windows Spotlight!')
            mbox.setWindowIcon(QIcon(':/icons/cat'))
            mbox.setInformativeText('Windows Spotlight Photos is only supported on Windows 10.')
            mbox.exec_()
            sys.exit()

        # Positioning window at center of screen
        d = QDesktopWidget().screenGeometry()
        self.DESKTOP_WIDTH, self.DESKTOP_HEIGHT = d.width(), d.height()
        self.APP_WIDTH, self.APP_HEIGHT = 1200, 800
        self.app_x_pos = (self.DESKTOP_WIDTH / 2) - (self.APP_WIDTH / 2)
        self.app_y_pos = (self.DESKTOP_HEIGHT / 2) - (self.APP_HEIGHT / 2)
        self.setGeometry(int(self.app_x_pos), int(self.app_y_pos), self.APP_WIDTH, self.APP_HEIGHT)
        self.setMinimumSize(600, 555)
        self.load_in_button_clicked = 0

        # Object Attributes
        self.images = []
        self.image_index = 0
        # self.app_dir = os.getcwd()

        # APP SETTINGS -------------------------------------------------------------------------------
        self.setts = QSettings('CHR-onicles', 'SpottyApp')
        print('App data already exists:', self.setts.contains('default prefix'))

        try:
            self.resize(self.setts.value('window size'))
            self.move(self.setts.value('window position'))
        except:
            pass

        if self.setts.contains('default prefix') is False:
            self.timer = QTimer()
            self.timer.singleShot(500, self.openSettings)

        self.UI()


    def closeEvent(self, event):
        self.setts.setValue('window size', self.size())
        self.setts.setValue('window position', self.pos())

    def UI(self):
        self.app_widgets()

    def app_widgets(self):
        # BUTTONS ---------------------------------------------------------------------------
        self.btn_load_in.clicked.connect(self.retrieveSpotlightPhotos)
        self.btn_load_in.setShortcut('Ctrl+D')

        self.btn_next.clicked.connect(self.nextImage)
        self.btn_next.setShortcut('Right')

        self.btn_previous.clicked.connect(self.previousImage)
        self.btn_previous.setShortcut('Left')

        self.btn_delete.clicked.connect(self.deleteImage)
        self.btn_delete.setShortcut('Del')

        self.btn_save.clicked.connect(self.saveImage)
        self.btn_save.setShortcut('Return')

        self.btn_export.clicked.connect(self.exportImages)
        self.btn_export.setShortcut('Ctrl+E')

        self.btn_settings.clicked.connect(self.openSettings)


    def retrieveSpotlightPhotos(self):
        self.image_index = 0
        prefix = self.setts.value('default prefix')
        temp_dir = self.setts.value('temporary directory')
        target_dir = self.setts.value('target directory')
        if ((temp_dir is None or target_dir is None) or (
                temp_dir in ['none', 'None'] or target_dir in ['none', 'None'])):
            QMessageBox.critical(self, 'Directory Error', 'Folder(s) NOT chosen in <b>Settings</b>')
        else:
            if self.load_in_button_clicked == 0 or (self.load_in_button_clicked != 0 and self.images == []):
                # First time its clicked or Clicked when user deletes all pictures
                self.t1 = time()
                print(self.t1)
                self.spotlight = Spotlight(prefix=prefix, temp_storage=temp_dir)

                print(self.spotlight.selected_new_win_files)

                self.setupFirstPicAfterRetrieval()

            else:  # Clicked while user is still viewing pictures.
                mbox = QMessageBox.warning(self, 'Spotlight Photos', 'Previous images could be lost!',  # todo: change message here to something about having duplicate images
                                           QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
                if mbox == QMessageBox.Cancel:
                    pass
                else:
                    self.t1 = time()
                    print('Time started: ', self.t1)
                    self.spotlight = Spotlight(prefix=prefix, temp_storage=temp_dir)
                    print(self.spotlight.selected_new_win_files)

                    self.setupFirstPicAfterRetrieval()

            if self.setts.value('default prefix') in self.images[self.image_index]:
                self.setFavIconVisible()
            else:
                self.lbl_fav_icon.clear()

    def nextImage(self):
        if self.image_index == (len(self.images) - 1):
            self.image_index -= 1
            self.btn_next.setEnabled(False)

        self.image_index += 1
        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index])))
        self.btn_previous.setEnabled(True)
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])

        if self.image_index == (len(self.images) - 1):
            self.btn_next.setEnabled(False)

        if self.setts.value('default prefix') in self.images[self.image_index]:
            self.setFavIconVisible()
        else:
            self.lbl_fav_icon.clear()

    def previousImage(self):
        # Check before executing button function
        if self.image_index == 0:
            self.image_index += 1
            self.btn_previous.setEnabled(False)

        self.image_index -= 1
        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index])))
        self.btn_next.setEnabled(True)
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])

        # Check after executing button function
        if self.image_index == 0:
            self.btn_previous.setEnabled(False)

        if self.setts.value('default prefix') in self.images[self.image_index]:
            self.setFavIconVisible()
        else:
            self.lbl_fav_icon.clear()

    def deleteImage(self):
        if len(self.images) == 1:  # Deleting the last image
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
            self.btn_export.setEnabled(False)
            self.lbl_fav_icon.clear()
            return

        if self.image_index == len(self.images) - 1:
            if len(self.images) == 2:
                self.btn_next.setEnabled(False)  # Don't know whether this works or not
            print('deleting last image in list')
            send2trash.send2trash(self.images[self.image_index])
            self.images.remove(self.images[self.image_index])
            self.image_index -= 1
            self.btn_next.setEnabled(False)
            if len(self.images) == 1:
                self.btn_previous.setEnabled(False)
            print('remaining images:', self.images)

        elif self.image_index <= 0:
            print('deleting first image in list')
            send2trash.send2trash(self.images[self.image_index])
            self.images.remove(self.images[self.image_index])
            if len(self.images) == 1:
                self.btn_previous.setEnabled(False)
                self.btn_next.setEnabled(False)
            else:
                self.image_index += 1
            print('remaining images', self.images)

        else:
            print('deleting image in the middle of list')
            send2trash.send2trash(self.images[self.image_index])
            self.images.remove(self.images[self.image_index])
            self.image_index -= 1
            if self.image_index == 0:
                self.btn_previous.setEnabled(False)
            elif len(self.images) == 2 and self.image_index == 1:
                self.btn_next.setEnabled(False)
            print('remaining images:', self.images)

        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index])))
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])
        if self.setts.value('default prefix') in self.images[self.image_index]:
            self.setFavIconVisible()
        else:
            self.lbl_fav_icon.clear()
        if len(self.images) > 1:
            self.lbl_counter.setText(str(len(self.images)) + ' items')
        else:
            self.lbl_counter.setText(str(len(self.images)) + ' item')

    def saveImage(self):
        self.save_dialog = RenameDialogBox()
        self.signal_photo_name.emit(self.images[self.image_index])
        self.save_dialog.show()
        self.save_dialog.signal_new_name.connect(self.getNewName)

    @pyqtSlot(str, str)
    def getNewName(self, prefix, name):
        self.new_prefix = prefix
        self.new_name = name
        print('\nOld name: ' + self.images[self.image_index])
        print(self.new_prefix + self.new_name)

        old_file = self.images[self.image_index]
        os.rename(old_file, self.new_prefix + self.new_name + '.png')
        self.images.remove(old_file)
        self.images = os.listdir()
        # print(self.images.index('.png'))  # Doesn't work...have no idea why
        for count, item in enumerate(self.images):
            if self.new_name in item:
                print('Renamed image at:', count)
                break
        self.image_index = count
        print('index: ', self.image_index)
        if self.image_index == len(self.images) - 1:
            print('last image')
            if len(self.images) == 1:
                self.btn_next.setEnabled(False)
                self.btn_previous.setEnabled(False)
            else:
                self.btn_next.setEnabled(False)
                self.btn_previous.setEnabled(True)

        elif self.image_index == 0:
            print('first image')
            self.btn_previous.setEnabled(False)
            self.btn_next.setEnabled(True)

        self.setWindowTitle(self.title + ' - ' + self.new_prefix + self.new_name + '.png')
        if self.setts.value('default prefix') in self.images[self.image_index]:
            self.setFavIconVisible()
        else:
            self.lbl_fav_icon.clear()
        print('New Images:', self.images)

    def exportImages(self):
        print('cur directory: ', os.getcwd())
        print('Dir chosen:', self.setts.value('target directory'))

        if self.setts.value('fav button checked') == 'true':
            print('fav button checked:', self.setts.value('fav button checked'))
            selected_pics = self.spotlight.moveFavoritesToSpecificFolder(prefix=self.setts.value('default prefix'),
                                                                         target_folder=self.setts.value('target directory'))
            print('from main app, selected pics:', selected_pics)
            if selected_pics is None:
                QMessageBox.critical(self, 'Export Failed', '<b>NO</b> Favorite images to Export!')

            elif selected_pics[0] == 'FileExistsError':
                QMessageBox.critical(self, 'Image already exists', f'Image with the name \'<i>{selected_pics[1]}</i>\''
                                                                   f' already exists at <b>target folder</b>!')

                self.conditionsForWhatToDoAfterExport(extra_condition='FileExistsError')

            else:
                for item in selected_pics:
                    self.images.remove(item)
                self.conditionsForWhatToDoAfterExport()

        elif self.setts.value('all button checked') == 'true':
            print('all button checked:', self.setts.value('all button checked'))
            all_pics = self.spotlight.moveAllToSpecificFolder(target_folder=self.setts.value('target directory'))

            print('from main app, all pics:', all_pics)
            if all_pics[0] == 'FileExistsError':
                QMessageBox.critical(self, 'Image already exists', f'Image with the name \'<i>{all_pics[1]}</i>\''
                                                                   f' already exists at <b>target folder</b>!')
                return
            else:
                self.images.clear()
                self.conditionsForWhatToDoAfterExport()

        elif self.setts.value('one button checked') == 'true':
            print('one button checked:', self.setts.value('one button checked'))
            single_pic = self.spotlight.moveOneToSpecificFolder(single_pic=self.images[self.image_index],
                                                                target_folder=self.setts.value('target directory'))

            print('from main app, single pic:', single_pic)
            if single_pic[0] == 'FileExistsError':
                QMessageBox.critical(self, 'Image already exists', f'Image with the name \'<i>{single_pic[1]}</i>\''
                                                                   f' already exists at <b>target folder</b>!')
                return
            else:
                self.images.remove(single_pic)
                self.conditionsForWhatToDoAfterExport()

        else:
            QMessageBox.critical(self, 'Export Choice', 'No <b>Export Option</b> was selected in Settings!')
            # TODO: Add informative text here to: 'go to settings'

    def openSettings(self):
        self.settings_dialog = SettingsDialog()
        self.settings_dialog.show()


    # CLASS HELPER FUNCTIONS (to reduce repetition) ------------------------------------------------------
    def conditionsForWhatToDoAfterExport(self, extra_condition=None):
        self.images = os.listdir()
        print(self.images, len(self.images))
        self.image_index = 0
        if len(self.images) != 0:
            self.lbl_image.setPixmap(QPixmap(self.images[self.image_index]))
            if len(self.images) == 1:
                self.lbl_counter.setText(str(len(self.images)) + ' item')
                self.btn_next.setEnabled(False)
                self.btn_previous.setEnabled(False)
            elif len(self.images) > 1:
                self.lbl_counter.setText(str(len(self.images)) + ' items')
                self.btn_previous.setEnabled(False)
                self.btn_next.setEnabled(True)
            if extra_condition is None:
                QMessageBox.information(self, 'Export Success', 'Image(s) exported successfully.')
                self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])
            else:
                self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])
            if self.setts.value('default prefix') in self.images[self.image_index]:
                self.setFavIconVisible()
            else:
                self.lbl_fav_icon.clear()

        else:
            self.lbl_fav_icon.clear()
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
            self.btn_export.setEnabled(False)
            QMessageBox.information(self, 'Export Success', 'Image(s) exported successfully.')

    def setFavIconVisible(self):
        self.lbl_fav_icon.setPixmap(QPixmap(':/icons/save_icon').scaledToHeight(self.fav_icon_size_y, Qt.SmoothTransformation))
        self.left_bottom_layout.addWidget(self.lbl_fav_icon)

    def setupFirstPicAfterRetrieval(self):
        if self.spotlight.selected_new_win_files == []:
            QMessageBox.critical(self, 'Spotlight Photos', 'No New Spotlight Photos Found!')
            self.t2 = time()
            print('Stopped abruptly - Time elapsed :', self.t2 - self.t1)
            with open('log.txt', 'a') as f:
                f.write('Stopped abruptly - Time elapsed :' + str(self.t2 - self.t1))
            return
        else:
            self.lbl_counter.setText(str(len(self.spotlight.selected_new_win_files)) + ' items')
            # self.lbl_counter.setToolTip('Number of <b>selected</b> img')
            self.images = self.spotlight.selected_new_win_files
            self.lbl_image.close()
            self.lbl_image = Label()
            self.top_layout.addWidget(self.lbl_image)
            self.lbl_image.setPixmap(
                QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index])))
            self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])

            # Enable buttons except previous button since we'll be at first image
            self.btn_delete.setEnabled(True)
            self.btn_next.setEnabled(True)
            self.btn_previous.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.btn_export.setEnabled(True)
            self.load_in_button_clicked += 1

            self.t2 = time()
            print('Time elapsed :', self.t2 - self.t1)
            print(os.getcwd())
            with open('log.txt', 'a') as f:
                f.write('Time elapsed :' + str(self.t2 - self.t1))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    main_ = MainApp()
    sys.exit(app.exec_())



    #   TODO: A[High Priority]:
    #       - Option to favorite without necessarily renaming
    #       - Add checkbox to allow user to remove prefix and deactivate it in the rename dialog box
    #       - Option to open previous pics or load new ones (Use 'more icon' and put some buttons there)
    #       - Lookup context menus [for the 'More' icon]

    #   TODO: [Moderate Priority]:
    #       - Check if spotlight images is enabled
    #       - Refactor repeating code into helper functions across board
    #       - Informative text with Messagebox for 'No fav image selected', and possibly all messageboxes
    #
    #   TODO: [Optional]:
    #       - Edit the no_image icon to show the text more and reduce opacity of the circle
    #       - Animating loading in of pictures with a round progress bar kinda style


    # TODO: FOR SETTINGS OPTIONS
    #   1. Option for user to delete temp storage when done [optional]
