import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello PySide")
label.show()
app.exec_()

