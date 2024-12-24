class Person:

    def __init__(self, fname, lname):

        self.firstname = fname
        self.lastname = lname

    def printName(self):

        print(self.firstname, self.lastname)


class Student(Person):
    
    def __init__(self, fname, lname, year):
        
        super().__init__(fname, lname)

        self.graduationYear = year


student = Student("Olaide", "Adepoju", 2024)

student.printName()
print(student.graduationYear)