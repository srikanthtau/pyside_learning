import sys
from PySide2 import QtGui, QtWidgets

class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Add ICON to the APP")
        #self.setWindowIcon(QtGui.QIcon(''))

        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    icon_app = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
