import sys
from PySide2 import QtGui, QtWidgets

class ShowToolTip(QtWidgets.QWidget):
    def __init__(self):
        super(ShowToolTip, self).__init__()

        self.initUI()

    def initUI(self):
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif',10))
        self.setToolTip("This is Widget class")

        button = QtWidgets.QPushButton('Button',self)
        button.setToolTip("This is a button")
        button.resize(button.sizeHint())
        button.move(50,50)

        self.setGeometry(500, 500, 400, 400)
        self.setWindowTitle("Widget to show tool tip")
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    show_tooltip = ShowToolTip()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

