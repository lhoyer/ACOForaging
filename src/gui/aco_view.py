from PyQt4.Qt import *

class ACOView(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.aco = None

    def set_aco(self, aco):
        self.aco = aco
        self.aco.ui_update_required.connect(self.update)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.aco.world.add_obstacle(event.x(), event.y())
            self.update()
        if event.buttons() == Qt.RightButton:
            self.aco.world.remove_obstacle(event.x(), event.y())
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.aco.paint(painter)

