# encoding: utf-8

import npyscreen


class RebMaCreateErlAppAndRelForm(npyscreen.ActionForm):
	def create(self):
		self.erlName = self.add(npyscreen.TitleText, name="Name:", scroll_exit=True)
		self.erlDeps = self.add(npyscreen.TitleMultiSelect, name="Dependencies", scroll_exit=True, max_height=10,
				values=self.parentApp.rebMaControl.get_repoList())
		self.add(npyscreen.FixedText, value="Press ^L to view Log", editable=False, rely=self.lines-3)
		self.add_handlers({"^L": self.show_log,
			"^Q": self.exit})

	def on_ok(self):
		npyscreen.notify_confirm("not implemented")
	def on_cancel(self):
		self.parentApp.switchForm(None)

	def exit(self, *args, **keywords):
		self.parentApp.change_form(None)
	def show_log(self, *args, **keywords):
		self.parentApp.change_form("LOG")
