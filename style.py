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

def mainWindowStyle():
    return """
    QWidget#MainWindow {
        background-color: #444;
    }
    
    QToolTip {
        border: 1px solid white;
        padding: 5px;
        border-radius: 5px;
        color: white;
        background-color: #444
    }
    
    QVSeparationLine {
        border-width: 1px;
        border-style: solid;
        border-color: #3d7eff;
    }

    QMessageBox {
        background-color: #444;
    }
    
    QMessageBox QLabel {
        font: 11pt segoe UI;
        color: white;
    }
    
    QMessageBox QPushButton {
        border: 1px solid #3d7eff;
        border-radius: 5px;
        font: 10pt segoe UI;
        min-width: 4em;
        padding-top: 5px;
        padding-bottom: 5px;
        color: white;
    }
    
    QMessageBox QPushButton:hover {
        background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.363184 rgba(17, 103, 241, 255), stop:1 rgba(255, 255, 255, 255));
    }
    
    QMessageBox QPushButton:focus {
        border: 3px solid #3d7eff;
    } 
    """

def RenameDialogStyle():
    return """
    QDialog#RenameDialogBox {
        background-color: #444;
    }
    
    QPushButton {
        color: white;
        font: 10pt segoe UI;
        border: 2px solid #3d7eff;
        border-radius: 5px;
        padding-top:5px;
        padding-bottom:5px;
    }
    
    QPushButton:hover {
        background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.363184 rgba(17, 103, 241, 255), stop:1 rgba(255, 255, 255, 255));
    }
    
    QPushButton:pressed {
        background-color:  qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.363184 rgba(15, 8, 227, 255), stop:1 rgba(255, 255, 255, 255));
    }
    
    QPushButton:focus {
        border: 4px solid #3d7eff;
    }
    
    QPushButton#btn_submit {
        background-color: #3d7eff;
        border-color: #3db7ff;
    }
    
    QLineEdit {
        font: 11pt segoe UI;
        border: 1px solid #444;
        border-radius: 7px;
    }
    
    QLineEdit:focus {
        border: 2px solid #3d7eff;
    }
    
    QLabel {
        font: 11pt segoe UI;
        color: white;
    }
    
    QLabel#lbl_rename {
        font: 11pt segoe UI;
        color: white;
    }
    
    QMessageBox {
        background-color: #444;
    }
    
    QMessageBox QLabel {
        font: 11pt segoe UI;
        color: white;
    }
    
    QMessageBox QPushButton {
        border: 1px solid #3d7eff;
        font: 10pt segoe UI;
        min-width: 4em;
    }
    
    QMessageBox QPushButton:focus {
        border: 3px solid #3d7eff;
    }
    
    QToolTip {
        border: 1px solid white;
        padding: 5px;
        border-radius: 5px;
        color: white;
        background-color: #444
    }
    
    QGroupBox {
    font: 9pt segoe UI;
    margin-top: 8px;
    border: 1px solid #3d7eff;
    border-right: none;
    border-left: none;
    border-bottom: none; 
    }
    
    QGroupBox::title {
    color: #3db7ff;
    top: -10px;
    }
    """

def SettingsDialogStyle():
    return """
    QDialog#SettingsDialogBox {
        background-color: #444;
    }
    
    QPushButton {
        color: white;
        font: 10pt segoe UI;
        border: 2px solid #3d7eff;
        border-radius: 5px;
        padding-top:5px;
        padding-bottom:5px;
    }
    
    QPushButton#btn_browse {
        color: white;
        font: 10pt segoe UI;
        border: 2px solid #3d7eff;
        border-radius: 5px;
        padding-top:3px;
        padding-bottom:3px;
        min-width: 4em;
    }
    
    QPushButton:hover {
        background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.363184 rgba(17, 103, 241, 255), stop:1 rgba(255, 255, 255, 255));
    }
    
    QPushButton:pressed {
        background-color:  qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.363184 rgba(15, 8, 227, 255), stop:1 rgba(255, 255, 255, 255));
    }
    
    QPushButton:focus {
        border: 4px solid #3d7eff;
    }
    
    QPushButton#btn_ok {
        background-color: #3d7eff;
        border-color: #3db7ff;
    }
    
    QHSeparationLine {
        border-width: 1px;
        border-style: solid;
        border-color: #3d7eff;
    }
    
    QLineEdit {
        font: 10pt segoe UI;
        border: 1px solid #444;
        border-radius: 7px;
        padding-top: 2px;
        padding-bottom: 2px;
    }
    
    QLineEdit#entry_dir {
        font: 9pt segoe UI;
        padding-top: 2px;
        padding-bottom: 2px;
    }
    
    QLineEdit:focus {
        border: 2px solid #3d7eff;
    }
    
    QLabel {
        font: 11pt segoe UI;
        color: white;
    }
    
    QRadioButton {
        font: 10pt segoei UI;
        color: white;    
    }
    
    QToolTip {
        border: 1px solid white;
        padding: 5px;
        border-radius: 5px;
        color: white;
        background-color: #444
    }
    
    QMessageBox {
        background-color: #444;
    }
    
    QMessageBox QLabel {
        font: 11pt segoe UI;
        color: white;
    }
    
    QMessageBox QPushButton {
        border: 1px solid #3d7eff;
        font: 10pt segoe UI;
        min-width: 4em;
    }
    
    QMessageBox QPushButton:focus {
        border: 3px solid #3d7eff;
    }
    
    QGroupBox {
    font: 9pt segoe UI;
    margin: 8px;
    border: 1px solid #3d7eff;
    border-right: none;
    border-left: none;
    border-bottom: none;
    }
    
    QGroupBox:title {
    color: #3d7eff;
    top: -12px;
    }
    """


def toolButtonStyle():
    return """
    QToolButton {
        border: #444; /* Not visible tho*/
    }
    
    QToolButton:hover {
        border: 3px solid #444;
        padding: 2px;
        margin: -2px;
    }
    
    QToolButton:pressed {
        border: #444;
    }
    """

def buttonGroupBoxStyle():
    return """
    QGroupBox#button_group_box {
        border: 1px solid white;
        border-radius: 10px;
    }
    """

def labelStyle():
    return """
    QLabel#lbl_counter {
        font: 13pt segoe UI;
        color: white;
    }
    """