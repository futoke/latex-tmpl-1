"""
Version: Bidlokod
Issue: restructure Faculty, Department, Group
"""

import os

from gi.repository import Gdk, Gtk
from GUI.calendar import Calendar
from GUI.schedule import Schedule


class BachelorsWindow(object):
    """
    Class creates a file with widening ".tex" by the addition text and dates from due to text fields.

    In future: will be add an allert window which notify a user about empty fields and not creates a file until it
    will be repaired.
    """

    dict_of_fields = {
        # Page 1: Title
        '[ARTICLE-1]': None, '[ARTICLE-2]': None, '[AUTHOR]': None, '[DIRECTION]': None, '[LEADER]': None,
        '[CHEF]': None, '[STUDENT]': None, '[CONSULSA]': None, '[CONSULSB]': None, '[MARK]': None,
        '[GROUP]': None, '[ASSISTENT]': None, '[PAGES]': None, '[DEMO]': None, '[FACULTY]': None,
        '[DEPARTMENT]': None,

        # Page 2: Task
        '[TOPIC]': None, '[TECHNICALSUBJECT]': None, '[MAINTENANCE]': None, '[GRAPHIC]': None, '[SOURCES]': None,
        '[TABLE-LINES]': None,

        # Page 3: Annotation
        '[ORGANISATION]': None, '[HITECH]': None, '[DESCRIPTION]': None, '[GRADUATE]': None,
        '[GRANTS]': None, '[PUBLICES]': None, '[RESEARCHOBJECTIVE]': None, '[PROBLEMS]': None,
        '[TOTALSOURCES]': None, '[LAST5NATIVE]': None, '[MIDDLENATIVE]': None, '[MORE10NATIVE]': None,
        '[LAST5FOREIGN]': None, '[MIDDLEFOREIGN]': None, '[MORE10FOREIGN]': None, '[INTERNET-REQUEST]': None,
        '[INTERNETRESOURCES]': None,

        # Page 4: Review by Recentest
        '[SUBJECT]': None, '[ARTICLE]': None, '[TOPIC-ARTICLE]': None,

        # Page 5: Review by leader

        # Dates
        "[DAY]": None, "[MONTH]": None, "[YEAR]": None,
        "[DAY-DEF]": None, "[MONTH-DEF]": None, "[YEAR-DEF]": None,
        "[DAY-ASSERTION]": None, "[MONTH-ASSERTION]": None, "[YEAR-ASSERTION]": None,
        "[DAY-DEAD]": None, "[MONTH-DEAD]": None, "[YEAR-DEAD]": None,
        "[DAY-DESTRIPTION]": None, "[MONTH-DESTRIPTION]": None, "[YEAR-DESTRIPTION]": None,
        "[DAY-ACCEPTION]": None, "[MONTH-ACCEPTION]": None, "[YEAR-ACCEPTION]": None,
        "[DAY-ANNOTATION]": None, "[MONTH-ANNOTATION]": None, "[YEAR-ANNOTATION]": None,
        "[DAY-REVIEW-RECENTEST]": None, "[MONTH-REVIEW-RECENTEST]": None, "[YEAR-REVIEW-RECENTEST]": None,
        "[DAY-REVIEW-LEADER]": None, "[MONTH-REVIEW-LEADER]": None, "[YEAR-REVIEW-LEADER]": None
    }

    tab = ["Title", "Task", "Annotation", "Recentest", "Leader"]
    boxes = ["facultyBox", "departmentBox", "groupBox"]
    lists = ["facultyList", "departmentList", "groupsList"]

    objects = [
        # Page 1
        ["article", "author", "direction", "leader", "chef", "dateTop", "student", "consulsA", "consulsB", "mark",
         "dateProt", "assistent", "pages", "demo", "createButton"],
        # Page 2
        ["confirm", "date", "student", "leader", "topic", "direction", "dateDelivery", "technicalsubject",
         "maintenance", "graphic", "sources", "timeSchedule", "dateIssue", "dateAccepted", "createButton"],
        # Page 3
        ["student", "subject", "direction", "organisation", "researchobjective", "problems", "sources", "totalsources",
         "last5native", "middlenative", "more10native", "last5foreign", "middleforeign", "more10foreign",
         "internetComboBox", "internetresources", "hitech", "description", "grants", "publices", "graduate", "leader",
         "date", "createButton"],
        # Page 4
        ["student", "direction", "leader", "topic", "advantages", "disadvantages", "mark", "recentest", "date",
         "createButton"],
        # Page 5
        ["student", "direction", "leader", "topic", "advantages", "disadvantages", "mark", "date",
         "createButton"]
    ]

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

    # noinspection PyArgumentList
    def __init__(self):
        """

        :return: nothing
        """
        builder = Gtk.Builder()
        builder.add_from_file(self.gladefile)
        builder.connect_signals(Handlers())
        # Bachelor's Window
        self.window1 = builder.get_object("window2")
        self.window1.set_title("Bachelor")
        self.window1.connect("delete-event", Gtk.main_quit)
        """Page 1: Title List
        """
        tab = 0
        self.array_of_lists = [builder.get_object(self.lists[i]) for i in range(len(self.lists))]
        self.array_of_title = [builder.get_object(self.objects[tab][j] + self.tab[tab]) for j in
                               range(len(self.objects[tab]))]
        self.array_of_title[14].connect("clicked", lambda cf2: self.change_tex_file(0, "TITLE.tex"))
        self.array_of_title[5].connect("clicked", lambda date_0: self.get_date_from_calendar(reported_id=0))
        self.array_of_title[10].connect("clicked", lambda date_1: self.get_date_from_calendar(reported_id=1))
        self.faculty_title = builder.get_object("facultyBoxTitle")
        self.faculty_title.connect("changed", self.change_department_list)
        self.department_title = builder.get_object("departmentBoxTitle")
        self.department_title.connect("changed", self.change_groups_list)
        self.group_title = builder.get_object("groupBoxTitle")
        """Page 2: "Task"
        """
        tab = 1
        self.array_of_task = [builder.get_object(self.objects[tab][j] + self.tab[tab]) for j in
                              range(len(self.objects[tab]))]
        self.array_of_task[1].connect("clicked", lambda date_2: self.get_date_from_calendar(reported_id=2))
        self.array_of_task[6].connect("clicked", lambda date_3: self.get_date_from_calendar(reported_id=3))
        self.array_of_task[11].connect("clicked", lambda cts: self.create_time_schedule())
        self.array_of_task[12].connect("clicked", lambda date_4: self.get_date_from_calendar(reported_id=4))
        self.array_of_task[13].connect("clicked", lambda date_5: self.get_date_from_calendar(reported_id=5))
        self.array_of_task[14].connect("clicked", lambda cf: self.change_tex_file(1, "TASK.tex"))
        self.faculty_task = builder.get_object("facultyBoxTask")
        self.faculty_task.connect("changed", self.change_department_list)
        self.department_task = builder.get_object("departmentBoxTask")
        self.department_task.connect("changed", self.change_groups_list)
        self.group_task = builder.get_object("groupBoxTask")
        """Page 3: Annotation
        """
        tab = 2
        self.array_of_annotation = [builder.get_object(self.objects[tab][j] + self.tab[tab]) for j in
                                    range(len(self.objects[tab]))]
        self.array_of_annotation[22].connect("clicked", lambda date_6: self.get_date_from_calendar(reported_id=6))
        self.array_of_annotation[23].connect("clicked", lambda cfa: self.change_tex_file(2, "ANNOTATION.tex"))
        """Page 4: Review by recentest
        """
        tab = 3
        self.array_of_recentest = [builder.get_object(self.objects[tab][j] + self.tab[tab]) for j in
                                   range(len(self.objects[tab]))]
        self.array_of_recentest[8].connect("clicked", lambda date_7: self.get_date_from_calendar(reported_id=7))
        self.array_of_recentest[9].connect("clicked", lambda cfr: self.change_tex_file(3, "REVIEW-BY-RECENTEST.tex"))
        self.faculty_recentest = builder.get_object("facultyBoxRecentest")
        self.faculty_recentest.connect("changed", self.change_department_list)
        self.department_recentest = builder.get_object("departmentBoxRecentest")
        self.department_recentest.connect("changed", self.change_groups_list)
        self.group_recentest = builder.get_object("groupBoxRecentest")
        """Page 5: Review by leader
        """
        tab = 4
        self.array_of_leader = [builder.get_object(self.objects[tab][j] + self.tab[tab]) for j in
                                range(len(self.objects[tab]))]
        self.array_of_leader[7].connect("clicked", lambda date_8: self.get_date_from_calendar(reported_id=8))
        self.array_of_leader[8].connect("clicked", lambda clf: self.change_tex_file(4, "REVIEW-BY-LEADER.tex"))
        self.faculty_leader = builder.get_object("facultyBoxLeader")
        self.faculty_leader.connect("changed", self.change_department_list)
        self.department_leader = builder.get_object("departmentBoxLeader")
        self.department_leader.connect("changed", self.change_groups_list)
        self.group_leader = builder.get_object("groupBoxLeader")
        self.window1.show_all()

    @staticmethod
    def get_date_from_calendar(reported_id):
        """

        :param button:
        :return: nothing
        """
        Calendar(reported_id)

    @staticmethod
    def create_time_schedule():
        Schedule()

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
            self.array_of_lists[1].append([i])

        self.department_title.set_model(self.array_of_lists[1])

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
            self.array_of_lists[2].append([i])
        self.group_title.set_model(self.array_of_lists[2])

    def change_department_list(self, combo):
        """

        :param combo:
        :return: nothing
        """
        tree_iter = combo.get_active()
        self.key_iter = tree_iter
        if tree_iter is not None:
            self.array_of_lists[1].clear()
            self.determine_list_store(tree_iter)

    def change_groups_list(self, combo):
        """

        :param combo:
        :return: nothing
        """
        tree_iter = combo.get_active()
        if tree_iter is not None:
            self.array_of_lists[2].clear()
            self.determine_group_store(tree_iter)

    def build_article(self):
        """
        If article not fit on the one line, function will divides it on two through the separation of 76 characters.
        :return first_line_of_article, second_line_of_article:
        """
        article = self.array_of_title[0].get_text()
        article = article.split(" ")
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
        length_of_field = 16
        length_of_line = len(text_field)
        count_of_spaces = 0
        if length_of_line < length_of_field:
            count_of_spaces = int(abs((length_of_field - length_of_line) / 2))
        line = "\\hspace{%sem}" % count_of_spaces + text_field + "\\hspace{%sem}" % count_of_spaces
        return line

    def got_entry_fields(self, page_num):
        """
        Take text from each field of the active Label of the window and interjected it into dictionary

        Issues: Change structure of the method. (!!!)

        :return self.dict_of_fields:
        """
        self.page_num = page_num
        if self.page_num is 0:
            """Page 1: Title
            """
            for i in range(len(self.dict_of_fields)):
                self.dict_of_fields["%s" % list(self.dict_of_fields.keys())[i]] = ''
            if len(self.array_of_title[0].get_text()) > 76:
                self.dict_of_fields["[ARTICLE-1]"] = self.build_article()[0]
                self.dict_of_fields["[ARTICLE-2]"] = self.build_article()[1]
            else:
                self.dict_of_fields["[ARTICLE-1]"] = self.array_of_title[0].get_text()
            for i in range(len(self.objects[self.page_num])):
                if i in [0, 5, 10, 14]:
                    pass
                else:
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.addition_lines_to_text_field(self.array_of_title[i].get_text())
            list_of_keys = list(Calendar.dict_of_dates.keys())
            for current_key in list_of_keys:
                self.dict_of_fields["[%s]" % current_key.upper()] = Calendar.dict_of_dates[current_key]
            self.faculty_model = self.faculty_title.get_model()
            self.dict_of_fields["[FACULTY]"] = self.faculty_model[self.faculty_title.get_active_iter()][0]
            self.department_model = self.department_title.get_model()
            self.dict_of_fields["[DEPARTMENT]"] = self.department_model[self.department_title.get_active_iter()][0]
            self.group_model = self.group_title.get_model()
            self.dict_of_fields["[GROUP]"] = self.group_model[self.group_title.get_active_iter()][0]
            return self.dict_of_fields

        elif self.page_num is 1:
            """Page 2: Task
            """
            for i in range(len(self.dict_of_fields)):
                self.dict_of_fields["%s" % list(self.dict_of_fields.keys())[i]] = ''
            list_of_keys = list(Calendar.dict_of_dates.keys())
            for current_key in list_of_keys:
                self.dict_of_fields["[%s]" % current_key.upper()] = Calendar.dict_of_dates[current_key]
            for i in range(len(self.objects[self.page_num])):
                if i in range(2, 6):
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.addition_lines_to_text_field(self.array_of_task[i].get_text())
                elif i in range(8, 11):
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.array_of_task[i].get_buffer().get_text(self.array_of_task[i].get_buffer().get_start_iter(),
                            self.array_of_task[i].get_buffer().get_end_iter(), True)
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.add_new_line_to_tex(self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()],
                                                 end=0)
                else:
                    pass
            self.dict_of_fields["[TABLE-LINES]"] = Schedule.total_table[0]
            self.faculty_model = self.faculty_task.get_model()
            self.dict_of_fields["[FACULTY]"] = self.faculty_model[self.faculty_task.get_active_iter()][0]
            self.department_model = self.department_task.get_model()
            self.dict_of_fields["[DEPARTMENT]"] = self.department_model[self.department_task.get_active_iter()][0]
            self.group_model = self.group_task.get_model()
            self.dict_of_fields["[GROUP]"] = self.group_model[self.group_task.get_active_iter()][0]
            return self.dict_of_fields

        elif self.page_num is 2:
            """Page 3: Annotation
            """
            for i in range(len(self.dict_of_fields)):
                self.dict_of_fields["%s" % list(self.dict_of_fields.keys())[i]] = ''
            list_of_keys = list(Calendar.dict_of_dates.keys())
            for current_key in list_of_keys:
                self.dict_of_fields["[%s]" % current_key.upper()] = Calendar.dict_of_dates[current_key]
            for i in range(len(self.objects[self.page_num])):
                if i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 20, 21]:
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.addition_lines_to_text_field(self.array_of_annotation[i].get_text())
                elif i in range(16, 20):
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.array_of_annotation[i].get_buffer().get_text(
                            self.array_of_annotation[i].get_buffer().get_start_iter(),
                            self.array_of_annotation[i].get_buffer().get_end_iter(), True)
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.add_new_line_to_tex(self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()],
                                                 end=0)
                else:
                    pass
            return self.dict_of_fields

        elif self.page_num is 3:
            """Page 4: Review by recentest
            """
            for i in range(len(self.dict_of_fields)):
                self.dict_of_fields["%s" % list(self.dict_of_fields.keys())[i]] = ''
            list_of_keys = list(Calendar.dict_of_dates.keys())
            for current_key in list_of_keys:
                self.dict_of_fields["[%s]" % current_key.upper()] = Calendar.dict_of_dates[current_key]
            for i in range(len(self.objects[self.page_num])):
                if i in [0, 1, 2, 3, 6, 7]:
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.addition_lines_to_text_field(self.array_of_recentest[i].get_text())
                elif i in [4, 5]:
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.array_of_recentest[i].get_buffer().get_text(
                            self.array_of_recentest[i].get_buffer().get_start_iter(),
                            self.array_of_recentest[i].get_buffer().get_end_iter(), True)
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.add_new_line_to_tex(self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()],
                                                 end=0)
                else:
                    pass
            self.faculty_model = self.faculty_recentest.get_model()
            self.dict_of_fields["[FACULTY]"] = self.faculty_model[self.faculty_recentest.get_active_iter()][0]
            self.department_model = self.department_recentest.get_model()
            self.dict_of_fields["[DEPARTMENT]"] = self.department_model[self.department_recentest.get_active_iter()][0]
            self.group_model = self.group_recentest.get_model()
            self.dict_of_fields["[GROUP]"] = self.group_model[self.group_recentest.get_active_iter()][0]
            return self.dict_of_fields

        elif self.page_num is 4:
            """Page 5: Review by leader
            """
            for i in range(len(self.dict_of_fields)):
                self.dict_of_fields["%s" % list(self.dict_of_fields.keys())[i]] = ''
            list_of_keys = list(Calendar.dict_of_dates.keys())
            for current_key in list_of_keys:
                self.dict_of_fields["[%s]" % current_key.upper()] = Calendar.dict_of_dates[current_key]
            for i in range(len(self.objects[self.page_num])):
                if i in [0, 1, 2, 3]:
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.addition_lines_to_text_field(self.array_of_leader[i].get_text())
                elif i in [4, 5]:
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.array_of_recentest[i].get_buffer().get_text(
                            self.array_of_leader[i].get_buffer().get_start_iter(),
                            self.array_of_leader[i].get_buffer().get_end_iter(), True)
                    self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()] = \
                        self.dict_of_fields["[%s]" % self.objects[self.page_num][i].upper()]
                else:
                    pass
            self.faculty_model = self.faculty_leader.get_model()
            self.dict_of_fields["[FACULTY]"] = self.faculty_model[self.faculty_leader.get_active_iter()][0]
            self.department_model = self.department_leader.get_model()
            self.dict_of_fields["[DEPARTMENT]"] = self.department_model[self.department_leader.get_active_iter()][0]
            self.group_model = self.group_leader.get_model()
            self.dict_of_fields["[GROUP]"] = self.group_model[self.group_leader.get_active_iter()][0]
            return self.dict_of_fields

    def add_new_line_to_tex(self, line, end):
        """

        :param line:
        :param end:
        :return:
        """
        self.line = line
        length_of_line = 95
        self.length_of_first_line = 0
        if end is 0:
            self.length_of_first_line = 30
        if end in [1, 2]:
            self.length_of_first_line = 40
        if end is 3:
            self.length_of_first_line = 87
        else:
            # Will be changed
            self.length_of_first_line = length_of_line
        self.line_to_slicing = self.line.replace("\n", " ").replace("- ", "")
        self.splitted_line = self.line.replace("\n", " ").replace("- ", "").split(" ")
        self.intermediate_array = []
        remaind_line = ""
        for i in self.splitted_line:
            remaind_line += i
            remaind_line += " "
            if len(remaind_line) <= self.length_of_first_line:
                self.intermediate_array.append(remaind_line)
                self.first_line = self.intermediate_array.pop()
        new_array = []
        start_slice_const = self.length_of_first_line
        end_slice_const = length_of_line
        for i in range(line.count("\n") + 1):
            start_slice = start_slice_const + end_slice_const * i + i
            end_slice = start_slice_const + end_slice_const * (i + 1) + i
            cut_a = len(self.line_to_slicing[start_slice:end_slice].rstrip().split(" ").pop())
            if i > 0:
                start_slice_prev = start_slice_const + end_slice_const * (i - 1) + (i - 1)
                end_slice_prev = end_slice_const + end_slice_const * i + (i - 1)
                cut_s_0 = len(self.line_to_slicing[
                              end_slice_prev - start_slice_prev:start_slice - end_slice_prev].lstrip().rstrip().split(
                    " ").pop())
                new_array.append(self.line_to_slicing[start_slice - cut_s_0:end_slice - cut_a + 1])
            else:
                new_array.append(self.line_to_slicing[start_slice:end_slice - cut_a])
        total_string = """"""
        total_string += "\\underline{%s}\n" % self.first_line
        for i in range(len(new_array)):
            if new_array[i] is not "":
                new_array[i] = "~\\\\~\\\\\\underline{%s}\n" % new_array[i]
                total_string += new_array[i]
        total_string += ("~\\\\~\\\\\\underline{\hspace{63em}}\n" * 2)

        return total_string

    def change_tex_file(self, page_num, file_name):
        """
        Creates a file with widening ".tex" by the addition text and dates from due to text fields.
        :param button:
        :return nothing:
        """
        path = os.getcwd() + "\\samples\\bachelor\\dev\\"
        path_to_files = [path + "title.tex", path + "task.tex", path + "annotation.tex",
                         path + "review_by_recentest.tex",
                         path + "review_by_leader.tex"]
        self.dict_of_fields = self.got_entry_fields(page_num=page_num)
        self.work_file = open("{0}".format(path_to_files[page_num]), "r", encoding="UTF-8")
        self.readed = self.work_file.read()
        self.work_file.close()
        self.work_file = open(file_name, "a", encoding="UTF-8")
        for i in self.dict_of_fields.keys():
            self.readed = self.readed.replace(str(i), str(self.dict_of_fields[i.upper()]))
        self.work_file.write(self.readed)
        self.work_file.close()


class Handlers(object):
    """

    """

    number_of_current_page = 0
    number = 0

    def on_notebook1_switch_page(self, widget, label, page):
        pass