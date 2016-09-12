from PyQt4.QtCore import QObject
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import pyqtSignal

from aco.ant import Ant
from aco.world import World
from gui.settings import settings


class ACOLogic(QObject):
    ui_update_required = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)
        self.scale = 8
        self.world = World(self.scale)
        self.ants = []
        self.timer = QTimer()

    def reset(self):
        self.world.reset()
        self.ants = []
        self.timer = QTimer()
        self.ui_update_required.emit()

    def reset_pheromones(self):
        self.world.reset_pheromones()
        for a in self.ants:
            a.reset()

    def create_ants(self, num):
        self.ants = []
        for i in range(num):
            self.ants.append(Ant(self.world, self.world.anthill[0], self.world.anthill[1]))

    def start_simulation(self):
        self.create_ants(settings.num_ants)
        self.timer.timeout.connect(self.simulate_step)
        self.timer.start(5)

    def simulate_step(self):
        for a in self.ants:
            a.simulate_step()
        self.world.evaporation()
        self.ui_update_required.emit()

    def paint(self, painter):
        self.world.paint(painter)
        for a in self.ants:
            a.paint(painter, self.scale)
