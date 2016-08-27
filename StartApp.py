__author__ = 'Juan Manuel Bermúdez Cabrera'

if __name__ == '__main__':
    import sys

    from PyQt4.QtGui import QApplication, QIcon, QPixmap

    from gui.forms.MainWindow import MainWindow

    app = QApplication(sys.argv)

    icon = QIcon()
    icon.addPixmap(QPixmap("../icons/app 128.png"), QIcon.Normal, QIcon.Off)
    app.setWindowIcon(icon)

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
