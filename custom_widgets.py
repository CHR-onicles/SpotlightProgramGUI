from PyQt5.QtGui import *
from PyQt5.QtWidgets import *




class QHSeparationLine(QFrame):
    """
      Custom Class to create a horizontal separation line.
    """
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1)
        self.setFixedHeight(1)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        return


class QVSeparationLine(QFrame):
    """
    Custom Class to create a vertical separation line.
    """
    def __init__(self):
        super().__init__()
        self.setFixedWidth(1)
        self.setMinimumHeight(1)
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        return



class Label(QWidget):
    """
    Custom Class to override QLabel and automatically resize photo with window size
    """

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.p = QPixmap()

    def setPixmap(self, p):
        self.p = p
        self.update()

    def paintEvent(self, event):
        if not self.p.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.p)
