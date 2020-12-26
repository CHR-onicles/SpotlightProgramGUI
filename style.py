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
