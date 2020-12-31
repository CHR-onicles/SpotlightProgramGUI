import os, sys, send2trash
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QSettings

# Local Imports
from UI_main_window import MainWindow
from custom_widgets import Label, QHSeparationLine
from spotlight import Spotlight
import style




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
        # print(self.D_WIDTH, self.D_HEIGHT)
        self.xpos = (self.D_WIDTH / 2) - (self.DIALOG_WIDTH / 2)
        self.ypos = (self.D_HEIGHT / 2) - (self.DIALOG_HEIGHT / 2)

        # Positioning at center of screen
        self.setGeometry(int(self.xpos), int(self.ypos), self.DIALOG_WIDTH, self.DIALOG_HEIGHT)
        self.setFixedSize(self.size())

        # RENAME DIALOG SETTINGS ---------------------------------------------------------------
        self.default_prefix = ''
        self.settings = QSettings('CHR-onicles', 'SpottyApp')
        try:
            self.move(self.settings.value('rename dialog position'))
            self.default_prefix = self.settings.value('default prefix')
            print('rename dialog box default prefix:', self.default_prefix)
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
        self.btn_cancel.clicked.connect(self.closeWindow)

        # LABELS -----------------------------------------------------------------------------------------
        self.lbl_rename = QLabel('')
        self.lbl_rename.setObjectName('lbl_rename')
        # self.lbl_rename.setAlignment(Qt.AlignCenter)

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


    def closeWindow(self):
        self.close()

    def submitNewName(self):
        prefix = self.entry_prefix.text()
        name = self.entry_new_name.text()

        if name == '':
            QMessageBox.critical(self, 'Rename Failed', 'New Name has <b>NOT</b> been provided!')
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

        self.DIALOG_WIDTH, self.DIALOG_HEIGHT = 450, 400
        self.D_WIDTH, self.D_HEIGHT = main_.DESKTOP_WIDTH, main_.DESKTOP_HEIGHT
        # print(self.D_WIDTH, self.D_HEIGHT)
        self.xpos = (self.D_WIDTH / 2) - (self.DIALOG_WIDTH / 2)
        self.ypos = (self.D_HEIGHT / 2) - (self.DIALOG_HEIGHT / 2)

        # Positioning at center of screen
        self.setGeometry(int(self.xpos), int(self.ypos), self.DIALOG_WIDTH, self.DIALOG_HEIGHT)
        self.setFixedSize(self.size())
        self.setStyleSheet(style.SettingsDialogStyle())

        # SETTINGS DIALOG SETTINGS lol --------------------------------------------------------------------
        self.default_prefix_text = 'spotlight_photos_'
        self.settings = QSettings('CHR-onicles', 'SpottyApp')
        try:
            self.move(self.settings.value('settings dialog location'))
            if self.settings.value('default prefix') is None:
                pass
            else:
                self.default_prefix_text = self.settings.value('default prefix')
                # print('value at default prefix registry:', self.default_prefix_text)
        except:
            pass

        self.UI()

    def closeEvent(self, event):
        self.settings.setValue('settings dialog location', self.pos())
        if self.entry_custom_prefix.text() != '':
            QMessageBox.information(self, 'Settings saved', 'Settings have been updated!')
        else:
            self.settings.setValue('default prefix', self.default_prefix_text)

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

        self.entry_temp_dir = QLineEdit()
        self.entry_temp_dir.setReadOnly(True)
        self.entry_temp_dir.setObjectName('entry_dir')
        self.entry_target_dir = QLineEdit()
        self.entry_target_dir.setReadOnly(True)
        self.entry_target_dir.setObjectName('entry_dir')

        self.btn_temp_dir_browse = QPushButton('Browse')
        self.btn_temp_dir_browse.setObjectName('btn_browse')
        self.btn_temp_dir_browse.setToolTip('Select folder for <b>temporary</b> storage of spotlight photos')
        self.btn_temp_dir_browse.clicked.connect(self.browseTempDirectory)
        self.btn_target_dir_browse = QPushButton('Browse')
        self.btn_target_dir_browse.setObjectName('btn_browse')
        self.btn_target_dir_browse.setToolTip('Select folder to <b>move</b> favorite/all photos to')
        self.btn_target_dir_browse.clicked.connect(self.browseTargetDirectory)


        # BOTTOM LAYOUT WIDGETS ----------------------------------------------------------------------------
        self.lbl_export_options = QLabel('Export options')
        self.lbl_export_options.setObjectName('lbl_options')
        self.hline_3 = QHSeparationLine()
        self.hline_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.rbtn_fav = QRadioButton('Favorite images only')
        self.rbtn_fav.setChecked(True)
        self.rbtn_all = QRadioButton('All images')

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
        self.bottom_form_layout.addRow(self.rbtn_fav, self.rbtn_all)
        self.btn_ok_cancel_layout.addWidget(self.btn_ok)
        self.btn_ok_cancel_layout.addWidget(self.btn_cancel)
        self.btn_ok_cancel_layout.setContentsMargins(170, 0, 0, 0)
        self.bottom_form_layout.setContentsMargins(10, 0, 0, 0)
        self.bottom_layout.addLayout(self.export_options_layout)
        self.bottom_layout.addLayout(self.bottom_form_layout)

        # CONFIGURING MAIN LAYOUT ----------------------------------------------------------------------------
        self.main_layout.addLayout(self.top_layout, 30)
        self.main_layout.addLayout(self.middle_layout, 35)
        self.main_layout.addLayout(self.bottom_layout, 20)
        self.main_layout.addLayout(self.btn_ok_cancel_layout, 15)
        self.setLayout(self.main_layout)


    def showHint(self):
        if self.entry_custom_prefix.text() != '':
            # print('Typed something in custom prefix')
            self.lbl_custom_prefix_hint.setText('This prefix will be used as the default prefix for all images from now on.')
            self.lbl_custom_prefix_hint.setStyleSheet('font: 8pt segoe UI; color: #3db7ff;')
            self.top_form_layout.addRow('', self.lbl_custom_prefix_hint)
        else:
            # print('removed all text from custom prefix')
            self.lbl_custom_prefix_hint.clear()

    def submitSettings(self):
        custom_prefix = self.entry_custom_prefix.text()
        if custom_prefix != '':
            self.settings.setValue('default prefix', custom_prefix)
        self.close()

    def browseTempDirectory(self):
        self.temp_dir = QFileDialog.getExistingDirectory(self, 'Select Temporary Folder for Images')
        if self.temp_dir != '':
            print('temp dir: ', self.temp_dir)
            if len(self.temp_dir) > 26:
                new_temp_dir = self.temp_dir[0:4] + '...' + self.temp_dir[-20:]
                self.entry_temp_dir.setText(new_temp_dir)
            else:
                self.entry_temp_dir.setText(self.temp_dir)

    def browseTargetDirectory(self):
        self.target_dir = QFileDialog.getExistingDirectory(self, 'Select Target Folder for Favorite/All Images')
        if self.target_dir != '':
            print('target dir: ', self.target_dir)
            if len(self.target_dir) > 26:
                new_target_dir = self.target_dir[0:4] + '...' + self.target_dir[-20:]
                self.entry_target_dir.setText(new_target_dir)
            else:
                self.entry_target_dir.setText(self.target_dir)




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
        self.setGeometry(int(self.app_x_pos), int(self.app_y_pos), self.APP_WIDTH, self.APP_HEIGHT)
        self.setMinimumSize(600, 555)
        self.load_in_button_clicked = 0

        # Object Attributes
        self.images = []
        self.image_index = 0
        self.app_dir = os.getcwd()

        # APP SETTINGS -------------------------------------------------------------------------------
        self.setts = QSettings('CHR-onicles', 'SpottyApp')
        try:
            self.resize(self.setts.value('window size'))
            self.move(self.setts.value('window position'))

        except:
            pass

        self.UI()

    def closeEvent(self, event):
        self.setts.setValue('window size', self.size())
        self.setts.setValue('window position', self.pos())

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

        self.btn_export.clicked.connect(self.exportImages)  # add shortcut Ctrl+Shift+E / W

        self.btn_settings.clicked.connect(self.openSettings)


    def retrieveSpotlightPhotos(self):
        self.image_index = 0

        if self.load_in_button_clicked == 0 or (self.load_in_button_clicked != 0 and self.images == []):
            # First time its clicked or Clicked when user deletes all pictures
            self.spotlight = Spotlight()
            print(self.spotlight.selected_new_win_files)

            if self.spotlight.selected_new_win_files == []:
                QMessageBox.critical(self, 'Spotlight Photos', 'No New Spotlight Photos Found!')
                return
            else:
                self.lbl_counter.setText(str(len(self.spotlight.selected_new_win_files)) + ' items')
                # self.lbl_counter.setToolTip('Number of <b>selected</b> img')
                self.images = self.spotlight.selected_new_win_files
                self.lbl_image.close()
                self.lbl_image = Label()
                self.top_layout.addWidget(self.lbl_image)
                self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index])))
                self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])

                # Enable buttons
                self.btn_delete.setEnabled(True)
                self.btn_next.setEnabled(True)
                self.btn_previous.setEnabled(False)
                self.btn_save.setEnabled(True)
                self.btn_export.setEnabled(True)
                self.load_in_button_clicked += 1

        else:  # Clicked while user is still viewing pictures.
            mbox = QMessageBox.warning(self, 'Spotlight Photos', 'Previous images could be lost!',
                                       QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
            if mbox == QMessageBox.Cancel:
                pass
            else:
                self.spotlight = Spotlight()
                print(self.spotlight.selected_new_win_files)

                if self.spotlight.selected_new_win_files == []:
                    QMessageBox.critical(self, 'Spotlight Photos', 'No New Spotlight Photos Found!')
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

                    # Enable buttons
                    self.btn_delete.setEnabled(True)
                    self.btn_next.setEnabled(True)
                    self.btn_previous.setEnabled(False)
                    self.btn_save.setEnabled(True)
                    self.btn_export.setEnabled(True)
                    self.load_in_button_clicked += 1

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
            return


        if self.image_index == len(self.images)-1:
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
            elif len(self.images) == 2 and self.image_index  == 1:
                self.btn_next.setEnabled(False)
            print('remaining images:', self.images)

        self.lbl_image.setPixmap(QPixmap(os.path.join(self.spotlight.temp_storage, self.images[self.image_index])))
        self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])
        if len(self.images) > 1:
            self.lbl_counter.setText(str(len(self.images)) + ' items')
        else:
            self.lbl_counter.setText(str(len(self.images)) + ' item')

    def saveImage(self):
        self.save_dialog = RenameDialogBox()
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

        self.setWindowTitle(self.title + ' - ' + self.new_prefix+self.new_name+'.png')
        print('New Images:', self.images)

    def exportImages(self):
        print('cur directory: ', os.getcwd())
        directory = QFileDialog.getExistingDirectory(self, "Open Directory", "../", QFileDialog.ShowDirsOnly)
        print('Dir chosen:', directory)

        if directory != '':
            selected_pics = self.spotlight.moveToSpecificFolder(target_folder=directory)
            print('from main app, selected pics: ', selected_pics)
            if selected_pics is None:
                QMessageBox.critical(self, 'Export Failed', '<b>NO</b> Favorite images to Export!')
            else:
                for item in selected_pics:
                    self.images.remove(item)
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
                    self.setWindowTitle(self.title + ' - ' + self.images[self.image_index])
                    QMessageBox.information(self, 'Export Success', 'Favorite image(s) exported.')

                else:
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

    def openSettings(self):
        self.settings_dialog = SettingsDialog()
        self.settings_dialog.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    main_ = MainApp()
    sys.exit(app.exec_())



    # TODO:
    #   1 Decouple custom widgets from main app
    #   3. Open settings when 'Load in' is clicked for first time to set directories and temp storage etc
    #   4. Add more vivid description to README
    #   5. Edit the no_image icon to show the text more and reduce opacity of the circle
    #   6. Check if spotlight images is enabled
    #   7. Option to open previous pics or load new ones (Use 'more icon' and put some buttons there)
    #   8. Lookup context menus

    # TODO: FOR SETTINGS OPTIONS
    #   0. Create settings file stuff in User/AppData/Roaming/ or /Local/
    #   1. Set new prefix name (and save to file permanently)
    #   2. Set target storage (and save to file permanently) and possibly temp storage
    #   3. Option for user to delete temp storage when done
    #   4. Add option to export all, and export only selected images
