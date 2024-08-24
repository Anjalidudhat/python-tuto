class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
        

my_car = car("Toyato", "Germany", 2000)
my_car.display_info()




#inheritance

class ElectricCar(car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_battery(self):
        print(f"Battery size: {self.battery_size} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
my_electric_car.display_info()
my_electric_car.display_battery()



#Polymorphism

class Animal:
    def make_sound(self):
         raise NotImplementedError
    
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()



#Encapsulation

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())


#Abstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!"
    
dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())