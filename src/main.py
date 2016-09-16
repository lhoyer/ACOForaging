import sys

from PyQt4.QtGui import *
from gui.aco_gui import ACOGui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ACOGui()

    window.show()
    sys.exit(app.exec_())
