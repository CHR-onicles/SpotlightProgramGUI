# %%
"""
### Import Statements
"""

import os,shutil,send2trash
from PIL import Image
from IPython.display import clear_output

# %%
"""
### Functions
"""

# %%
def rename_func():
    """
    Function to ask user for new name of file.
    returns y or n
    """
    while True:
        choice = input('Enter the new name for the file: ')
        yes_or_no = input('\nAre you sure?: [y/n] ')
        if yes_or_no[0].lower() == 'y':
            break
        elif yes_or_no[0].lower() == 'n':
            continue
        else:
            print('Invalid Response!')
            continue
    
    return choice

# %%
"""
<hr>
"""

# %%
def ask_to_rename_or_delete_or_skip(file):
    """
    Function to ask user whether to delete, rename,
    or skip a file.
    """
    while True:
        choice = input('Do you want to RENAME, DELETE or SKIP?: [r/d/s] ')
        if choice[0].lower() == 'r':
            return 'r'
        elif choice[0].lower() == 'd':
                send2trash.send2trash(file)
                break
        elif choice[0].lower() == 's':
            return 's'
        else:
            print('Invalid Choice!')

# %%
"""
<hr>
"""

# %%
"""
### Copying raw files from spotlight path to win folder <hr>
"""

# %%
# paths of win folder and spotlight photos files

winpath = 'B:\\Desktop\\win'
spotlight_path = ('C:\\Users\\tpand\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\')

# %%
# First clear the folder of all default-named files/pics
# (meaning User didnt actually rename it, hence it's not important)
# even if it is, file would be located in recycle bin

os.chdir(winpath)
default_files = os.listdir()

for def_file in default_files:
    if 'spotlight' not in def_file:
        send2trash.send2trash(def_file)

print('All previous files cleared!')

# %%
# changing OS directory to location of spotlight photos files

os.chdir('C:\\Users\\tpand\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets')

# %%
# giving all raw files full path names for later copy operation

files = [spotlight_path + os.listdir()[count] for count,fl in enumerate(os.listdir())] 

# %%
# Copying raw files to win folder

for f in files:
    shutil.copy(f,winpath)
    
print('Copying all raw files successful!')

# %%
"""
<hr>
"""

# %%
"""
### Looping through pictures, rename and delete on the go
"""

# %%
# change path to win folder on desktop

os.chdir(winpath)

# %%
# converting all raw files to pictures (* + .png) except those that are already pictures

# %%
win_files = []

for count,file in enumerate(os.listdir()):
    if file[-4] != '.':
        win_files.append(winpath + '\\' + os.listdir()[count])
    else:
        continue

# win_files

# %%
# changing all raw files to pictures using byte-form (using os.rename)

for count,f in enumerate(win_files):
    os.rename(f,str(count) + '.png')

print('All raw files converted to pictures!')

# %%
new_win_files = os.listdir()

# %%
# Loop through and delete unnecessary windows pictures (icons, thumbnails etc.)
# Their dimensions will not be same as desktop dimensions

# %%
# PIL to check dimensions and delete unnecessary pics since using 
# raw file size was inefficient

# change this value accordingly with your system's
DESKTOP_RESOLUTION = (1920,1080)

for f in new_win_files:
    if Image.open(f).size != (DESKTOP_RESOLUTION):
        send2trash.send2trash(f)
        
print('Unnecessary files deleted successfully')    

# %%
"""
<hr>
"""

# %%
from IPython.display import Image

# %%
# main code to display, rename, delete or skip pic

selected_new_win_files = os.listdir()

for f in selected_new_win_files:
    if f[:4] == 'spot':
        break
    display(Image(f,width=400,height=300))
    print(f)

    choice = ask_to_rename_or_delete_or_skip(f)
    if choice == 'r':
        os.rename(f,'spotlight_photos_' + rename_func() + '.png')
    elif choice == 's':
        clear_output()
        continue
    clear_output()
        
    
print('All done now!')

# %%


# %%
"""
<hr>
"""

# %%
"""
### transferring remaining pictures to wallpapers folder
"""

# %%
# Grab remaining pics(those that have been renamed by User)

ready_pics = os.listdir()

# %%
wallpapers_path = 'B:\\Desktop\\Wallpapers'

# %%
# transfer pics to new wallpaper folder

for file in ready_pics:
    shutil.move( os.getcwd() + '\\' + file, wallpapers_path)

print('Files moved successfully!')

# %%
"""
<hr>
"""