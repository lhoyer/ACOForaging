# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\aco_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.pauseButton = QtGui.QPushButton(self.centralwidget)
        self.pauseButton.setCheckable(True)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.verticalLayout.addWidget(self.pauseButton)
        self.resetButton = QtGui.QPushButton(self.centralwidget)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.verticalLayout.addWidget(self.resetButton)
        self.resetPheromonesButton = QtGui.QPushButton(self.centralwidget)
        self.resetPheromonesButton.setObjectName(_fromUtf8("resetPheromonesButton"))
        self.verticalLayout.addWidget(self.resetPheromonesButton)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.antCheckbox = QtGui.QCheckBox(self.groupBox)
        self.antCheckbox.setChecked(True)
        self.antCheckbox.setObjectName(_fromUtf8("antCheckbox"))
        self.verticalLayout_2.addWidget(self.antCheckbox)
        self.pheromonesCheckbox = QtGui.QCheckBox(self.groupBox)
        self.pheromonesCheckbox.setChecked(True)
        self.pheromonesCheckbox.setObjectName(_fromUtf8("pheromonesCheckbox"))
        self.verticalLayout_2.addWidget(self.pheromonesCheckbox)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.alphaSpin = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.alphaSpin.setDecimals(1)
        self.alphaSpin.setMaximum(100.0)
        self.alphaSpin.setSingleStep(0.5)
        self.alphaSpin.setProperty("value", 2.0)
        self.alphaSpin.setObjectName(_fromUtf8("alphaSpin"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.alphaSpin)
        self.rhoLabel = QtGui.QLabel(self.groupBox_2)
        self.rhoLabel.setObjectName(_fromUtf8("rhoLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.rhoLabel)
        self.rhoSpin = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.rhoSpin.setDecimals(3)
        self.rhoSpin.setMaximum(0.5)
        self.rhoSpin.setSingleStep(0.001)
        self.rhoSpin.setProperty("value", 0.002)
        self.rhoSpin.setObjectName(_fromUtf8("rhoSpin"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.rhoSpin)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.antNumSpin = QtGui.QSpinBox(self.groupBox_2)
        self.antNumSpin.setMaximum(10000)
        self.antNumSpin.setSingleStep(10)
        self.antNumSpin.setProperty("value", 100)
        self.antNumSpin.setObjectName(_fromUtf8("antNumSpin"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.antNumSpin)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.speedSpinBox = QtGui.QSpinBox(self.groupBox_2)
        self.speedSpinBox.setAccelerated(True)
        self.speedSpinBox.setMinimum(0)
        self.speedSpinBox.setMaximum(10000)
        self.speedSpinBox.setSingleStep(20)
        self.speedSpinBox.setProperty("value", 20)
        self.speedSpinBox.setObjectName(_fromUtf8("speedSpinBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.speedSpinBox)
        self.verticalLayout.addWidget(self.groupBox_2)
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
        self.pauseButton.setText(_translate("ACOGui", "Pause", None))
        self.resetButton.setText(_translate("ACOGui", "Reset", None))
        self.resetPheromonesButton.setText(_translate("ACOGui", "Reset pheromones", None))
        self.groupBox.setTitle(_translate("ACOGui", "Visualization", None))
        self.antCheckbox.setText(_translate("ACOGui", "Ants", None))
        self.pheromonesCheckbox.setText(_translate("ACOGui", "Pheromones", None))
        self.groupBox_2.setTitle(_translate("ACOGui", "ACO parameters", None))
        self.label.setText(_translate("ACOGui", "Alpha", None))
        self.rhoLabel.setText(_translate("ACOGui", "Evaporation coefficient", None))
        self.label_2.setText(_translate("ACOGui", "Number of ants", None))
        self.label_3.setText(_translate("ACOGui", "Simulation speed", None))

from gui.aco_view import ACOView
