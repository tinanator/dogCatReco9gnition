# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(693, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnImgSelect = QtWidgets.QPushButton(self.centralwidget)
        self.btnImgSelect.setGeometry(QtCore.QRect(260, 280, 171, 61))
        font = QtGui.QFont()
        font.setItalic(True)
        self.btnImgSelect.setFont(font)
        self.btnImgSelect.setObjectName("btnImgSelect")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 110, 271, 141))
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnRecognize = QtWidgets.QPushButton(self.centralwidget)
        self.btnRecognize.setEnabled(False)
        self.btnRecognize.setGeometry(QtCore.QRect(260, 340, 171, 61))
        self.btnRecognize.setObjectName("btnRecognize")
        self.prediction = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.prediction.setGeometry(QtCore.QRect(250, 420, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.prediction.setFont(font)
        self.prediction.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.prediction.setAutoFillBackground(False)
        self.prediction.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.prediction.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.prediction.setTabChangesFocus(False)
        self.prediction.setReadOnly(True)
        self.prediction.setPlainText("")
        self.prediction.setOverwriteMode(False)
        self.prediction.setCenterOnScroll(False)
        self.prediction.setObjectName("prediction")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnImgSelect.setText(_translate("MainWindow", "Выберите картинку"))
        self.btnRecognize.setText(_translate("MainWindow", "Это кто"))

