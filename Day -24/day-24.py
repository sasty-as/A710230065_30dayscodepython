class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

employee1 = Employee("sasty", 20, 5000000)
print("Name :", employee1.get_name()) 
print("Age :", employee1.get_age()) 
print("Salary :", employee1.get_salary())

employee1.set_name("azizah")
employee1.set_age(23)
employee1.set_salary(8000000)
print()
print("Name :", employee1.get_name()) 
print("Age :", employee1.get_age()) 
print("Salary :", employee1.get_salary())