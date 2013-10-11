#!/usr/bin/python
# encoding: utf-8

import npyscreen, curses
from rebmaStartForm import RebMaStartForm
from rebmaCreateErlAppAndRelForm import RebMaCreateErlAppAndRelForm
from mywidgets import InfoBox, LogForm, LogView

class RebMaCurses(npyscreen.NPSAppManaged):
	def onStart(self):
		npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
		self.addForm("MAIN", RebMaStartForm, name="RebMa - Start")
		self.addForm("CreateErlAppAndRel", RebMaCreateErlAppAndRelForm, name="RebMa - Create Erlang Application and Release")
		self.log = self.addForm("LOG", LogForm, name="RebMa - LOG")

	def onCleanExit(self):
		return 0

	def change_form(self, name):
		self.switchForm(name)


if __name__ == "__main__":
	App = RebMaCurses()
	App.run()
