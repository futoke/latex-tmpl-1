import os
import sys

from gi.repository import Gtk, Gdk


class BachelorsWindow():

	GLADEFILE = "open-main.glade"
	# КТУ
	departmentCSM = ["БИТ", "ВПТС", "ВТ", "ИКГ", "ИС ТПП", "ИТПР", "ИПМ", "ИНС", "КОТ", "МП БЭВА", "МТ", "ОЦСиТ", "ПБКС", "СТТБ", "СУиИ", "ТПС", "ТВ", "УСС", "ЭТиПЭМС"]
	groupsCSM = [["4130", "4131", "4132", "4133", "4894"],["-"],["4100", "4101", "4105", "4106"], ["4641", "4642", "4643", "4645"], ["-"], ["-"], ["4120", "4121", "4125"], ["4163"], ["4108"], ["-"], ["4671", "4672"], ["-"], ["4155", "4156", "4157", "4840", "4896"], ["-"], ["4145", "4146", "4147", "4810"], ["4650", "4651", "4652", "4809", "4860"], ["-"], ["-"], ["4166"]]
	# ИТИП
	departmentITIP = ["ВПВ", "ИС", "КТ", "ПИВП", "РИС", "ТП"]
	groupsITIP = [["-"], ["4501", "4511", "4512", "4514", "4515", "4520", "4521", "4522"], ["4537", "4538", "4539"], ["-"], ["-"], ["-"], ["-"]]
	# ИКТ
	departmentDICT = ["БТ", "ГИС", "ИКТвАФиАП", "ИСиТвВБ", "ППиТИ", "ПС", "СФ", "СиУвИС", "ТС"]
	groupsDICT = [["-"], ["-"], ["-"], ["-"], ["-"], ["4957", "4958"], ["4951"], ["4955", "4956"], ["-"]]
	# ФиОИ
	departmentPOI = ["КФиВИ", "НТМ", "Кафедра наноинформатики и метаматериалов", "ОФиСЕ", "ОТиМ", "ФиОИ"]
	groupsPOI = [["4320", "4321", "4352", "4362", "4363"], ["4675"], ["-"], ["-"], ["4345", "4351"], ["4350", "4360"]]
	# ТМИ
	departmentTMI = ["МиК", "ПМиТТ", "ПЭ", "ТПиУИ", "УГИС", "ФМиА", "ЭиСМ"]
	groupsTMI = [["-"], ["и4501", "и4504", "и4644", "4050", "4051", "4890"], ["и4505", "и4641"], ["-"], ["-"], ["и4502", "и4503", "и4643", "4080"], ["4060", "4062", "4070", "4072", "4073"]]
	# ИХиБТ
	departmentXKTK = ["Математики", "ИП", "ИиПМ", "КВ", "КриоТех", "ПКТ", "ТОТХТ", "ТМиМ", "Физики(ИХиБТ)", "ХМиНЭ", "ХУ", "ЭиЭ"]
	groupsXKTK = [["-"], ["-"], ["-"], ["и4403", "и4604"], ["и4401", "и4402", "и4603"], ["-"], ["-"], ["-"], ["-"], ["и4101", "и4102", "и4601", "и4602"], ["и4104", "и4608"], ["-"]]

	departmentTPP = ["АБиТП", "БЖиПТ", "КИТиМХ", "ПБПРС", "ПиАПП", "ТМиПБТ", "ТМРПиКХ", "ТМиО", "ХиМБ"]
	groupsTPP = [["и4201", "и4611"], ["-"], ["-"], ["и4302", "и4303", "и4621", "и4622"], ["-"], ["и4304", "и4305", "и4619", "и4632"], ["и4301", "и4306", "и4307", "и4623", "и4631"], ["и4202", "и4203","и4613", "и4614"], ["-"]]
	 # ИФ
	departmentIF = ["ИТиКТ", "ИФ", "ИТТЭК", "КТФиЭМ", "ЛТБМО", "ЛТиЭП", "ОЛ", "СТ", "СФМ", "ТТОЭ", "ЭН"]
	groupsIF = [["4660"], ["-"], ["4203"], ["4211", "4212"], ["4221", "4222"], ["4231", "4232"], ["4251"], ["-"], ["-"], ["4241", "4244"], ["-"]]
	# ОИСТ
	departmentOIST = ["ОЭПиС", "ПиКО"]
	groupsOIST = [["4310", "4311", "4312", "4830"], ["4301", "4303", "4309"]]
	# ИКВО
	departmentIKVO = ["БСУОВ", "ВК", "ИТЗИ", "МиПИУ", "СПЗИ", "ФВиВ"]
	groupsIKVO = [["-"], ["-"], ["-"], ["4750", "4751"], ["-"], ["-"]]
	# ИМБИП
	departmentIMBIP = ["ИСиУИ", "МЭиМО", "ПД", "ТДиЛ", "КТиТН", "ФС", "ШГА"]
	groupsIMBIP = [["-"], ["-"], ["-"], ["4440", "4441", "4442"], ["-"], ["-"], ["-"]]
	# ЕН
	departmentEN = ["ЭПиМ", "ВМ", "ИТГС", "ТиПМ", "Физика"]
	groupsEN = [["-"], ["4742", "4743"], ["4707", "4711"], ["-"], ["-"]]

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
