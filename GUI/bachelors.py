import os
import sys

from gi.repository import Gtk, Gdk


class BachelorsWindow():

	GLADEFILE = "open-main.glade"
	
	
	def __init__(self):
		self.create_window()
		

	def create_window(self):
		'''Создание основного окна Бакалавра
		'''
		builder = Gtk.Builder()
		builder.add_from_file(self.GLADEFILE)
		builder.connect_signals(Handlers())
		# Bachelor's Window
		self.window1 = builder.get_object("window2")

		# Notebook
		# Page 1
		# Entries
		self.nameEntry = builder.get_object("nameEntry")
		self.authorEntry = builder.get_object("authorEntry")
		self.dirPrepEntry = builder.get_object("dirPrepEntry")
		self.qualEntry = builder.get_object("qualEntry")
		self.leaderEntry = builder.get_object("leaderEntry")
		self.chefEntry = builder.get_object("chefEntry")
		self.dateEntry = builder.get_object("dateEntry")
		self.studentEntry = builder.get_object("studentEntry")
		self.consulsEntry = builder.get_object("consulsEntry")
		self.markEntry = builder.get_object("markEntry")
		self.datePropEntry = builder.get_object("datePropEntry")
		self.assistsEntry = builder.get_object("assistsEntry")
		self.pagesEntry = builder.get_object("pagesEntry")
		self.demosEntry = builder.get_object("demosEntry")
		# Comboboxes
		self.facultyBoxTitle = builder.get_object("facultyBoxTitle")
		self.departmentBoxTitle = builder.get_object("departmentBoxTitle")
		self.groupBoxTitle = builder.get_object("groupBoxTitle")
		# List Stores
		self.facultyList = builder.get_object("facultyList")
		self.departmentList = builder.get_object("departmentList")
		self.groupList = builder.get_object("groupsList")
		# Buttons
		self.createButton = builder.get_object("createTitleButton")

		self.window1.show_all()


class Handlers():

	def open_bachelors_blanks(self):
		pass
