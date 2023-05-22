from abc import ABC
import math

class Shape(ABC):
    def __init__(self,sides):
        self.sides = sides

    def Compute_Area(self):
        pass

class Triangle(Shape):
    def __init__(self,sides,base,height):
        super().__init__(sides)
        self.base = base
        self.height = height

    def Compute_Area(self):
        return 1/2 * self.base * self.height

class Circle(Shape):
    def __init__(self,sides,radius):
        super().__init__(sides)
        self.radius = radius

    def Compute_Area(self):
        return math.pi * self.radius ** 2

def main():
    t = Triangle(3, 8, 6)
    print(t.Compute_Area())

    c = Circle(0, 4)
    print(c.Compute_Area())
main()


class Employee:
    def __init__(self,emp_name,emp_id,salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = salary

    def salary_status(self):
        print(self.emp_name,self.emp_id,self.salary)


class Building_Manager(Employee):
    def __init__(self,emp_name,emp_id):
        super().__init__(emp_name,emp_id,10000)


class Procurement_Manager(Employee):
    def __init__(self,emp_name,emp_id):
        super().__init__(emp_name, emp_id,12000)


class Logistics_Manager(Employee):
    def __init__(self,emp_name,emp_id):
        super().__init__(emp_name, emp_id,15000)


def main():
    employees = [Building_Manager("talha", "1"),Procurement_Manager("Ali", "2"),Logistics_Manager("Ahmed", "3")]
    for employee in employees:
        employee.salary_status()

main()
