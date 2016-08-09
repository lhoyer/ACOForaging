import sys

from PyQt4.QtGui import *

from aco.aco_logic import ACOLogic
from gui.aco_gui_ui import Ui_ACOGui
from gui.settings import settings


class ACOGui(QMainWindow):

    def __init__(self):
        super(ACOGui, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_ACOGui()
        self.ui.setupUi(self)

        self.acoLogic = ACOLogic()
        self.ui.widget.set_aco(self.acoLogic)

        self.ui.startButton.clicked.connect(self.start_simulation)
        self.ui.resetPheromonesButton.clicked.connect(self.acoLogic.world.reset_pheromones)
        self.ui.antNumSpin.valueChanged.connect(self.ant_number_changed)
        self.ui.alphaSpin.valueChanged.connect(self.alpha_changed)
        self.ui.rhoSpin.valueChanged.connect(self.rho_changed)
        settings.alpha = self.ui.alphaSpin.value()
        settings.num_ants = self.ui.antNumSpin.value()
        settings.rho = self.ui.rhoSpin.value()

    def start_simulation(self):
        self.acoLogic.start_simulation()

    @staticmethod
    def ant_number_changed(value):
        settings.num_ants = value

    @staticmethod
    def alpha_changed(value):
        settings.alpha = value

    @staticmethod
    def rho_changed(value):
        settings.rho = value


def main():
    app = QApplication(sys.argv)
    window = ACOGui()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
