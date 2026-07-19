class Employee:

    language = "Py"
    salary = 12000000

    def getInfo(self):
        print(f"the language is {self.language} and salary is {self.salary}")

    def greet(self):
        print("Good Morning")


# goutham is an object for the  class Employee
goutham = Employee()
goutham.name = "Goutham"
goutham.getInfo()
goutham.greet()
