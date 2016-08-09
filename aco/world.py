from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.settings import settings


class World:

    def __init__(self):
        self.anthill = (200, 200)
        self.food = [(100, 300), (400, 300), (330, 170)]
        self.height = 500
        self.width = 600
        self.obstacles = QImage(self.width, self.height, QImage.Format_RGB32)
        self.obstacles.invertPixels()
        self.pheromones = [[0 for y in range(self.height)] for x in range(self.width)]
        self.max_pheromones = 0.1
        for x in range(len(self.pheromones)):
            for y in range(len(self.pheromones[x])):
                self.pheromones[x][y] = 0.01
        self.step_size = 5

    def is_food_source(self, position):
        for f in self.food:
            if f == position:
                return True
        return False

    def get_transitions(self, actual_position):
        transitions = []
        x = actual_position[0]
        y = actual_position[1]
        if x+self.step_size < self.width and not self.is_obstacle(x+self.step_size, y):
            transitions.append((x+self.step_size, y))
        if y+self.step_size < self.height and not self.is_obstacle(x, y+self.step_size):
            transitions.append((x, y+self.step_size))
        if x-self.step_size >= 0 and not self.is_obstacle(x-self.step_size, y):
            transitions.append((x-self.step_size, y))
        if y-self.step_size >= 0 and not self.is_obstacle(x, y-self.step_size):
            transitions.append((x, y-self.step_size))
        return transitions

    """def get_decision_map(self, start):
        transitions = self.get_transitions(start)
        num = {}
        decision_map = {}
        denom = 0
        for t in transitions:
            tau = self.pheromones[t[0]][t[1]]
            num[t] = tau ** self.alpha
            denom += num[t]
        for t in transitions:
            decision_map[t] = num[t] / denom
        return decision_map

    def get_probability(self, start, end):
        decision_map = self.get_decision_map(start)
        num = decision_map[end]
        denom = 0
        for d in decision_map:
            denom += decision_map[d]
        return num / denom"""

    def get_probability(self, start, end):
        num = self.pheromones[end[0]][end[1]] ** settings.alpha
        denom = 0
        transitions = self.get_transitions(start)
        for t in transitions:
            denom += self.pheromones[t[0]][t[1]] ** settings.alpha
        return num / denom

    def release_pheromones(self, position, concentration):
        self.pheromones[position[0]][position[1]] += concentration
        if self.pheromones[position[0]][position[1]] > self.max_pheromones:
            self.max_pheromones = self.pheromones[position[0]][position[1]]

    def evaporation(self):
        for x in range(0, len(self.pheromones), self.step_size):
            for y in range(0, len(self.pheromones[x]), self.step_size):
                self.pheromones[x][y] *= 1 - settings.rho
                if self.pheromones[x][y] <= 0.01:
                    self.pheromones[x][y] = 0.01
        self.max_pheromones *= 1 - settings.rho

    def add_obstacle(self, x, y):
        painter = QPainter(self.obstacles)
        pen = QPen(QColor(Qt.blue), 5)
        painter.setPen(pen)
        painter.drawPoint(x, y)
        painter.end()

    def remove_obstacle(self, x, y):
        painter = QPainter(self.obstacles)
        pen = QPen(QColor(Qt.white), 5)
        painter.setPen(pen)
        painter.drawPoint(x, y)
        painter.end()

    def is_obstacle(self, x, y):
        return self.obstacles.pixel(x, y) == qRgb(0, 0, 255)

    def paint(self, painter):
        painter.save()
        # Draw obstacles
        painter.drawImage(0, 0, self.obstacles)
        # Draw pheromones
        for x in range(0, len(self.pheromones), self.step_size):
            for y in range(0, len(self.pheromones[x]), self.step_size):
                if self.pheromones[x][y] <= 0.01:
                    continue
                col_alpha = self.pheromones[x][y] / self.max_pheromones * 255
                painter.setPen(QPen(QColor(255, 0, 0, col_alpha), 1))
                painter.setBrush(QBrush(QColor(255, 0, 0, col_alpha), 1))
                painter.drawEllipse(QRectF(x - 2, y - 2, 4, 4))
        # Draw anthill
        painter.setBrush(QBrush(QColor(255, 0, 0)))
        painter.setPen(QPen(QColor(Qt.black), 1))
        painter.drawEllipse(QRectF(self.anthill[0] - 6, self.anthill[1] - 6, 12, 12))
        # Draw food sources
        painter.setBrush(QBrush(QColor(0, 255, 0)))
        painter.setPen(QPen(QColor(Qt.black), 1))
        for f in self.food:
            painter.drawEllipse(QRectF(f[0] - 4, f[1] - 4, 8, 8))
        painter.restore()
