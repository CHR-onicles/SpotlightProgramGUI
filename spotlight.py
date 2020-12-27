import os, shutil, send2trash
from getpass import getuser
from PIL import Image




class Spotlight:
    """
    TODO: Documentation here
    """
    def __init__(self, temp_storage='B:/Desktop/win', desktop_resolution=(1920, 1080)):
        self.spotlight_path = (
            f'C:/Users/{getuser()}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy'
            f'/LocalState/Assets')

        print('Spotlight Path:', os.path.isdir(self.spotlight_path))
        self.temp_storage = temp_storage
        print('Temp Storage: ', os.path.isdir(self.temp_storage))


        # change to temp storage and check if there are previous files
        # First clear the folder of all default-named files/pics
        # (meaning User didn't actually rename it, hence it's not important)
        # even if it is, file would be located in recycle bin
        os.chdir(self.temp_storage)
        default_files = os.listdir()

        for def_file in default_files:
            if 'spotlight' not in def_file:
                send2trash.send2trash(def_file)
        print('All previous files cleared!')


        # changing OS directory to location of spotlight photos files
        os.chdir(self.spotlight_path)

        # giving all raw files full path names for later copy operation
        files = [os.path.join(self.spotlight_path, os.listdir()[count]) for count, fl in enumerate(os.listdir())]

        # Copying raw files to win folder
        for f in files:
            shutil.copy(f, self.temp_storage)
        print('Copying all raw files successful!')


        # change path to win folder on desktop
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

        # Loop through and delete unnecessary windows pictures (images, thumbnails etc.)
        # Their dimensions will not be same as desktop dimensions

        # change this value accordingly with your system's
        self.DESKTOP_RESOLUTION = desktop_resolution

        # PIL to check dimensions and delete unnecessary pics since using
        # raw file size was inefficient
        for f in new_win_files:
            if Image.open(f).size != self.DESKTOP_RESOLUTION:
                send2trash.send2trash(f)
        print('Unnecessary files deleted successfully')


        self.selected_new_win_files = os.listdir()
        # print(self.selected_new_win_files)


    def moveToSpecificFolder(self, new_folder='B:/Desktop/Wallpapers'):
        # transferring remaining pictures to wallpapers folder
        # Grab remaining pics(those that have been renamed by User)
        ready_pics = os.listdir()

        wallpapers_path = new_folder

        # transfer pics to new wallpaper folder

        for file in ready_pics:
            shutil.move(os.getcwd() + '/' + file, wallpapers_path)

        print('Files moved successfully!')



# s = Spotlight()
