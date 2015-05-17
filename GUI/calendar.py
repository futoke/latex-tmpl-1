__author__ = 'eprivalov'

from gi.repository import Gtk, Gdk

import os, shutil
import tempfile

import GUI.bachelors


class Calendar():

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

        # TempFiles().create_tmp_file_for_date(self.calendar)
        self.create_tmp_file_for_date(self.calendar)
        self.calendar_window.hide()
        return self.calendar.get_date()

    def clicked_cancel_button(self, button):
        print("clicked Cancel")
        self.calendarWindow.destroy()

    def create_tmp_file_for_date(self, args):
        if args is not None:
            date = str(args.get_date())
            months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
              "Ноябрь", "Декабрь"]
            list_of_date = date[1:-1].split(", ")
            #print(list_of_date)
            taken_year = int(list_of_date[0])
            taken_month = months[int(list_of_date[1])]
            taken_day = int(list_of_date[2])
            #self.a = (taken_day, taken_month, taken_year)
            self.array_of_dates.append(taken_day), self.array_of_dates.append(taken_month)
            self.array_of_dates.append(taken_year)
            # with open(self.work_directory+"\\temp", "a+", encoding="utf-8") as temp_file:
            #     temp_file.writelines(str(self.a)+"\n")
        else:
            pass



class TempFiles:

    work_directory = os.getcwd()
    array_of_dates = []


    def create_tmp_file_for_date(self, args):
        if args is not None:
            date = str(args.get_date())
            months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
              "Ноябрь", "Декабрь"]
            list_of_date = date[1:-1].split(", ")
            #print(list_of_date)
            taken_year = int(list_of_date[0])
            taken_month = months[int(list_of_date[1])]
            taken_day = int(list_of_date[2])
            #self.a = (taken_day, taken_month, taken_year)
            self.array_of_dates.append(taken_day), self.array_of_dates.append(taken_month)
            self.array_of_dates.append(taken_year)
            # with open(self.work_directory+"\\temp", "a+", encoding="utf-8") as temp_file:
            #     temp_file.writelines(str(self.a)+"\n")
        else:
            pass

    def open_file(self):
        with open(self.work_directory+"\\temp", "r+", encoding="utf-8") as read_file:
            #print("readed: ", read_file.readlines())
            take_data = read_file.readlines()
        normal_day = take_data[0][1:-2].split(", ")[0]
        normal_month = take_data[0][1:-2].split(", ")[1]
        normal_year = take_data[0][1:-2].split(", ")[2]

        day_def = take_data[1][1:-2].split(", ")[0]
        month_def = take_data[1][1:-2].split(", ")[1]
        year_def = take_data[1][1:-2].split(", ")[2]

        self.a.append(normal_day)
        self.a.append(normal_month)
        self.a.append(normal_year)
        self.a.append(day_def)
        self.a.append(month_def)
        self.a.append(year_def)

        print("start: ", self.a)

        return normal_day, normal_month, normal_year, day_def, month_def, year_def


'''
class TempFiles():

    def create_tmp_file_for_date(self, args):
        tmp = tempfile.NamedTemporaryFile(mode="w+t", delete=False)
        try:
            if args is not None:
                tmp.write(str(args.get_date()))
                tmp.seek(0)
                global tmpText, year, month, day
                tmpText = self.change_date_format(tmp.read())
                year = tmpText[2]
                month = tmpText[1]
                day = tmpText[0]
            else:
                pass
        except FileExistsError:
            print("File not found.")
        finally:
            tmp.close()
        return year, month, day

    @staticmethod
    def change_date_format(date_from_file):
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                  "Ноябрь", "Декабрь"]
        list_of_date = date_from_file[1:-1].split(", ")
        taken_year = int(list_of_date[0])
        taken_month = months[int(list_of_date[1])]
        taken_day = int(list_of_date[2])

        return taken_day, taken_month, taken_year'''
