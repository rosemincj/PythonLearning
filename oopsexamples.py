# A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Sample Method

    def say_hi(self):
        print('Hello, my name is', self.name)
        print('And I am', self.age)


# Creating different objects


p1 = Person('Adam', '21')
p2 = Person('John', '22')
p3 = Person('Joe', '23')

p1.say_hi()
p2.say_hi()
p3.say_hi()


class Parrot:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
# Output: <function Parrot.sing>
print(Parrot.sing)

