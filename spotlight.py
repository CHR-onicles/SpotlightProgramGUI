# ------------------------------------------------------------------------------
#
# AUTHOR: CHR-onicles (GitHub)
# PROJECT MADE WITH: PyQt5
# Version: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ------------------------------------------------------------------------------

import os, shutil, send2trash
from getpass import getuser
from PIL import Image
from random import choices
import string




class Spotlight:
    """
    Class for handling retrieval and filtering of spotlight photos for further processing.
    """
    def __init__(self, prefix=None, temp_storage=None):
        self.spotlight_path = (
            f'C:/Users/{getuser()}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy'
            f'/LocalState/Assets')

        print('Spotlight Path valid:', os.path.isdir(self.spotlight_path))
        self.temp_storage = temp_storage
        print('Temp Storage valid: ', os.path.isdir(self.temp_storage))


        # Change to temp storage and check if there are previous files
        # First clear the folder of all default-named files/pics
        # (meaning User didn't actually rename it, hence it's not important)
        # even if it is, file would be located in recycle bin
        os.chdir(self.temp_storage)
        default_files = os.listdir()

        for def_file in default_files:
            if prefix not in def_file:
                send2trash.send2trash(def_file)
        print('All previous files cleared!')
        # TODO: Remove this at release, and prefix and prefix arg in class call
        #   also implement option to see previous images (with 'more' button and context menu)


        # changing OS directory to location of spotlight photos files
        os.chdir(self.spotlight_path)

        # giving all raw files full path names for later copy operation
        files = [os.path.join(self.spotlight_path, os.listdir()[count]) for count, fl in enumerate(os.listdir())]

        # Copying raw files to temporary folder
        for f in files:
            shutil.copy(f, self.temp_storage)
        print('Copying all raw files successful!')


        # change path to temporary folder
        os.chdir(self.temp_storage)

        # converting all raw files to pictures (* + .png) except those that are already pictures
        win_files = []

        for count, file in enumerate(os.listdir()):
            if file[-4] != '.':
                win_files.append(os.path.join(self.temp_storage, os.listdir()[count]))
            else:
                continue


        # changing all raw files to pictures using byte-form (using os.rename)
        for count, f in enumerate(win_files):
            os.rename(f, str(count) + '.png')
        print('All raw files converted to pictures!')


        # Get new filenames
        new_win_files = os.listdir()

        # Loop through and delete unnecessary windows pictures (img, thumbnails etc.)
        # All spotlight_photos on all desktops are 1920x1080
        self.IMAGE_RESOLUTION = (1920, 1080)

        # PIL to check dimensions and delete unnecessary pics since using
        # raw file size was inefficient
        for f in new_win_files:
            if Image.open(f).size != self.IMAGE_RESOLUTION:
                send2trash.send2trash(f)
        print('Unnecessary files deleted successfully')

        # Giving selected pics random non-repeating(hopefully) names
        self.selected_new_win_files = os.listdir()

        for pics in self.selected_new_win_files:
            if prefix not in pics:
                os.rename(pics, ''.join(choices(string.ascii_letters + string.digits, k=7)) + '.png')
            else:
                continue

        self.selected_new_win_files = os.listdir()
        print('from Spotlight class, selected images: ', self.selected_new_win_files)


    def moveFavoritesToSpecificFolder(self, prefix=None, target_folder=None):
        pics = os.listdir()
        print('listing target dir: ', os.listdir(target_folder))
        fav_pics = []
        print('Target folder valid: ', os.path.isdir(target_folder))

        # Selecting pics with prefix in them (favorited pics)
        for pic in pics:
            if prefix in pic:
                fav_pics.append(pic)
            else:
                continue

        if fav_pics == []:
            print('No image selected')
            return
        else:
            wallpapers_path = target_folder

            # Transfer selected pics to new wallpaper folder
            for file in fav_pics:
                try:
                    shutil.move(os.path.join(os.getcwd(), file), wallpapers_path)
                except:
                    print('File Exits Already')
                    return ['FileExistsError', file]

            print('Favorite Files moved successfully! \n')
            return fav_pics

    def moveAllToSpecificFolder(self, target_folder=None):
        pics = os.listdir()
        print('listing target dir: ', os.listdir(target_folder))
        print('Target folder valid: ', os.path.isdir(target_folder))

        wallpapers_path = target_folder

        # Transfer all pics to new wallpaper folder
        for file in pics:
            try:
                shutil.move(os.path.join(os.getcwd(), file), wallpapers_path)
            except:
                print('File Exits Already')
                return ['FileExistsError', file]

        print('All Files moved successfully! \n')
        return pics

    def moveOneToSpecificFolder(self, single_pic=None, target_folder=None):
        pic = single_pic
        print('listing target dir: ', os.listdir(target_folder))
        print('Target folder valid: ', os.path.isdir(target_folder))

        wallpapers_path = target_folder

        # Transfer selected pic to new wallpaper folder
        try:
            shutil.move(os.path.join(os.getcwd(), pic), wallpapers_path)
        except:
            print('File Exits Already')
            return ['FileExistsError', pic]

        print('All Files moved successfully! \n')
        return pic
