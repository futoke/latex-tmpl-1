import os
import sys

from gi.repository import Gtk, Gdk

class CreateMainWindow:

	GLADEFILE = "open-main.glade"
	def __init__(self):

		builder = Gtk.Builder()
		builder.add_from_file(self.GLADEFILE)
		builder.connect_signals(Handlers())
		Gtk.main()
	

class Handlers():
  
  def for_future(self):
    pass
