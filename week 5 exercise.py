# exercise 1:

# create a BankAccount class that uses a private
# balance and methods deposits, withdrawing, and
# checking balance

print("\nCreating BankAccount class:\n")

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid value")

    def check_balance(self):
        return self.__balance

# Example usage:
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(f"Current balance: {account.check_balance()}")

# question 1: which OOP concept is shown by making
# the balance private and accessing it through
# such methods?

# answer: Encapsulation

# question 2: why is it important to keep the
# balance private instead of letting users change 
# it directly?

# answer: protects the security and privacy of the 
# data by preventing unauthorized access and 
# modifications, ensuring that all changes go 
# through controlled methods.

# question 3: if you wanted to add interest
# calculation, how would you extend this class
# while still following OOP principles?

# answer: create a new class SavingsAccount that inherits
# from BankAccount and adds an interest rate attribute
# and a method to add interest to the balance.

print("\nExtending BankAccount with SavingsAccount:\n")

class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0, interest_rate=0, years=0):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate
        self.years = years
    
    def apply_interest(self):
        interest = self.check_balance() * (1 + (self.interest_rate / 12)) ** self.years - self.check_balance()
        self.deposit(interest)
        print(f"Applied interest: {interest}")

# Example usage:
savings = SavingsAccount(100, 0.1, 12)
savings.apply_interest()
print(f"Savings balance after interest: {savings.check_balance()}")

#####################

# exercise 2:

# Create classes for Person, Teacher, and Student, 
# and a School class that that holds them in a list

print("\nCreating Person, Teacher, Student, and School classes:\n")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"Teacher: {super().__str__()}, Subject: {self.subject}"
    
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f"Student: {super().__str__()}, Grade: {self.grade}"
    
class School:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def list_people(self):
        for person in self.people:
            print(person)

# Example usage:
school = School()
teacher1 = Teacher("Mr. Morgan", 40, "English")
teacher2 = Teacher("Ms. Intan", 35, "Bahasa Indonesia")
student = Student("Jane Doe", 14, "9th Grade")
school.add_person(teacher1)
school.add_person(teacher2)
school.add_person(student)
school.list_people()

# question 1: what OOP concept is used when Student
# and Teacher inherit from Person?

# answer: Inheritance

# question 2: what concept is shown by the Student
# class containing a list of Person objects?

# answer: Composition

# question 3: if the school had a "Club" that includes
# boh students and teachers, how would you reuse
# existing classes to build it?

# answer: create a Club class that contains a list
# of Person objects, allowing both Student and Teacher
# instances to be added to the club.

print("\nCreating Club class:\n")

class Club:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def list_members(self):
        print(f"Club: {self.name}")
        for member in self.members:
            print(member)

# Example usage:
club = Club("Nippon Club")
club.add_member(teacher1)
club.add_member(teacher2)
club.add_member(student)
club.list_members()

#####################

# exercise 3:

# make a base class Shape and subclass Circle and 
# Rectangle that overrides the area() method

print("\nCreating Shape, Circle, Rectangle, and Triangle classes:\n")

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return round(math.pi * self.radius ** 2, 3)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        if self.width < 0 or self.height < 0:
            return "Invalid dimensions"
        else:
            return self.width * self.height
        
# Example usage:
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")

# question 1: what OOP concept allows Circle and 
# Rectangle to provide their own version of area()?

# answer: polymorphism

# question 2: why did we use a parent class Shape
# instead of just creating Circle and Rectangle?

# answer: it provides a common interface and allows
# for polymorphism

# question 3: if we added a Triangle class, how 
# could we make it fit easily into the same structure?

# answer: add a new Triangle class that inherits
# from Shape and implements its own area() method.

print("\nAdding Triangle class:\n")

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        if self.base < 0 or self.height < 0:
            return "Invalid dimensions"
        else:
            return 0.5 * self.base * self.height
        
# Example usage:
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 7)]
for shape in shapes:
    print(f"Area: {shape.area()}")