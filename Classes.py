class Student:
    def __init__(self, first_name, last_name, GPA, Major, grade_level):
        self.first_name = first_name
        self.last_name = last_name
        self.GPA = GPA
        self.Major = Major
        self.grade_level = grade_level

    def study(self):
        print()
        print(self.first_name + " " + self.last_name + " is studying!")

    def eatLunch(self):
        print()
        print(self.first_name + " " + self.last_name + " is eating lunch.")

    def getAll(self):
        print()
        print("First name: " + self.first_name + "\n" + "Last name: " + self.last_name + "\n" + "Major: " +
              self.Major + "\n" + "Grade level: " + self.grade_level + "\n" + "GPA: " + str(self.GPA))


class Faculty:
    def __init__(self, first_name, last_name, teachingClass, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.teachingClass = teachingClass
        self.gender = gender

    def getAll(self):
        print()
        print("First name: " + self.first_name + "\n" + "Last name: " + self.last_name + "\n" + "Class: " +
              self.teachingClass + "\n" + "Gender: " + self.gender)
