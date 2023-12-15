from PyQt5.QtWidgets import QMessageBox


# Alert
def alert(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle('Alert')
    msg.setText(text)

alert("What in the Hell are you doing!")
