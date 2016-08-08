from PyQt4.QtGui import *


class ACOView(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.aco = None

    def set_aco(self, aco):
        self.aco = aco
        self.aco.ui_update_required.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.aco.paint(painter)

