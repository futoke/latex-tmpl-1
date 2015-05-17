import os, shutil

from gi.repository import Gdk, Gtk
from GUI.calendar import Calendar, TempFiles


class BachelorsWindow(object):
    """
    Class creates a file with widening ".tex" by the addition text and dates from due to text fields.

    In future: will be add an allert window which notify a user about empty fields and not creates a file until it
    will be repaired.
    """

    dict_of_fields = {
        "[ARTICLE-1]": None,
        "[ARTICLE-2]": None,
        "[AUTHOR]": None,
        "[DIRECTION]": None,
        "[LEADER]": None,
        "[CHEF]": None,
        "[YEAR]": None,
        "[STUDENT]": None,
        "[CONSUL-A]": None,
        "[CONSUL-B]": None,
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
        self.consuls_a_entry = builder.get_object("consulsAEntryTitle")
        self.consuls_b_entry = builder.get_object("consulsBEntryTitle")
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
        self.choose_date_bottom.connect("clicked", self.get_date_from_calendar)
        # Save window
        '''will delete'''
        self.save_tex_file = builder.get_object("filechooserdialog1")
        self.save_button = builder.get_object("save-action-button")
        self.cancel_button = builder.get_object("cancel-action-button")
        self.window1.show_all()

    @staticmethod
    def get_date_def_from_calendar(button):
        """

        :param button:
        :return: nothing
        """
        Calendar()

    def determine_list_store(self, list_number):
        """
        Determination the list of the departments which will be interjected in the model of the departments box
        :param list_number: current number of the faculty
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
        Determination the list of the groups which will be interjected in the model of the group box
        :param group_number: current number of the department
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

    def build_article(self):
        """
        If article not fit on the one line, function will divides it on two through the separation of 76 characters.
        :return first_line_of_article, second_line_of_article:
        """
        article = self.name_entry.get_text()
        article = article.split(" ")
        print(article)
        first_line_of_article = []
        remainder_of_article = ""
        for current_word in article:
            remainder_of_article += current_word
            remainder_of_article += " "
            if len(remainder_of_article) <= 76:
                first_line_of_article.append(remainder_of_article)
            else:
                first_line_of_article = first_line_of_article.pop()[:-1]
        second_line_of_article = remainder_of_article[len(first_line_of_article):].strip()
        return first_line_of_article, second_line_of_article

    @staticmethod
    def addition_lines_to_text_field(text_field):
        """
        The input is a string that is modified by the addition of N spaces before and after it.
        :return line: chaged line
        """
        length_of_field = 23
        length_of_line = len(text_field)
        count_of_spaces = 0
        if length_of_line < length_of_field:
            count_of_spaces = int((length_of_field - length_of_line) / 2)
        line = "\quad"*count_of_spaces+" "+text_field+"\\quad"*count_of_spaces
        return line

    @property
    def got_entry_fields(self):
        """
        Take text from each field of the active Label of the window and interjected it into dictionary
        :return self.dict_of_fields:
        """
        self.dict_of_fields["[ARTICLE-1]"] = self.build_article()[0]
        self.dict_of_fields["[ARTICLE-2]"] = self.build_article()[1]
        self.dict_of_fields["[AUTHOR]"] = self.addition_lines_to_text_field(self.author_entry.get_text())
        self.dict_of_fields["[DIRECTION]"] = self.dir_prep_entry.get_text()
        self.dict_of_fields["[LEADER]"] = self.addition_lines_to_text_field(self.leader_entry.get_text())
        self.dict_of_fields["[CHEF]"] = self.addition_lines_to_text_field(self.chef_entry.get_text())
        self.dict_of_fields["[STUDENT]"] = self.addition_lines_to_text_field(self.student_entry.get_text())
        self.dict_of_fields["[CONSUL-A]"] = self.addition_lines_to_text_field(self.consuls_a_entry.get_text())
        self.dict_of_fields["[CONSUL-B]"] = self.addition_lines_to_text_field(self.consuls_b_entry.get_text())
        self.dict_of_fields["[TOTAL-MARK]"] = self.mark_entry.get_text()
        self.dict_of_fields["[SECRET]"] = self.assists_entry.get_text()
        self.dict_of_fields["[SHEETS]"] = self.pages_entry.get_text()
        self.dict_of_fields["[DEMO-MATERIALS]"] = self.demos_entry.get_text()
        '''Taken date'''
        self.dict_of_fields["[DAY]"] = Calendar.array_of_dates[0]
        self.dict_of_fields["[MONTH]"] = Calendar.array_of_dates[1]
        self.dict_of_fields["[YEAR]"] = Calendar.array_of_dates[2]
        self.dict_of_fields["[DAY-DEF]"] = Calendar.array_of_dates[3]
        self.dict_of_fields["[MONTH-DEF]"] = Calendar.array_of_dates[4]
        self.dict_of_fields["[YEAR-DEF]"] = Calendar.array_of_dates[5]
        # Taken student "properties"
        self.faculty_model = self.faculty_box_title.get_model()
        self.dict_of_fields["[FACULTY]"] = self.faculty_model[self.faculty_box_title.get_active_iter()][0]
        self.department_model = self.department_box_title.get_model()
        self.dict_of_fields["[DEPARTMENT]"] = self.department_model[self.department_box_title.get_active_iter()][0]
        self.group_model = self.group_box_title.get_model()
        self.dict_of_fields["[GROUP]"] = self.group_model[self.group_box_title.get_active_iter()][0]

        return self.dict_of_fields

    def change_tex_file(self, button):
        """
        Creates a file with widening ".tex" by the addition text and dates from due to text fields.
        :param button:
        :return nothing:
        """
        self.dict_of_fields = self.got_entry_fields
        self.work_file = open(os.getcwd()+"\\test.tex", "r", encoding="UTF-8")
        self.readed = self.work_file.read()
        self.work_file.close()
        self.work_file = open(os.getcwd()+"\\%s.tex" % self.author_entry.get_text(), "a", encoding="UTF-8")
        for i in self.dict_of_fields.keys():
            self.readed = self.readed.replace(str(i), str(self.dict_of_fields[i]))
        self.work_file.write(self.readed)
        self.work_file.close()


class Handlers(object):
    """

    """

    def passed(self):
        """

        :return: nothing
        """
        pass