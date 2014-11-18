# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\uis\ACDialog.ui'
#
# Created: Tue Nov 18 15:37:54 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(608, 567)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.colInput = QtWidgets.QDoubleSpinBox(Dialog)
        self.colInput.setObjectName("colInput")
        self.gridLayout.addWidget(self.colInput, 3, 1, 1, 1)
        self.trigInput = QtWidgets.QDoubleSpinBox(Dialog)
        self.trigInput.setObjectName("trigInput")
        self.gridLayout.addWidget(self.trigInput, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.acidInput = QtWidgets.QDoubleSpinBox(Dialog)
        self.acidInput.setObjectName("acidInput")
        self.gridLayout.addWidget(self.acidInput, 5, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.creatInput = QtWidgets.QDoubleSpinBox(Dialog)
        self.creatInput.setObjectName("creatInput")
        self.gridLayout.addWidget(self.creatInput, 2, 1, 1, 1)
        self.hbInput = QtWidgets.QDoubleSpinBox(Dialog)
        self.hbInput.setProperty("showGroupSeparator", False)
        self.hbInput.setObjectName("hbInput")
        self.gridLayout.addWidget(self.hbInput, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.gliInput = QtWidgets.QDoubleSpinBox(Dialog)
        self.gliInput.setObjectName("gliInput")
        self.gridLayout.addWidget(self.gliInput, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Análisis Complementarios"))
        self.label_5.setText(_translate("Dialog", "Triglicéridos"))
        self.label_6.setText(_translate("Dialog", "Ácido úrico"))
        self.label.setText(_translate("Dialog", "Hemoglobina"))
        self.label_4.setText(_translate("Dialog", "Colesterol"))
        self.label_2.setText(_translate("Dialog", "Glicemia"))
        self.label_3.setText(_translate("Dialog", "Creatinina"))

