from PyQt4.QtCore import QObject
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import pyqtSignal

from aco.ant import Ant
from aco.world import World


class ACOLogic(QObject):
    ui_update_required = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)
        self.world = World()
        self.ants = None
        self.create_ants(200)
        self.timer = QTimer()

    def create_ants(self, num):
        self.ants = []
        for i in range(num):
            self.ants.append(Ant(self.world, self.world.anthill[0], self.world.anthill[1]))

    def start_simulation(self):
        self.timer.timeout.connect(self.simulate_step)
        self.timer.start(20)

    def simulate_step(self):
        for a in self.ants:
            a.simulate_step()
        self.world.evaporation()
        self.ui_update_required.emit()

    def paint(self, painter):
        self.world.paint(painter)
        for a in self.ants:
            a.paint(painter)
