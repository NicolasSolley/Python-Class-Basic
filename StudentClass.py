from Classes import Student
from Classes import Faculty

student1 = Student("Nick", "Solley", 3.0, "IT", "Junior")
student2 = Student("John", "Smith", 3.2, "Business", "Freshman")
student1.study()
student2.study()
student1.eatLunch()
print()
student2.getAll()

faculty1 = Faculty("Jonah", "Smith", "Calculus II", "Male")
faculty1.getAll()

