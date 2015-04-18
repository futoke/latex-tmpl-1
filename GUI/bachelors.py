import os
import sys

from gi.repository import Gtk, Gdk


class BachelorsWindow():

	GLADEFILE = "open-main.glade"
	# КТУ
	departmentCSM = ["БИТ", "ВПТС", "ВТ", "ИКГ", "ИС ТПП", "ИТПР", "ИПМ", "ИНС", "КОТ", "МП БЭВА", "МТ", "ОЦСиТ", "ПБКС", "СТТБ", "СУиИ", "ТПС", "ТВ", "УСС", "ЭТиПЭМС"]
	# ИТИП
	departmentITIP = ["ВПВ", "ИС", "КТ", "ПИВП", "РИС", "ТП"]
	# ИКТ
	departmentDICT = ["БТ", "ГИС", "ИКТвАФиАП", "ИСиТвВБ", "ППиТИ", "ПС", "СФ", "СиУвИС", "ТС"]
	# ФиОИ
	departmentPOI = ["КФиВИ", "НТМ", "Кафедра наноинформатики и метаматериалов", "ОФиСЕ", "ОТиМ", "ФиОИ"]
	# ТМИ
	departmentTMI = ["МиК", "ПМиТТ", "ПЭ", "ТПиУИ", "УГИС", "ФМиА", "ЭиСМ"]
	# ИХиБТ
	departmentXKTK = ["Математики", "ИП", "ИиПМ", "КВ", "КриоТех", "ПКТ", "ТОТХТ", "ТМиМ", "Физики(ИХиБТ)", "ХМиНЭ", "ХУ", "ЭиЭ"]

	departmentTPP = ["АБиТП", "БЖиПТ", "КИТиМХ", "ПБПРС", "ПиАПП", "ТМиПБТ", "ТМРПиКХ", "ТМиО", "ХиМБ"]
	 # ИФ
	departmentIF = ["ИТиКТ", "ИФ", "ИТТЭК", "КТФиЭМ", "ЛТБМО", "ЛТиЭП", "ОЛ", "СТ", "СФМ", "ТТОЭ", "ЭН"]
	# ОИСТ
	departmentOIST = ["ОЭПиС", "ПиКО"]
	# ИКВО
	departmentIKVO = ["БСУОВ", "ВК", "ИТЗИ", "МиПИУ", "СПЗИ", "ФВиВ"]
	# ИМБИП
	departmentIMBIP = ["ИСиУИ", "МЭиМО", "ПД", "ТДиЛ", "КТиТН", "ФС", "ШГА"]
	# ЕН
	departmentEN = ["ЭПиМ", "ВМ", "ИТГС", "ТиПМ", "Физика"]

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
		self.facultyBoxTitle.connect("changed", self.change_department_list)
		self.departmentBoxTitle = builder.get_object("departmentBoxTitle")
		self.departmentBoxTitle.connect("changed", self.change_groups_list)
		self.groupBoxTitle = builder.get_object("groupBoxTitle")
		# List Stores
		self.facultyList = builder.get_object("facultyList")
		self.departmentList = builder.get_object("departmentList")
		self.groupList = builder.get_object("groupsList")
		# Buttons
		self.createButton = builder.get_object("createTitleButton")
		self.createButton.connect("clicked", self.on_click_createButton)

		self.window1.show_all()
		
	def on_click_createButton(self, widget):
		self.getName()
		

	def getName(self):
		'''Вывод введённого названия работы'''
		self.checkEnteredValue(self.nameEntry)
		

	def checkEnteredValue(self, entry):
		'''Проверка пустое поле или нет'''
		if entry.get_text() == "":
			raise ValueError
		else:
			print(entry.get_text())


	def determine_list_store(self, listNumber):
		arrayOfListsStores = [self.departmentCSM, self.departmentITIP, 
			self.departmentEN, self.departmentIMBIP, self.departmentIKVO, 
			self.departmentOIST, self.departmentIF, self.departmentTPP, 
			self.departmentXKTK, self.departmentTMI, self.departmentPOI, 
			self.departmentDICT]
		for i in arrayOfListsStores[listNumber]:
			self.departmentList.append([i])
		self.departmentBoxTitle.set_model(self.departmentList)


	def change_department_list(self, combo):
		tree_iter = combo.get_active()
		self.KEY = tree_iter
		print(tree_iter)
		if tree_iter != None:
			self.departmentList.clear()
			self.determine_list_store(tree_iter)

	
class Handlers():

	def open_bachelors_blanks(self):
		pass
