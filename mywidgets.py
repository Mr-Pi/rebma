from npyscreen import BoxBasic, MultiLineEdit, FormBaseNew, MultiLine, notify_confirm
import curses
import weakref

class LogForm(FormBaseNew):
	def create(self):
		self.log = self.add(LogView, max_height=self.lines-15, name="Messages", scroll_exit=True)
		self.optionBox = self.add(BoxBasic, name="Options", editable=False, scroll_exit=True,
				max_width=30, rely=self.lines-13)
		self.infoBox = self.add(InfoBox, name="Information", scroll_exit=True,
				max_width=self.columns-36, relx=33, rely=self.lines-13)
		self.add_handlers({"^L": self.show_last,
			"^Q": self.exit})

	def appendMessage(self, msg, info):
		self.log.addLogMessage(msg, info)

	def exit(self, *args, **keywords):
		self.parentApp.change_form(None)
	def show_last(self, *args, **keywords):
		self.parentApp.switchFormPrevious()

class LogView(MultiLine):
	infoValues = []
	def addLogMessage(self,msg,info):
		self.values.insert(0,'{0}: {1}'.format(len(self.values), msg))
		self.infoValues.insert(0,str(info))

	def when_value_edited(self):
		try:
			infoMsg = self.infoValues[self.value]
		except:
			infoMsg = "no data aviable"
		try:
			self.parent.infoBox.value=infoMsg
			self.parent.infoBox.display()
		except:
			notify_confirm(infoMsg)

class InfoBox(BoxBasic):
	_contained_widget = MultiLineEdit
	def __init__(self, screen, *args, **keywords):
		super(InfoBox, self).__init__(screen, *args, **keywords)
		self.make_contained_widget()
	
	def make_contained_widget(self):
		self._my_widgets = []
		self._my_widgets.append(self._contained_widget(self.parent, 
		 rely=self.rely+1, relx = self.relx+2, 
		 max_width=self.width-4, max_height=self.height-2,
		 ))
		self.entry_widget = weakref.proxy(self._my_widgets[0])
			
	def update(self, clear=True):
		if self.hidden and clear:
			self.clear()
			return False
		elif self.hidden:
			return False
		super(InfoBox, self).update(clear=clear)
		for w in self._my_widgets:
			w.update(clear=clear)
	
	def edit(self):
		self.editing=True
		self.display()
		self.entry_widget.edit()
		#self.value = self.textarea.value
		self.how_exited = self.entry_widget.how_exited
		self.editing=False
		self.display()
	
	def get_value(self):
		if hasattr(self, 'entry_widget'):
			return self.entry_widget.value
		elif hasattr(self, '__tmp_value'):
			return self.__tmp_value
		else:
			return None
	def set_value(self, value):
		if hasattr(self, 'entry_widget'):
			self.entry_widget.value = value
		else:
			# probably trying to set the value before the textarea is initialised
			self.__tmp_value = value
	def del_value(self):
		del self.entry_widget.value
	value = property(get_value, set_value, del_value)
	
	def get_values(self):
		if hasattr(self, 'entry_widget'): 
			return self.entry_widget.values
		elif hasattr(self, '__tmp_value'):
			return self.__tmp_values
		else:
			return None
	def set_values(self, value):
		if hasattr(self, 'entry_widget'): 
			self.entry_widget.values = value
		elif hasattr(self, '__tmp_value'):
			# probably trying to set the value before the textarea is initialised
			self.__tmp_values = value
	def del_values(self):
		del self.entry_widget.value
	values = property(get_values, set_values, del_values)
	
	def get_editable(self):
		if hasattr(self, 'entry_widget'):
#			return False
			return self.entry_widget.editable
		else:
			return None
	def set_editable(self, value):
		if hasattr(self, 'entry_widget'): 
			self.entry_widget.editable = value
		elif hasattr(self, '__tmp_value'):
			# probably trying to set the value before the textarea is initialised
			self.__tmp_values = value
	def del_editable(self):
		del self.entry_widget.editable
	editable = property(get_editable, set_editable, del_editable)

