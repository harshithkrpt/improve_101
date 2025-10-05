class Encapsulation:
    def __init__(self):
        self.__private = "name"


    def get_private(self):
        return self.__private

    def set_private(self, private):
        self.__private = private


enc = Encapsulation()
print(enc.get_private())    
enc.set_private("New Secret")
print(enc.get_private())

class Interntance:
    def first_method(self):
        print("Method 1")

class Interntance2(Interntance):
    def second_method(self):
        print("Method 2")

ins = Interntance2()
ins.first_method()
ins.second_method()


# Polymorphism

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("dog is woff!")

class Cat(Animal):
    def speak(self):
        print("cat is meow!")

for pet in [Dog(), Cat()]:
    pet.speak()

# 4. Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

class Square(Shape):
    def __init__(self, w): self.w = w
    def area(self): return self.w ** 2

cir = Circle(10)
squ = Square(10)

print(cir.area())
print(squ.area())