import os, shutil, send2trash
from getpass import getuser
from PIL import Image




class Spotlight:
    """
    Class for handling retrieval and filtering of spotlight photos for further processing.
    """
    def __init__(self, prefix='', temp_storage=''):  # C:/Users/ADMIN/Desktop/win
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


        self.selected_new_win_files = os.listdir()
        print('from Spotlight, selected images: ', self.selected_new_win_files)


    def moveToSpecificFolder(self, prefix='', target_folder=''):
        # Transferring remaining pictures to target folder
        pics = os.listdir()
        fav_pics = []
        print('Target folder valid: ', os.path.isdir(target_folder))

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

            # transfer pics to new wallpaper folder
            for file in fav_pics:
                try:
                    shutil.move(os.path.join(os.getcwd(), file), wallpapers_path)
                except:
                    print('File Exits Already')
                    return ['FileExistsError', file]

            print('Files moved successfully! \n')
            return fav_pics
        # TODO: Connect this to main window, add prefix to class call for this function in case user changes it.


# s = Spotlight()
