import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt

dbfilename = 'assignment6.dat'


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        list = ['Name', 'Age', 'Score']

        Name = QLabel('Name:')
        Age = QLabel('Age:')
        Score = QLabel('Score:')
        Amount = QLabel('Amount:')
        Key = QLabel('Key:')
        Result = QLabel('Result:')

        NameEdit = QLineEdit()
        AgeEdit = QLineEdit()
        ScoreEdit = QLineEdit()
        AmountEdit = QLineEdit()
        ResultEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(5)
        self.setLayout(grid)

        grid.addWidget(Name, 0, 0)
        grid.addWidget(NameEdit, 0, 1)

        grid.addWidget(Age, 0, 2)
        grid.addWidget(AgeEdit, 0, 3)

        grid.addWidget(Score, 0, 4)
        grid.addWidget(ScoreEdit, 0, 5)

        grid.addWidget(Amount, 1, 2)
        grid.addWidget(AmountEdit, 1, 3)

        grid.addWidget(Key, 1, 4)

        grid.addWidget(Result, 3, 0)
        grid.addWidget(ResultEdit, 4, 0, 1, 6)

        self.lbl = QLabel("Name", self)
        combo = QComboBox(self)
        combo.addItem("Name")
        combo.addItem("Age")
        combo.addItem("Score")
        combo.move(465, 35)
        self.lbl.move(40, 250)

        Add = QPushButton("Add");
        Del = QPushButton("Del");
        Find = QPushButton("Find");
        Inc = QPushButton("Inc");
        Show = QPushButton("Show");

        grid.addWidget(Add, 2, 1)
        grid.addWidget(Del, 2, 2)
        grid.addWidget(Find, 2, 3)
        grid.addWidget(Inc, 2, 4)
        grid.addWidget(Show, 2, 5)

        Add.clicked.connect(self.addclick)
        Del.clicked.connect(self.delclick)
        Find.clicked.connect(self.findclick)
        Inc.clicked.connect(self.incclick)
        Show.clicked.connect(self.showclick)



        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def addclick(self):
        sender=self.sender()
        self.showclick()

    def closeEvent(self, event):
        self.writeScoreDB()
        reply = QMessageBox.question(self, 'message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())