#!/usr/bin/python
# encoding: utf-8

import npyscreen, curses
from mywidgets import InfoBox, LogForm, LogView

class RebMa:
	@staticmethod
	def createErlAppAndRel():
		npyscreen.notify_wait("not implementet yet")

class RebMaGit:
	@staticmethod
	def getList():
		return ["Cowboy", "Lager", "mimetypes"]

class RebMaCurses(npyscreen.NPSAppManaged):
	def onStart(self):
		npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
		self.addForm("MAIN", RebMaMainForm, name="RebMa - Start")
		self.log = self.addForm("LOG", LogForm, name="RebMa - LOG")

	def onCleanExit(self):
		return 0

	def change_form(self, name):
		self.switchForm(name)
		self.resetHistory()

class RebMaMainForm(npyscreen.ActionForm):
	def create(self):
		self.action = self.add(npyscreen.MultiLine, max_height=self.lines-5, value=0, scroll_exit=True,
			values=["Create new Erlang Application and Release",
			"Create new Erlang Application in existing Release",
			"Create new Erlang Application without Release",
			"Manage Dependencies of existing Erlang Application"])
		self.add(npyscreen.FixedText, value="Prease ^L to view Log", editable=False)
		self.add_handlers({"^L": self.show_log,
			"^Q": self.exit})

	def on_ok(self):
		if self.action.value == 0:
			RebMa.createErlAppAndRel()
			self.parentApp.log.appendMessage('Execute Option »{0}«'.format(self.action.values[self.action.value]),
					"curently in work")
		else:
			self.parentApp.log.appendMessage('Execute Option »{0}«'.format(self.action.values[self.action.value]),
					self.action.value)
		self.action.hidden=True
	
	def on_cancel(self):
		self.parentApp.switchForm(None)
	
	def exit(self, *args, **keywords):
		self.parentApp.change_form(None)

	def show_log(self, *args, **keywords):
		self.parentApp.change_form("LOG")


if __name__ == "__main__":
	App = RebMaCurses()
	App.run()
