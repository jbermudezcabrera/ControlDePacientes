# -*- coding: utf-8 -*-
from gui.forms import MainWindow

__author__ = 'Juan Manuel Bermúdez Cabrera'

if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import  QIcon, QPixmap

    from gui.forms.MainWindow import MainWindow

    app = QApplication(sys.argv)

    icon = QIcon()
    icon.addPixmap(QPixmap("../icons/app 128.png"), QIcon.Normal, QIcon.Off)
    app.setWindowIcon(icon)

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
