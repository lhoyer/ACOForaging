import sys

from PyQt4.QtGui import *

from aco.aco_logic import ACOLogic
from gui.aco_gui_ui import Ui_ACOGui


class ACOGui(QMainWindow):

    def __init__(self):
        super(ACOGui, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_ACOGui()
        self.ui.setupUi(self)

        self.acoLogic = ACOLogic()
        self.ui.widget.set_aco(self.acoLogic)

        self.ui.startButton.clicked.connect(self.start_simulation)

    def start_simulation(self):
        self.acoLogic.start_simulation()


def main():
    app = QApplication(sys.argv)
    window = ACOGui()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
