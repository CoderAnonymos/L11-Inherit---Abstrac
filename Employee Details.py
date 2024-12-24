class Person(object):

    def __init__(self, name, idNumber):

        self.name = name
        self.idNumber = idNumber

    def display(self):

        print(self.name)
        print(self.idNumber)


class Employee(Person):

    def __init__(self, name, idNumber, salary, post):

        self.salary = salary
        self.post = post

        Person.__init__(self, name, idNumber)


a = Employee("Penguin", 2023142, 800000, "CEO")
a.display()