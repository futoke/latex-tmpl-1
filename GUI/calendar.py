__author__ = 'eprivalov'

from gi.repository import Gtk, Gdk

import os, shutil
import tempfile

import GUI.bachelors


class Calendar(object):
    """

    """

    dict_of_dates = {"day": None, "month": None, "year": None,
                     "day-def": None, "month-def": None, "year-def": None,
                     "day-assertion": None, "month-assertion": None, "year-assertion": None,
                     "day-dead": None, "month-dead": None, "year-dead": None,
                     "day-destription": None, "month-destription": None, "year-destription": None,
                     "day-acception": None, "month-acception": None, "year-acception": None,
                     "day-annotation": None, "month-annotation": None, "year-annotation": None,
                     "day-recentest": None, "month-recentest": None, "year-recentest": None,
                     "day-leader": None, "month-leader": None, "year-leader": None}

    def __init__(self, id):
        """

        :param id:
        :return:
        """
        self.id = id
        builder = Gtk.Builder()
        builder.add_from_file("open-main.glade")
        # Calendar's Window
        self.calendar_window = builder.get_object("calendar")
        self.calendar_window.set_title("Calendar")
        self.calendar = builder.get_object("calendar1")
        # Buttons
        self.calendar_ok_button = builder.get_object("CalendarOKButton")
        self.calendar_ok_button.connect("clicked", self.clicked_ok_button)

        self.calendar_cancel_button = builder.get_object("CalendarCancelButton")
        self.calendar_cancel_button.connect("clicked", self.clicked_cancel_button)

        self.calendar_window.show_all()
        Gtk.main()

    def clicked_ok_button(self, button):
        """

        :param button:
        :return:
        """
        self.create_tmp_file_for_date(self.calendar, self.id)
        self.calendar_window.hide()
        return self.calendar.get_date()

    def clicked_cancel_button(self, button):
        """

        :param button:
        :return:
        """
        self.calendar_window.destroy()

    def create_tmp_file_for_date(self, calendar, ident):
        """

        :param calendar:
        :param ident:
        :return:
        """
        if ident is 0:
            self.dict_fill(calendar, "day", "month", "year")
        elif ident is 1:
            self.dict_fill(calendar, "day-def", "month-def", "year-def")
        elif ident is 2:
            self.dict_fill(calendar, "day-assertion", "month-assertion", "year-assertion")
        elif ident is 3:
            self.dict_fill(calendar, "day-dead", "month-dead", "year-dead")
        elif ident is 4:
            self.dict_fill(calendar, "day-destription", "month-destription", "year-destription")
        elif ident is 5:
            self.dict_fill(calendar, "day-acception", "month-acception", "year-acception")
        elif ident is 6:
            self.dict_fill(calendar, "day-annotation", "month-annotation", "year-annotation")
        elif ident is 7:
            self.dict_fill(calendar, "day-recentest", "month-recentest", "year-recentest")
        elif ident is 8:
            self.dict_fill(calendar, "day-leader", "month-leader", "year-leader")

    def dict_fill(self, calendar, day, month, year):
        """

        :param calendar:
        :param day:
        :param month:
        :param year:
        :return:
        """
        if calendar is not None:
                date = str(calendar.get_date())
                months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                          "Ноябрь", "Декабрь"]
                list_of_date = date[1:-1].split(", ")
                taken_year = int(list_of_date[0])
                taken_month = months[int(list_of_date[1])]
                taken_day = int(list_of_date[2])
                self.dict_of_dates[day] = taken_day
                self.dict_of_dates[month] = taken_month
                self.dict_of_dates[year] = taken_year