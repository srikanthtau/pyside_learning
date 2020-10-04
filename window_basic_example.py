import sys
from PySide2 import QtGui, QtWidgets

# PySide application needs an Application object
app = QtWidgets.QApplication(sys.argv)

# QWidget is the base class for all the UI objects
# Widget with no parent is called a window
window = QtWidgets.QWidget()
window.resize(250, 250)
window.setWindowTitle("First QT Application")
window.show()


sys.exit(app.exec_())



