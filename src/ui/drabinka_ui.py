# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drabinka.ui'
#
# Created: Mon Jun 10 13:53:54 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1500, 900)
        Form.setMinimumSize(QtCore.QSize(1500, 900))
        Form.setMaximumSize(QtCore.QSize(1500, 900))
        self.saveButton = QtGui.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(10, 10, 141, 27))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Form", "Zapisz wyniki meczy", None, QtGui.QApplication.UnicodeUTF8))

