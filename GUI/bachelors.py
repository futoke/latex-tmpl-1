import os, shutil

from gi.repository import Gdk, Gtk
from GUI.calendar import Calendar, TempFiles


class BachelorsWindow():
    """

    """

    dict_of_fields = {
        "[ARTICLE-1]": None,
        "[AUTHOR]": None,
        "[DIRECTION]": None,
        "[LEADER]": None,
        "[CHEF]": None,
        "[YEAR]": None,
        "[STUDENT]": None,
        "[CONSULT-A]": None,
        "[TOTAL-MARK]": None,
        "[MONTH]": None,
        "[DAY]": None,
        "[SECRET]": None,
        "[SHEETS]": None,
        "[DEMO-MATERIALS]": None,
        "[FACULTY]": None,
        "[DEPARTMENT]": None,
        "[GROUP]": None,
        "[DAY-DEF]": None,
        "[MONTH-DEF]": None,
        "[YEAR-DEF]": None
        }

    gladefile = "open-main.glade"
    # КТУ
    department_csm = ["БИТ", "ВПТС", "ВТ", "ИКГ", "ИС ТПП", "ИТПР", "ИПМ", "ИНС", "КОТ", "МП БЭВА", "МТ", "ОЦСиТ",
                      "ПБКС", "СТТБ", "СУиИ", "ТПС", "ТВ", "УСС", "ЭТиПЭМС"]
    groups_csm = [["4130", "4131", "4132", "4133", "4894"], ["-"], ["4100", "4101", "4105", "4106"],
                  ["4641", "4642", "4643", "4645"], ["-"], ["-"], ["4120", "4121", "4125"], ["4163"], ["4108"], ["-"],
                  ["4671", "4672"], ["-"], ["4155", "4156", "4157", "4840", "4896"], ["-"],
                  ["4145", "4146", "4147", "4810"], ["4650", "4651", "4652", "4809", "4860"], ["-"], ["-"], ["4166"]]
    # ИТИП
    department_itip = ["ВПВ", "ИС", "КТ", "ПИВП", "РИС", "ТП"]
    groups_itip = [["-"], ["4501", "4511", "4512", "4514", "4515", "4520", "4521", "4522"], ["4537", "4538", "4539"],
                   ["-"], ["-"], ["-"], ["-"]]
    # ИКТ
    department_dict = ["БТ", "ГИС", "ИКТвАФиАП", "ИСиТвВБ", "ППиТИ", "ПС", "СФ", "СиУвИС", "ТС"]
    groups_dict = [["-"], ["-"], ["-"], ["-"], ["-"], ["4957", "4958"], ["4951"], ["4955", "4956"], ["-"]]
    # ФиОИ
    department_poi = ["КФиВИ", "НТМ", "Кафедра наноинформатики и метаматериалов", "ОФиСЕ", "ОТиМ", "ФиОИ"]
    groups_poi = [["4320", "4321", "4352", "4362", "4363"], ["4675"], ["-"], ["-"], ["4345", "4351"], ["4350", "4360"]]
    # ТМИ
    department_tmi = ["МиК", "ПМиТТ", "ПЭ", "ТПиУИ", "УГИС", "ФМиА", "ЭиСМ"]
    groups_tmi = [["-"], ["и4501", "и4504", "и4644", "4050", "4051", "4890"], ["и4505", "и4641"], ["-"], ["-"],
                  ["и4502", "и4503", "и4643", "4080"], ["4060", "4062", "4070", "4072", "4073"]]
    # ИХиБТ
    department_xktk = ["Математики", "ИП", "ИиПМ", "КВ", "КриоТех", "ПКТ", "ТОТХТ", "ТМиМ", "Физики(ИХиБТ)", "ХМиНЭ",
                       "ХУ", "ЭиЭ"]
    groups_xktk = [["-"], ["-"], ["-"], ["и4403", "и4604"], ["и4401", "и4402", "и4603"], ["-"], ["-"], ["-"], ["-"],
                   ["и4101", "и4102", "и4601", "и4602"], ["и4104", "и4608"], ["-"]]

    department_tpp = ["АБиТП", "БЖиПТ", "КИТиМХ", "ПБПРС", "ПиАПП", "ТМиПБТ", "ТМРПиКХ", "ТМиО", "ХиМБ"]
    groups_tpp = [["и4201", "и4611"], ["-"], ["-"], ["и4302", "и4303", "и4621", "и4622"], ["-"],
                  ["и4304", "и4305", "и4619", "и4632"], ["и4301", "и4306", "и4307", "и4623", "и4631"],
                  ["и4202", "и4203", "и4613", "и4614"], ["-"]]
    # ИФ
    department_if = ["ИТиКТ", "ИФ", "ИТТЭК", "КТФиЭМ", "ЛТБМО", "ЛТиЭП", "ОЛ", "СТ", "СФМ", "ТТОЭ", "ЭН"]
    groups_if = [["4660"], ["-"], ["4203"], ["4211", "4212"], ["4221", "4222"], ["4231", "4232"], ["4251"],
                 ["-"], ["-"], ["4241", "4244"], ["-"]]
    # ОИСТ
    department_oist = ["ОЭПиС", "ПиКО"]
    groups_oist = [["4310", "4311", "4312", "4830"], ["4301", "4303", "4309"]]
    # ИКВО
    department_ikvo = ["БСУОВ", "ВК", "ИТЗИ", "МиПИУ", "СПЗИ", "ФВиВ"]
    groups_ikvo = [["-"], ["-"], ["-"], ["4750", "4751"], ["-"], ["-"]]
    # ИМБИП
    department_imbip = ["ИСиУИ", "МЭиМО", "ПД", "ТДиЛ", "КТиТН", "ФС", "ШГА"]
    groups_imbip = [["-"], ["-"], ["-"], ["4440", "4441", "4442"], ["-"], ["-"], ["-"]]
    # ЕН
    department_en = ["ЭПиМ", "ВМ", "ИТГС", "ТиПМ", "Физика"]
    groups_en = [["-"], ["4742", "4743"], ["4707", "4711"], ["-"], ["-"]]

    def __init__(self):
        """

        :return: nothing
        """
        builder = Gtk.Builder()
        builder.add_from_file(self.gladefile)
        builder.connect_signals(Handlers())
        '''Bachelor's Window'''
        self.window1 = builder.get_object("window2")
        self.window1.set_title("Bachelor")
        self.window1.connect("delete-event", Gtk.main_quit)
        """Notebook
        Page 1
        Entries
        """
        self.name_entry = builder.get_object("nameEntryTitle")
        self.author_entry = builder.get_object("authorEntryTitle")
        self.dir_prep_entry = builder.get_object("dirPrepEntryTitle")
        self.qual_entry = builder.get_object("qualEntryTitle")
        self.leader_entry = builder.get_object("leaderEntryTitle")
        self.chef_entry = builder.get_object("chefEntryTitle")
        self.date_entry = builder.get_object("dateEntryTitle")
        self.student_entry = builder.get_object("studentEntryTitle")
        self.consuls_entry = builder.get_object("consulsEntryTitle")
        self.mark_entry = builder.get_object("markEntryTitle")
        self.date_prop_entry = builder.get_object("datePropEntryTitle")
        self.assists_entry = builder.get_object("assistsEntryTitle")
        self.pages_entry = builder.get_object("pagesEntryTitle")
        self.demos_entry = builder.get_object("demosEntryTitle")
        '''Comboboxes'''
        self.faculty_box_title = builder.get_object("facultyBoxTitle")
        self.faculty_box_title.connect("changed", self.change_department_list)
        self.department_box_title = builder.get_object("departmentBoxTitle")
        self.department_box_title.connect("changed", self.change_groups_list)
        self.group_box_title = builder.get_object("groupBoxTitle")
        '''List Store'''
        self.faculty_list = builder.get_object("facultyList")
        self.department_list = builder.get_object("departmentList")
        self.group_list = builder.get_object("groupsList")
        # Buttons
        self.create_button = builder.get_object("createTitleButton")
        self.create_button.connect("clicked", self.change_tex_file)
        '''Calendar buttons'''
        self.choose_date_top = builder.get_object("button16")
        self.choose_date_top.connect("clicked", self.get_date_from_calendar)
        self.choose_date_bottom = builder.get_object("button17")
        self.choose_date_bottom.connect("clicked", self.get_date_def_from_calendar)
        # Save window
        '''will delete'''
        self.save_tex_file = builder.get_object("filechooserdialog1")
        self.save_button = builder.get_object("save-action-button")
        self.cancel_button = builder.get_object("cancel-action-button")


        '''allert window'''
        self.allert_window_for_enter_empty_entries = builder.get_object("allert-empty-entries")


        self.window1.show_all()

    @staticmethod
    def get_date_def_from_calendar(button):
        """

        :param button:
        :return: nothing
        """
        Calendar()

    @staticmethod
    def get_date_from_calendar(button):
        """

        :param button:
        :return: nothing
        """
        Calendar()

    def determine_list_store(self, list_number):
        """

        :param list_number:
        :return: nothing
        """
        array_of_lists_stores = [self.department_csm, self.department_itip, self.department_en, self.department_imbip,
                                 self.department_ikvo, self.department_oist, self.department_if, self.department_tpp,
                                 self.department_xktk, self.department_tmi, self.department_poi, self.department_dict]
        for i in array_of_lists_stores[list_number]:
            self.department_list.append([i])
        self.department_box_title.set_model(self.department_list)

    def determine_group_store(self, group_number):
        """

        :param group_number:
        :return: nothing
        """
        array_of_group_lists = [self.groups_csm, self.groups_itip, self.groups_dict, self.groups_poi, self.groups_tmi,
                                self.groups_xktk, self.groups_tpp, self.groups_if, self.groups_oist, self.groups_ikvo,
                                self.groups_imbip, self.groups_en]
        for i in array_of_group_lists[self.key_iter][group_number]:
            self.group_list.append([i])
        self.group_box_title.set_model(self.group_list)

    def change_department_list(self, combo):
        """

        :param combo:
        :return: nothing
        """
        tree_iter = combo.get_active()
        self.key_iter = tree_iter
        if tree_iter is not None:
            self.department_list.clear()
            self.determine_list_store(tree_iter)

    def change_groups_list(self, combo):
        """

        :param combo:
        :return: nothing
        """
        tree_iter = combo.get_active()
        print("Group id: %s" % tree_iter)
        if tree_iter is not None:
            self.group_list.clear()
            self.determine_group_store(tree_iter)

    @property
    def got_entry_fields(self):
        """

        :return: self.dict_of_fields
        """
        self.dict_of_fields["[ARTICLE-1]"] = self.name_entry.get_text()
        self.dict_of_fields["[AUTHOR]"] = self.author_entry.get_text()
        self.dict_of_fields["[DIRECTION]"] = self.dir_prep_entry.get_text()
        self.dict_of_fields["[LEADER]"] = self.leader_entry.get_text()
        self.dict_of_fields["[CHEF]"] = self.chef_entry.get_text()
        self.dict_of_fields["[STUDENT]"] = self.student_entry.get_text()
        self.dict_of_fields["[CONSULT-A]"] = self.consuls_entry.get_text()
        self.dict_of_fields["[TOTAL-MARK]"] = self.mark_entry.get_text()
        self.dict_of_fields["[SECRET]"] = self.assists_entry.get_text()
        self.dict_of_fields["[SHEETS]"] = self.pages_entry.get_text()
        self.dict_of_fields["[DEMO-MATERIALS]"] = self.demos_entry.get_text()
        '''Taken date'''
        # self.get_date_from_temp_file()
        # print("end: ", TempFiles.a)
        # self.dict_of_fields["[DAY]"] = self.get_date_from_temp_file()[0]
        # self.dict_of_fields["[MONTH]"] = self.get_date_from_temp_file()[1]
        # self.dict_of_fields["[YEAR]"] = self.get_date_from_temp_file()[2]
        #
        # self.dict_of_fields["[DAY-DEF]"] = self.get_date_from_temp_file()[3]
        # self.dict_of_fields["[MONTH-DEF]"] = self.get_date_from_temp_file()[4]
        # self.dict_of_fields["[YEAR-DEF]"] = self.get_date_from_temp_file()[5]

        self.dict_of_fields["[DAY]"] = Calendar.array_of_dates[0]
        self.dict_of_fields["[MONTH]"] = Calendar.array_of_dates[1]
        self.dict_of_fields["[YEAR]"] = Calendar.array_of_dates[2]
        self.dict_of_fields["[DAY-DEF]"] = Calendar.array_of_dates[3]
        self.dict_of_fields["[MONTH-DEF]"] = Calendar.array_of_dates[4]
        self.dict_of_fields["[YEAR-DEF]"] = Calendar.array_of_dates[5]

        self.faculty_model = self.faculty_box_title.get_model()
        self.dict_of_fields["[FACULTY]"] = self.faculty_model[self.faculty_box_title.get_active_iter()][0]

        self.department_model = self.department_box_title.get_model()
        self.dict_of_fields["[DEPARTMENT]"] = self.department_model[self.department_box_title.get_active_iter()][0]

        self.group_model = self.group_box_title.get_model()
        self.dict_of_fields["[GROUP]"] = self.group_model[self.group_box_title.get_active_iter()][0]

        self.valid_all_entries(self.dict_of_fields)

        # TempFiles().open_file()
        # print("end: ", TempFiles.a)
        # os.remove(os.getcwd()+"\\temp")

        return self.dict_of_fields

    def change_tex_file(self, button):
        """

        :param button:
        :return: nothing
        """
        self.dict_of_fields = self.got_entry_fields

        #self.valid_all_entries(self.dict_of_fields)

        self.work_file = open(os.getcwd()+"\\test", "r", encoding="utf-8")
        self.readed = self.work_file.read()
        self.work_file.close()
        self.work_file = open(os.getcwd()+"\\%s.tex" % self.dict_of_fields["[AUTHOR]"].lower(), "a", encoding="utf-8")
        for i in self.dict_of_fields.keys():
            self.readed = self.readed.replace(str(i), str(self.dict_of_fields[i]))
        print("Test: %s" % self.dict_of_fields)
        #self.valid_all_entries(self.dict_of_fields)
        self.work_file.write(self.readed)
        self.work_file.close()

    @staticmethod
    def get_date_from_temp_file():
        """

        :return:
        """
        return TempFiles().open_file()

    @staticmethod
    def valid_all_entries(check_dict):
        for element in check_dict.values():
            if element is None or element is "":
                print("Element %s is empty" % element)


class Handlers():
    """

    """

    def passed(self):
        """

        :return: nothing
        """
        pass