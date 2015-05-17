import os

import GUI


class ParserLaTexFile():

    workDirectory = os.getcwd()
    workFilePath = workDirectory + "\\test.txt"

    def __init__(self):
        print("Entered parser")
        self.changeFile()

    def changeFile(self):
        self.file = open(self.workFilePath, "r", encoding="utf8")
        self.readed = self.file.read()
        print(self.readed)
        print(len(self.readed))

        print(self.changeAuthor(GUI.bachelors.BachelorsWindow().gotEntryFields()))
        '''self.changeDirection(BachelorsWindow().gotDirPrep)
        self.changeChef(BachelorsWindow().gotChef)
        self.changeDate(BachelorsWindow().getDateFromTempFile()[0], BachelorsWindow().getDateFromTempFile()[1],
                        BachelorsWindow().getDateFromTempFile()[2])'''

    def changeAuthor(self, author):
        self.readed.replace("[AUTHOR]", author)
        print(self.readed)

    def changeDirection(self, direction):
        self.readed.replace("[DIRECTION]", direction)

    def changeChef(self, chef):
        self.readed.replace("[CHEF]", chef)

    def changeDate(self, year, month, day):
        self.readed.replace("[YEAR]", year)
        self.readed.replace("[MONTH]", month)
        self.readed.replace("[DAY]", day)
