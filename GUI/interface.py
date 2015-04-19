import os
import sys

from gi.repository import Gtk, Gdk

from GUI.bachelors import BachelorsWindow

class CreateMainWindow:

	GLADEFILE = "interface.glade"
	def __init__(self):

		builder = Gtk.Builder()
		builder.add_from_file(self.GLADEFILE)
		builder.connect_signals(Handlers())
		global window
		window = builder.get_object("window1")
		window.show_all()
		Gtk.main()
	

class Handlers():

	def open_bachelors_blanks(self, button):
		BachelorsWindow()
		window.destroy()

	def open_master_blanks(self, button):
		window.destroy()
		pass

	def open_specialist_blanks(self, button):
		window.destroy()
		pass

