class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    @property
    def name(self):
        return self.ename

e = Employee()

e.a = 45
e.name="Goutham"
print(e.name)
e.show()
