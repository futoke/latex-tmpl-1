__author__ = 'eprivalov'

from gi.repository import Gtk, Gdk
import GUI.bachelors


class Calendar(object):

    array_of_dates = []

    def __init__(self, flag=None):
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
        self.create_tmp_file_for_date(self.calendar)
        self.calendar_window.hide()
        return self.calendar.get_date()

    def clicked_cancel_button(self, button):
        self.calendarWindow.destroy()

    def create_tmp_file_for_date(self, args):
        if args is not None:
            date = str(args.get_date())
            months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
              "Ноябрь", "Декабрь"]
            list_of_date = date[1:-1].split(", ")
            taken_year = int(list_of_date[0])
            taken_month = months[int(list_of_date[1])]
            taken_day = int(list_of_date[2])
            self.array_of_dates.append(taken_day), self.array_of_dates.append(taken_month)
            self.array_of_dates.append(taken_year)

        else:
            pass