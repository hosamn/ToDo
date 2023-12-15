import os
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox


# Alert
def alert(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle('Alert')
    msg.setText(text)

# Absolute path
def abspath(f):
    return os.path.abspath(os.path.dirname(__file__)) + '/' + f

class Gui:
    def __init__(self):
        # self.actions = GuiBehavior(self)
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(abspath('ico.ico')))
        app.setStyle('Fusion')
        # app.aboutToQuit.connect(self.actions.handle_exit)
        # self.main_win()
        # self.add_links_win()
        # self.settings_win()
        # sys.exit(app.exec_())


Gui()
alert("What in the Hell are you doing!")


# https://github.com/jovanzers/1fichier-dl/blob/main/src/gui.py
