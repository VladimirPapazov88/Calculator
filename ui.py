# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(619, 474)
        MainWindow.setAutoFillBackground(True)
        self.actionCopy_result = QAction(MainWindow)
        self.actionCopy_result.setObjectName(u"actionCopy_result")
        font = QFont()
        font.setFamily(u"Apple Braille")
        self.actionCopy_result.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 571, 91))
        font1 = QFont()
        font1.setFamily(u"Apple Braille")
        font1.setPointSize(36)
        self.label.setFont(font1)
        self.label.setMouseTracking(True)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.b1 = QPushButton(self.centralwidget)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(10, 120, 101, 51))
        font2 = QFont()
        font2.setFamily(u"Apple Braille")
        font2.setPointSize(18)
        self.b1.setFont(font2)
        self.b1.setMouseTracking(False)
        self.b1.setCheckable(False)
        self.b1.setAutoDefault(True)
        self.b2 = QPushButton(self.centralwidget)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(130, 120, 101, 51))
        self.b2.setFont(font2)
        self.b3 = QPushButton(self.centralwidget)
        self.b3.setObjectName(u"b3")
        self.b3.setGeometry(QRect(250, 120, 101, 51))
        self.b3.setFont(font2)
        self.b4 = QPushButton(self.centralwidget)
        self.b4.setObjectName(u"b4")
        self.b4.setGeometry(QRect(10, 180, 101, 51))
        self.b4.setFont(font2)
        self.b5 = QPushButton(self.centralwidget)
        self.b5.setObjectName(u"b5")
        self.b5.setGeometry(QRect(130, 180, 101, 51))
        self.b5.setFont(font2)
        self.b6 = QPushButton(self.centralwidget)
        self.b6.setObjectName(u"b6")
        self.b6.setGeometry(QRect(250, 180, 101, 51))
        self.b6.setFont(font2)
        self.b7 = QPushButton(self.centralwidget)
        self.b7.setObjectName(u"b7")
        self.b7.setGeometry(QRect(10, 240, 101, 51))
        self.b7.setFont(font2)
        self.b8 = QPushButton(self.centralwidget)
        self.b8.setObjectName(u"b8")
        self.b8.setGeometry(QRect(130, 240, 101, 51))
        self.b8.setFont(font2)
        self.b9 = QPushButton(self.centralwidget)
        self.b9.setObjectName(u"b9")
        self.b9.setGeometry(QRect(250, 240, 101, 51))
        self.b9.setFont(font2)
        self.b0 = QPushButton(self.centralwidget)
        self.b0.setObjectName(u"b0")
        self.b0.setGeometry(QRect(70, 300, 101, 51))
        self.b0.setFont(font2)
        self.bp = QPushButton(self.centralwidget)
        self.bp.setObjectName(u"bp")
        self.bp.setGeometry(QRect(190, 300, 101, 51))
        self.bp.setFont(font2)
        self.podel = QPushButton(self.centralwidget)
        self.podel.setObjectName(u"podel")
        self.podel.setGeometry(QRect(390, 120, 101, 51))
        self.podel.setFont(font2)
        self.umn = QPushButton(self.centralwidget)
        self.umn.setObjectName(u"umn")
        self.umn.setGeometry(QRect(390, 180, 101, 51))
        self.umn.setFont(font2)
        self.minus = QPushButton(self.centralwidget)
        self.minus.setObjectName(u"minus")
        self.minus.setGeometry(QRect(390, 240, 101, 51))
        self.minus.setFont(font2)
        self.plus = QPushButton(self.centralwidget)
        self.plus.setObjectName(u"plus")
        self.plus.setGeometry(QRect(390, 300, 101, 51))
        self.plus.setFont(font2)
        self.res = QPushButton(self.centralwidget)
        self.res.setObjectName(u"res")
        self.res.setGeometry(QRect(10, 360, 371, 51))
        self.res.setFont(font2)
        self.C = QPushButton(self.centralwidget)
        self.C.setObjectName(u"C")
        self.C.setGeometry(QRect(390, 360, 101, 51))
        font3 = QFont()
        font3.setFamily(u"Apple Braille")
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setWeight(50)
        self.C.setFont(font3)
        self.AC = QPushButton(self.centralwidget)
        self.AC.setObjectName(u"AC")
        self.AC.setGeometry(QRect(500, 360, 101, 51))
        self.AC.setFont(font3)
        self.sqrt = QPushButton(self.centralwidget)
        self.sqrt.setObjectName(u"sqrt")
        self.sqrt.setGeometry(QRect(500, 180, 101, 51))
        self.sqrt.setFont(font2)
        self.step = QPushButton(self.centralwidget)
        self.step.setObjectName(u"step")
        self.step.setGeometry(QRect(500, 240, 101, 51))
        self.step.setFont(font2)
        self.fact = QPushButton(self.centralwidget)
        self.fact.setObjectName(u"fact")
        self.fact.setGeometry(QRect(500, 300, 101, 51))
        self.fact.setFont(font2)
        self.min = QPushButton(self.centralwidget)
        self.min.setObjectName(u"min")
        self.min.setGeometry(QRect(500, 120, 101, 51))
        self.min.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 619, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionCopy_result)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.actionCopy_result.setText(QCoreApplication.translate("MainWindow", u"Copy result", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.b4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.b5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.b6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.b8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.b9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.b0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bp.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.podel.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.umn.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.res.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.AC.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.step.setText(QCoreApplication.translate("MainWindow", u"x^y", None))
        self.fact.setText(QCoreApplication.translate("MainWindow", u"x!", None))
        self.min.setText(QCoreApplication.translate("MainWindow", u"-x", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi
