class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Coder:
    language = "Python"

    def printLanguages(self):
        print(f"Out of all the languages, here is your language: {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good at {self.language}")


b = Programmer("Harry", 50000)

b.show()
b.printLanguages()
b.showLanguage()