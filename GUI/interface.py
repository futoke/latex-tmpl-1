import os
import sys

from gi.repository import Gtk, Gdk
from GUI.bachelors import BachelorsWindow


class CreateMainWindow:

    GLADEFILE = "open-main.glade"

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file(self.GLADEFILE)
        builder.connect_signals(Handlers())
        global window
        window = builder.get_object("window1")
        window.connect("delete-event", Gtk.main_quit)
        window.show_all()
        Gtk.main()


class Handlers():

    @staticmethod
    def open_bachelors_blanks(button):
        """Create a window for Bachelors blanks
        :param button:
        :return: nothing
        """
        BachelorsWindow()
        window.destroy()

    @staticmethod
    def open_master_blanks(button):
        """Create a window for Master blanks
        :param button:
        :return: nothing
        """
        window.destroy()
        pass

    @staticmethod
    def open_specialist_blanks(button):
        """Create a window for Specialist blanks
        :param button:
        :return: nothing
        """
        window.destroy()
        pass