class Person:

    # Constructor
    def __init__(self, name):
        self.name = name

        # To get name

    def get_name(self):
        return self.name

        # To check if this person is an employee

    def is_employee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def is_employee(self):
        return True


# Driver code
emp = Person("John")  # An Object of Person
print(emp.get_name(), emp.is_employee())

emp = Employee("Jacob")  # An Object of Employee
print(emp.get_name(), emp.is_employee())


# Multiple Inheritance


class PersonMulti:
    # defining constructor
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

        # defining class methods

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


# defining another class
class Student:
    def __init__(self, student_id):
        self.student_id = student_id

    def get_id(self):
        return self.student_id


class Resident(PersonMulti, Student):  # extends both Person and Student class
    def __init__(self, name, age, id):
        PersonMulti.__init__(self, name, age)
        Student.__init__(self, id)

    # Create an object of the subclass


resident1 = Resident('John', 30, '102')
resident1.show_name()
print(resident1.get_id())