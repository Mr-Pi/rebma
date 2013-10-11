# encoding: utf-8

import npyscreen

class RebMaStartForm(npyscreen.ActionForm):
	def create(self):
		self.action = self.add(npyscreen.MultiLine, max_height=self.lines-5, value=0, scroll_exit=True,
			values=["Create new Erlang Application and Release",
			"Create new Erlang Application in existing Release",
			"Create new Erlang Application without Release",
			"Manage Dependencies of existing Erlang Application"])
		self.add(npyscreen.FixedText, value="Press ^L to view Log", editable=False)
		self.add_handlers({"^L": self.show_log,
			"^Q": self.exit})

	def on_ok(self):
		if self.action.value == 0:
			self.parentApp.log.appendMessage('Select Option »{0}«'.format(self.action.values[self.action.value]),
					"waiting for user input")
			self.parentApp.change_form("CreateErlAppAndRel")
		else:
			self.parentApp.log.appendMessage('Select Option »{0}«'.format(self.action.values[self.action.value]),
					"not implemented")
	
	def on_cancel(self):
		self.parentApp.switchForm(None)
	
	def exit(self, *args, **keywords):
		self.parentApp.change_form(None)
	def show_log(self, *args, **keywords):
		self.parentApp.change_form("LOG")
