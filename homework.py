# პირველი დავალება
class Calculator:
    
    def sum(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a-b
    
    def divide(self, a, b):
        return a / b
    
    def multiply(self, a, b):
        return a * b
    
calculator = Calculator()
print(calculator.sum(5, 10))
print(calculator.subtract(5, 10))
print(calculator.divide(5, 10))
print(calculator.multiply(5, 10))

print("-----------------------------------------")

# მეორე დავალება
class Rectangle:
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return self.width * 2 + self.length * 2
    
    def print_info(self):
        print(f"width = {self.width}, length = {self.length}\narea = {self.area()}, perimeter = {self.perimeter()}")
    
rectangle = Rectangle(15, 10)
rectangle.print_info()

#

print("-----------------------------------------")

# მესამე დავალება

class Employee:
    
    def __init__(self, name, surname, age, salary):
        self.name = name;
        self.surname = surname;
        self.age = age;
        self.salary = salary;
    
import csv

employee_data = []

with open('dataset1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        name = row[0]
        surname = row[1]
        age = row[2]
        salary = row[3]
           
        employee = Employee(name, surname, age, salary)
        employee_data.append(employee)

smallest_salary_owner = min(employee_data, key = lambda e : e.salary)
print(f"{smallest_salary_owner.name} {smallest_salary_owner.surname} has the smallest salary: {smallest_salary_owner.salary}")

oldest_employee = max(employee_data, key = lambda e : e.age)
print(f"Oldest Employee is {oldest_employee.name} {oldest_employee.surname}, who is {oldest_employee.age} years old")
