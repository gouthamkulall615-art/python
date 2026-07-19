class Employee:

    language = "Py"
    salary = 12000000

    def __init__(
        self, name, salary, language
    ):  # dunder method which is automatically called when the object is created
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"the language is {self.language} and salary is {self.salary}")

    def greet(self):
        print("Good Morning")


# goutham is an object for the  class Employee
goutham = Employee("Harry", 130000, "JavaScript")
print(goutham.name, goutham.salary, goutham.language)
# goutham.name = "Goutham"
# goutham.getInfo()
# goutham.greet()
