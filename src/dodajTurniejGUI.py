#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re, os
from src.ui import windowTournaments_ui
import importGUI, playerGUI
import player
import myZODB, transaction

class DodajTurniejGUI(QtGui.QMainWindow, windowTournaments_ui.Ui_windowTournaments):
	def __init__(self, parent=None, name=None, fl=0):
		super(DodajTurniejGUI, self).__init__(parent)
		self.setupUi(self)
		self.otherWindow = None

		### Tournaments var ####{{{
		self.name = None
		self.uid = None#}}}

		### SIGNALS ####{{{
		self.buttonAnuluj.connect(self.buttonAnuluj, SIGNAL("clicked()"), self.close)
		self.buttonImport.connect(self.buttonImport, SIGNAL("clicked()"), self.openImportPlayer)
		self.inputSkrotNazwy.connect(self.inputSkrotNazwy, SIGNAL("textChanged()"), self.checkUID)
		self.buttonWybierzZaw.connect(self.buttonWybierzZaw, SIGNAL("clicked()"), self.openWindowPlayer)#}}}
	
	def checkUID(self):
		self.getExisted()
		for self.ui


	def getExisted(self):#{{{
		self.tournamentsDB = myZODB.myZODB('src/db/tournaments.fs')
		self.tournaments = self.tournamentsDB.dbroot()
		self.existing = self.tournaments.keys()
		self.playersDB.close()#}}}

	def openWindowPlayer(self):#{{{
		if (self.tournamentId()):
			self.otherWindow = playerGUI.PlayerGUI()
			self.otherWindow.show()#}}}

	def openImportPlayer(self):#{{{
		if (self.tournamentId()):
			self.otherWindow = importGUI.ImportGUI()
			self.otherWindow.show()#}}}

	def tournamentId(self):#{{{
		if (self.inputSkrotNazwy.toPlainText() != '') and (self.inputNazwa.toPlainText() != ''):
			self.uid = self.inputSkrotNazwy.toPlainText()
			self.name = self.inputNazwa.toPlainText()
			return self.checkUID()
		else:
			QtGui.QMessageBox.information(self, 'Brakuje informacji',\
						str("Prosze podac nazwe turnieju oraz skrocona wersje"))
			return False#}}}