import random
from enum import Enum

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class AntState(Enum):
    searching = 1
    transporting = 2


class Ant:

    def __init__(self, world, x, y):
        self.world = world
        self.position = (x, y)
        self.track = [self.position]
        self.state = AntState.searching
        self.pheromone_concentration = 0

    def move_to(self, pos):
        self.position = pos
        self.track.append(pos)

    def simulate_step(self):
        if self.state == AntState.searching:
            self.move_to(self.choose_transition())
            if self.world.is_food_source(self.position):
                self.state = AntState.transporting
                self.eliminate_cycles()
                self.pheromone_concentration = self.calculate_pheromone_concentration()
        else:
            self.position = self.track.pop()
            self.world.release_pheromones(self.position, self.pheromone_concentration)
            if self.position == self.world.anthill:
                self.state = AntState.searching
                self.track = [self.world.anthill]

    def calculate_pheromone_concentration(self):
        track_length = 0
        track_copy = self.track[:]
        while not track_copy.pop() == self.world.anthill:
            track_length += 1
        return 1.0 / track_length

    def choose_transition(self):
        transitions = self.world.get_transitions(self.position)

        chosen_transition = self.position
        num_of_iterations = 0
        while chosen_transition in self.track[-10:] and num_of_iterations < 10:
            num_of_iterations += 1
            decision = random.random()
            p = 0
            for t in transitions:
                p += self.world.get_probability(self.position, t)
                if decision <= p:
                    chosen_transition = t
                    break
        return chosen_transition

    def eliminate_cycles(self):
        i = len(self.track)-1
        while not i == 0:
            first_occurrence = self.forward_search(self.track, self.track[i])
            if first_occurrence < i:
                del self.track[first_occurrence:i]
                i = first_occurrence
            else:
                i -= 1

    @staticmethod
    def forward_search(list, item):
        for i in range(len(list)):
            if list[i] == item:
                return i
        return None

    def paint(self, painter):
        painter.save()
        if self.state == AntState.searching:
            painter.setBrush(QBrush(QColor(0, 0, 0)))
        else:
            painter.setBrush(QBrush(Qt.yellow))
        painter.setPen(QPen(QColor(Qt.black), 1))
        painter.drawEllipse(QRectF(self.position[0] - 2, self.position[1] - 2, 4, 4))
        painter.restore()
