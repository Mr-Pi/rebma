#!/usr/bin/python
# encoding: utf-8

import npyscreen, curses, rebmaControl
from rebmaStartForm import RebMaStartForm
from rebmaCreateErlAppAndRelForm import RebMaCreateErlAppAndRelForm
from mywidgets import InfoBox, LogForm, LogView

class RebMaCurses(npyscreen.NPSAppManaged):
	def onStart(self):
		npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)

		npyscreen.notify("Please Wait...")
		self.rebMaControl = rebmaControl.RebMaControl("https://raw.github.com/Mr-Pi/rebma/master/repos.txt")

		self.addForm("MAIN", RebMaStartForm, name="RebMa - Start")
		self.addForm("CreateErlAppAndRel", RebMaCreateErlAppAndRelForm,
				name="RebMa - Create Erlang Application and Release")
		self.log = self.addForm("LOG", LogForm, name="RebMa - LOG")

	def onCleanExit(self):
		return 0

	def change_form(self, name):
		self.switchForm(name)


def main():
	App = RebMaCurses()
	return App.run()


if __name__ == "__main__":
	main()
