import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from math import*
class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('My Calculator')
        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)
        self.display = QtWidgets.QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        grid.addWidget(self.display,0,0,1,5)
        names = [
        '7', '8', '9', '*','/',
        '4', '5', '6', '+','-',
        '1', '2', '3', '(',')',
        '0', '.', '=', 'C',]
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),(0,4),
           (1, 0), (1, 1), (1, 2), (1, 3),(1,4),
           (2, 0), (2, 1), (2, 2), (2, 3),(2,4),
           (3, 0), (3, 1), (3, 2), (3, 3),(3,4),
           (4, 0), (4, 1), (4, 2), (4, 3)]
        c = 0
        for name in names:
             button = QtWidgets.QPushButton(name)
             button.clicked.connect(self.buttonClicked)
             grid.addWidget(button, pos[c][0] + 1, pos[c][1])
             c = c + 1

    def buttonClicked(self):
        sender = self.sender();
        #self.display.setText(sender.text())
        key = sender.text()
        if key == "=":
            result=str(eval(self.display.text()))
            self.display.setText(result)
        elif key == "C":
            self.display.setText('0')
        else:
            if (self.display.text() == "0"):
                self.display.setText('')
            self.display.setText(self.display.text()+key)
app = QtWidgets.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
