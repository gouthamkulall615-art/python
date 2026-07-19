class Employee:

    language = "Py"
    salary = 12000000


"""
adjective->Attribute 
ex: name, language,salry


here name is object(instances) attribute and salary and langauge  are class attributes as  directly belong to the class


instance attribute is given more prefrence over the class attributes
"""

# goutham is an object for the  class Employee
goutham = Employee()
goutham.name = "Goutham"
print(goutham.name, goutham.language)

preetham = Employee()
preetham.name = "Preetham"
print(preetham.name, preetham.language)
