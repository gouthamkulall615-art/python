class Employee:

    language = "Py"
    salary = 12000000

    # self refers to the current object and lets us access its data.
    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    # @staticmethod is used when a method doesn't need the object's data.
    @staticmethod
    def greet():
        print("Good Morning")


# Creating an object (instance) of the Employee class.
goutham = Employee()

# Creating an instance variable for this object.
goutham.name = "Goutham"

goutham.getInfo()
goutham.greet()