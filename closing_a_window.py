import sys
from PySide2 import QtGui, QtWidgets, QtCore

class ClosingWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ClosingWindow, self).__init__()

        self.initUI()

    def initUI(self):
        close_button = QtWidgets.QPushButton('Close Window', self)
        close_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        close_button.resize(close_button.sizeHint())
        close_button.move(50, 40)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    close_window = ClosingWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()