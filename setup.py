from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'zip_include_packages': ['PyQt5.QtWidgets', 'PyQt5.QtGui', 'PyQt5.QtCore', 'send2trash', 'PIL'],
                 'excludes': ['PySide2', 'tkinter', 'multiprocessing', 'email', 'numpy', 'scipy', 'setuptools',
                              'distutils', 'unittest', 'packaging', 'cffi', 'html', 'http', 'pycparser'
                              ]
                 }

import sys
base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('SpottyApp.py', base=base, icon='img/cat.ico', target_name='Spotty App')
]


setup(
      name="Spotlight App",
      version='0.1.0',
      description='App to download and save Windows Spotlight Photos.',
      options={'build_exe': build_options},
      executables=executables)
