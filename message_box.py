import sys
from PySide2 import QtGui, QtWidgets, QtCore

class MessageBox(QtWidgets.QWidget):
    def __int__(self):
        super(MessageBox, self).__int__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Message",
                                               "Are you sure you want to quit?", QtWidgets.QMessageBox.Yes |:wq
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QtWidgets.QApplication(sys.argv)
    message_box = MessageBox()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


