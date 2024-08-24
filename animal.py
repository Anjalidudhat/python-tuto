#class method

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return f"{self.name} says Hello!"
    
dog = Animal("cat")
print(dog.speak())


# sub class method(inheritance)

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return f"{self.name} say hello!"
    
class dog:
    def speak(self):
        return f"{self.name} barks!"
    pass
dog = Animal("rabit")
print(dog.speak())


# using super function()

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"
    

class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name)
        self.bread = bread

dog = Dog("charlin", "bulldog")
print(dog.bread)


#creating property

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

circle = Circle(5)
print(circle.radius)
circle.radius = 10
print(circle.radius)


# Encapsulation

class MyClass:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self._private = "private"

obj = MyClass()
print(obj.public)
print(obj._protected)
print(obj._private)


# Polymorphism – Using Inbuilt Abstract Base Classes (ABC)

from collections.abc import Iterable

def get_length(item):
    if isinstance(item, Iterable):
       return len(item)
    else:
        return "Not iterable"
    
print(get_length("Hello"))
print(get_length([1,2,3]))
print(get_length(123))


# Defining an Abstract Base Class (ABC)

from abc import ABC, abstractmethod

class AbstracAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AbstracAnimal):
    def speak(self):
        return "Boww Boww!"

dog = Dog()
print(dog.speak())    



#  Using class methods and static methods


class MyClass:
    @classmethod    
    def class_method(cls):
        return "Class method called"
    
    @staticmethod
    def static_method():
        return "Static method called"
    

print(MyClass.class_method())
print(MyClass.static_method())


# Operator Overloading in Python

class Mango:
    def __init__(self,x):
        self.x = str(x)
    def __add__(self,y):
        return self.x + y.x
obj1 = Mango(7)
obj2 = Mango('mangoes')
print(obj1+obj2)


# Using Special methods for string representations (repr and str)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', is {self.age})"
    
p = Person("BOB", 30)
print(str(p))
print(repr(p))   


# Using composition in Python OOP

class Salary:
    def __init__(self, pay, bouns):
        self.pay = pay
        self.bouns = bouns

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

s = Salary(15000, 20000)
e = Employee("Anjali", s)
print(e.salary.pay)

# Using multiple inheritance

class Parent1:
    def method1(self):
        return "Parent's method called"

class Parent2:
    def method2(self):
        return "Parent's mathod called"

class child(Parent1, Parent2):
    pass


c = child()
print(c.method1())
print(c.method2())


#  Implementing Decorators within classes
class MyClass:
    @staticmethod
    def method():
        return "Static method called"

    @classmethod
    def classmethod(cls):
        return "Class method called"

print(MyClass.method())
print(MyClass.classmethod())

#Creating a Singleton class in Python

class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance
    
    def __init__(self):
        if  Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self

s = Singleton.getInstance()
print(s)

# Using Mixin classes in Python
        
class Mixin1(object):
    def test(self):
        print(Mixin1)

class Mixin2(object):
    def test(self):
        print(Mixin2)

class MyClass(Mixin1,Mixin2):
    pass

obj = MyClass()
obj.test()