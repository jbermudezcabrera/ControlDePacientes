import os

from PyQt4 import uic
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog, QDialogButtonBox

__author__ = 'Juan Manuel Bermúdez Cabrera'


class APPDialog(QDialog):
    def __init__(self, controller, *args):
        super(APPDialog, self).__init__(*args)

        uic.loadUi(os.path.join('resources', 'uis', 'APPDialog.ui'), self)

        self.controller = controller

        self.buttonBox.button(QDialogButtonBox.Save).setText('Guardar')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')

        self.buttonBox.accepted.connect(self.on_save)

        self.hta = None
        self.ci = None
        self.hc = None
        self.ht = None
        self.dm = None
        self.smoker = None
        self.other = None
        self.idiag = None

        self._data_collected = False

        self._init_dm()
        self._init_smoker()

    def _init_dm(self):
        self.dmCombo.clear()
        self.dmCombo.addItem('No', 0)
        self.dmCombo.addItem('Tipo I', 1)
        self.dmCombo.addItem('Tipo II', 2)

    def _init_smoker(self):
        self.smokerCombo.clear()
        self.smokerCombo.addItem('No', 0)
        self.smokerCombo.addItem('Ex', 1)
        self.smokerCombo.addItem('Si', 2)

    @property
    def data_collected(self):
        return self._data_collected

    def modify_app(self, app):
        if app is not None:
            self.htaCheck.setChecked(app.hta)
            self.ciCheck.setChecked(app.ci)
            self.hclCheck.setChecked(app.hc)
            self.htdCheck.setChecked(app.ht)

            self.dmCombo.setCurrentIndex(self.dmCombo.findData(app.dm))
            self.smokerCombo.setCurrentIndex(self.smokerCombo.findData(app.fumador))

            self.otherInput.setText(app.otro)
            self.idInput.setPlainText(app.idiagnostico)

    @pyqtSlot()
    def on_save(self):
        self.hta = self.htaCheck.isChecked()
        self.ci = self.ciCheck.isChecked()
        self.hc = self.hclCheck.isChecked()
        self.ht = self.htdCheck.isChecked()
        self.dm = self.dmCombo.itemData(self.dmCombo.currentIndex())
        self.smoker = self.smokerCombo.itemData(self.smokerCombo.currentIndex())
        self.other = self.otherInput.text().strip()
        self.idiag = self.idInput.toPlainText().strip()

        self._data_collected = True
        self.close()
