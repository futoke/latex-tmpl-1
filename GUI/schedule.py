__author__ = 'eprivalov'

from gi.repository import Gtk, Gdk
import os
import GUI.bachelors


class Schedule(object):

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("open-main.glade")
        # Calendar's Window
        self.schedule_window = builder.get_object("window_schedule")
        self.schedule_window.set_title("Time Schedule")
        # Buttons
        self.schedule_accept_button = builder.get_object("accept_button")
        self.schedule_accept_button.connect("clicked", self.clicked_accept_button)

        self.schedule_clear_button = builder.get_object("clear_button")
        self.schedule_clear_button.connect("clicked", self.clicked_clear_button)

        self.schedule_window.show_all()
        Gtk.main()

    def clicked_accept_button(self, button):
        print("accepted")
        self.schedule_window.destroy()

    def clicked_clear_button(self, button):
        print("cleared")
        self.schedule_window.destroy()
