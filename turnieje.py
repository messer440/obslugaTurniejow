#!/usr/bin/python2.7

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys, string, re
from src.ui import mainWindow_ui
from src import playerGUI

class Turnieje(QtGui.QMainWindow, mainWindow_ui.Ui_MainWindow):
	def __init__(self, parent=None, name=None, fl=0):
		super(Turnieje, self).__init__(parent)
		self.setupUi(self)

		self.otherWindow = None
#		windows = { "players" : PlayersGUI() }
		
		### SIGNALS ###
		self.gracze.connect(self.gracze, SIGNAL('clicked()'), self.openPlayers)
		self.buttonExit.connect(self.buttonExit, SIGNAL('clicked()'), self.close)

	def openPlayers(self):
		self.otherWindow = playerGUI.PlayersGUI() 
		#windows[nameOfWindow]
#		self.connect(self.otherWindow, SIGNAL('closed()')
		self.otherWindow.show()

	def main(self):
		self.show()

	def exit(self):
		sys.exit()


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	turnieje = Turnieje()
	turnieje.main()
	app.exec_()
