import sys

from cx_Freeze import setup, Executable

from _version import __version__



# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'zip_include_packages': ['PyQt5.QtWidgets', 'PyQt5.QtGui', 'PyQt5.QtCore', 'send2trash', 'PIL'],
                 'excludes': ['PySide2', 'tkinter', 'multiprocessing', 'email', 'numpy', 'scipy', 'setuptools',
                              'distutils', 'unittest', 'packaging', 'cffi', 'html', 'http', 'pycparser'
                              ]
                 }

base = None  # todo: uncomment for testing and debugging
# base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('main.py', base=base, icon='img/cat.ico', target_name='Spotty App')
]

setup(
    name="Spotlight App",
    version=__version__,
    license='MIT',
    author='Divine Anum',
    author_email='tpandivine48@gmail.com',
    url='https://github.com/CHR-onicles/SpotlightProgramGUI',
    description='App to download and save Windows Spotlight Photos.',
    options={'build_exe': build_options},
    executables=executables)
