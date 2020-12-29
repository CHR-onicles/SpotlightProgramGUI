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
    
    QVSeparationLine#vline_1 {
    border-width: 1px;
    border-top-style: none;
    border-right-style: solid;
    border-bottom-style: none;
    border-left-style: none;
    border-color: #3d7eff;
    }
    
    QVSeparationLine#vline_2 {
    border-width: 1px;
    border-top-style: none;
    border-right-style: none;
    border-bottom-style: none;
    border-left-style: solid;
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

def DialogStyle():
    return """
    QDialog#RenameDialogWindow {
    background-color: #444;
    color: white;
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
    font: 13pt segoe UI;
    color: white;
    }
    
    QLabel#lbl_rename {
    font: 12pt segoe UI;
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
    
    QHSeparationLine {
    border-width: 1px;
    border-top-style: solid;
    border-right-style: none;
    border-bottom-style: none;
    border-left-style: none;
    border-color: #3d7eff;
    }
    """


def toolButtonStyle():
    return """
    QToolButton {
    border: #444;
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