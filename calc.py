from PySide2 import QtCore, QtWidgets, QtGui
import sys, os
from ui import Ui_MainWindow
import math, clipboard

os.environ['QT_MAC_WANTS_LAYER'] = '1'

app = QtWidgets.QApplication(sys.argv)
form = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(form)
form.show()


def b1():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '1')
    else:
        ui.label.setText('1')
    ui.label.repaint()


def b2():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '2')
    else:
        ui.label.setText('2')
    ui.label.repaint()


def b3():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '3')
    else:
        ui.label.setText('3')
    ui.label.repaint()


def b4():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '4')
    else:
        ui.label.setText('4')
    ui.label.repaint()


def b5():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '5')
    else:
        ui.label.setText('5')
    ui.label.repaint()


def b6():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '6')
    else:
        ui.label.setText('6')
    ui.label.repaint()


def b7():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '7')
    else:
        ui.label.setText('7')
    ui.label.repaint()


def b8():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '8')
    else:
        ui.label.setText('8')
    ui.label.repaint()


def b9():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '9')
    else:
        ui.label.setText('9')
    ui.label.repaint()


def b0():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '0')
    ui.label.repaint()


def bp():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '.')
    ui.label.repaint()


def plus():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '+')
    ui.label.repaint()


def minus():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '-')
    ui.label.repaint()


def umn():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '×')
    ui.label.repaint()


def podel():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '÷')
    ui.label.repaint()


def c():
    if ui.label.text() != '0' and len(ui.label.text()) > 1:
        ui.label.setText(ui.label.text()[:-1])
    elif ui.label.text() != '0' and len(ui.label.text()) <= 1:
        ui.label.setText('0')
    ui.label.repaint()


def ac():
    ui.label.setText('0')
    ui.label.repaint()


def res():
    try:
        if ui.label.text()[0] == '√':
            ui.label.setText(str(math.sqrt(int(ui.label.text()[1:]))))
            pass
        if ui.label.text()[len(ui.label.text()) - 1] == '!':
            ui.label.setText(str(math.factorial(int(ui.label.text()[:-1]))))
            pass

        mathch = ui.label.text().replace('×', '*').replace('÷', '/').replace('^', '**')
        ui.label.setText(str(eval(mathch)))
        ui.label.repaint()
    except (SyntaxError, ZeroDivisionError):
        ui.label.setText('ERROR!')
        ui.label.repaint()


def minc():
    if ui.label.text() != '0':
        ui.label.setText('-' + ui.label.text())
    ui.label.repaint()


def sqrtc():
    if ui.label.text() == '0':
        ui.label.setText('√')
    else:
        ui.label.setText('√' + ui.label.text())

    ui.label.repaint()


def fact():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '!')
    ui.label.repaint()


def copyres():
    clipboard.copy(ui.label.text())
    QtWidgets.QMessageBox().information(None, 'Window', 'Copied!', QtWidgets.QMessageBox().Ok)


def step():
    if ui.label.text() != '0':
        ui.label.setText(ui.label.text() + '^')
    ui.label.repaint()

ui.actionCopy_result.setShortcut(QtGui.QKeySequence('Ctrl+C'))
ui.b1.clicked.connect(b1)
ui.b2.clicked.connect(b2)
ui.b3.clicked.connect(b3)
ui.b4.clicked.connect(b4)
ui.b5.clicked.connect(b5)
ui.b6.clicked.connect(b6)
ui.b7.clicked.connect(b7)
ui.b8.clicked.connect(b8)
ui.b9.clicked.connect(b9)
ui.b0.clicked.connect(b0)
ui.bp.clicked.connect(bp)
ui.plus.clicked.connect(plus)
ui.minus.clicked.connect(minus)
ui.umn.clicked.connect(umn)
ui.podel.clicked.connect(podel)
ui.C.clicked.connect(c)
ui.AC.clicked.connect(ac)
ui.res.clicked.connect(res)
ui.min.clicked.connect(minc)
ui.sqrt.clicked.connect(sqrtc)
ui.fact.clicked.connect(fact)
ui.actionCopy_result.triggered.connect(copyres)
ui.step.clicked.connect(step)

sys.exit(app.exec_())
