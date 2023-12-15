from PyQt5.QtWidgets import QApplication, QMessageBox


# Alert
def alert(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle('Alert')
    msg.setText(text)


class Gui:
    def __init__(self):
        # self.actions = GuiBehavior(self)
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(abs('ico.ico')))
        app.setStyle('Fusion')
        app.aboutToQuit.connect(self.actions.handle_exit)
        self.main_win()
        self.add_links_win()
        self.settings_win()
        sys.exit(app.exec_())


Gui()
alert("What in the Hell are you doing!")
