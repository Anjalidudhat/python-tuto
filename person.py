class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("anjali", 24)
print(p1.name)
print(p1.age)



#string

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("anjali", 24)



#object

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
       
p1 = Person("anjali", 24)
p1.myfunc()


#inheritance

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Anjali", "dudhat")
x.printname()
           