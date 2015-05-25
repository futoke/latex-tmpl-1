__author__ = 'eprivalov'

from gi.repository import Gtk, Gdk
import os
import GUI.bachelors


class Schedule(object):

    array_of_line = []
    total_table = []

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("open-main.glade")
        # Calendar's Window
        self.schedule_window = self.builder.get_object("window_schedule")
        self.schedule_window.set_title("Time Schedule")
        # Buttons
        self.schedule_accept_button = self.builder.get_object("accept_button")
        self.schedule_accept_button.connect("clicked", self.clicked_accept_button)
        self.schedule_clear_button = self.builder.get_object("clear_button")
        self.schedule_clear_button.connect("clicked", self.clicked_clear_button)
        self.schedule_window.show_all()
        Gtk.main()


    def clicked_accept_button(self, button):
        """

        Issue: FIX creating table in the TEX file. (!)

        :param button:
        :return:
        """
        self.array_of_line = [[self.builder.get_object("num%s" % i).get_text(),
                               self.builder.get_object("name%s" % i).get_text(),
                               self.builder.get_object("dead%s" % i).get_text(),
                               self.builder.get_object("mark%s" % i).get_text()] for i in range(1, 16)]
        count = 0
        string = ""
        for i in self.array_of_line:
            for j in range(len(i)):
                if j is len(i)-1:
                    string += "%s \\\\ \\hline \n" % i[j]
                    count += 1
                else:
                    string += "%s & " % i[j]
        string += " & & & \\\\ \\hline \n"*int((count/4))
        self.total_table.append(string)
        self.schedule_window.hide()

    def clicked_clear_button(self, button):
        self.schedule_window.destroy()
