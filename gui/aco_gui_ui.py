# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\aco_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from gui.aco_view import ACOView

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ACOGui(object):
    def setupUi(self, ACOGui):
        ACOGui.setObjectName(_fromUtf8("ACOGui"))
        ACOGui.resize(800, 600)
        self.centralwidget = QtGui.QWidget(ACOGui)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = ACOView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.verticalLayout.addWidget(self.startButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        ACOGui.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ACOGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ACOGui.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ACOGui)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ACOGui.setStatusBar(self.statusbar)

        self.retranslateUi(ACOGui)
        QtCore.QMetaObject.connectSlotsByName(ACOGui)

    def retranslateUi(self, ACOGui):
        ACOGui.setWindowTitle(_translate("ACOGui", "ACO Foraging", None))
        self.startButton.setText(_translate("ACOGui", "Start", None))