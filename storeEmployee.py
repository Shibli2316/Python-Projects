from turtle import position
from unicodedata import name


class Employee:
    count = 0
    def __init__(self, name, position, salary):
        self.name=name
        self.position=position
        self.salary=salary
        Employee.count+=1

    def displayCount(self):
        print(f"There are {Employee.count} employees")

    def displayDeatails(self):
        print("Name: ", self.name, ", Position: ", self.position, ", Salary: ", self.salary)

emp1=Employee("Employee1", "HR", 30000)
emp2=Employee("Employee2", "Manager", 3000)
emp3=Employee("Employee3", "Programmer", 3000)
emp4=Employee("Employee4", "HRS", 30000)

emp4.displayCount()

print("Information about Employees")
emp1.displayDeatails()
emp2.displayDeatails()
emp3.displayDeatails()
emp4.displayDeatails()