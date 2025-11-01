# Most Asked Python Questions with Answers:  

-- Todo all the basics of the questions have been copied to a sheet we have to transport them here we will do it later 

## Functions & OOPS

### What is inheritance and its types in Python?

- Inheritance in Python is an object-oriented programming (OOP) concept that allows one class (child or subclass) to derive properties and methods from another class (parent or base class).

**Single Inheritance**
- A child class inherits from one parent class

```py
class A:
    def featureA(self):
        print("Feature A")

class B(A):
    def featureB(self):
        print("Feature B")

```

**Multiple Inheritance**
- A child class inherits from more than one parent class.

```py
class A:
    def featureA(self):
        print("Feature A")

class B:
    def featureB(self):
        print("Feature B")

class C(A, B):
    def featureC(self):
        print("Feature C")

```


**Multilevel Inheritance**
- A child class inherits from a parent, and another class inherits from that child (a chain).

```py
class A:
    def featureA(self):
        print("Feature A")

class B(A):
    def featureB(self):
        print("Feature B")

class C(B):
    def featureC(self):
        print("Feature C")

```

### What is encapsulation in Python?

- Encapsulation in Python is an object-oriented programming (OOP) principle that refers to bundling data (variables) and methods (functions) that operate on that data into a single unit — a class.

-> data protection and controlled access

| Modifier      | Syntax  | Access Level                                               | Example         |
| ------------- | ------- | ---------------------------------------------------------- | --------------- |
| **Public**    | `var`   | Accessible everywhere                                      | `self.name`     |
| **Protected** | `_var`  | Should be accessed only within class/subclass (convention) | `self._salary`  |
| **Private**   | `__var` | Name-mangled to prevent direct access                      | `self.__salary` |

```py
class Student:
    def __init__(self):
        self.name = "John"       # public
        self._age = 20           # protected
        self.__marks = 90        # private

obj = Student()
print(obj.name)        # ✅ Allowed
print(obj._age)        # ⚠️ Technically allowed, but discouraged
# print(obj.__marks)   # ❌ Not allowed

# Access private variable using name mangling
print(obj._Student__marks)  # ✅ Works but not recommended

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    @property
    def balance(self):
        """Getter method — read access to private variable"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter method — write access with validation"""
        if amount >= 0:
            self.__balance = amount
        else:
            print("❌ Balance cannot be negative!")

    @balance.deleter
    def balance(self):
        """Deleter method — controlled deletion"""
        print("Deleting balance...")
        del self.__balance

```



### What is abstraction and how can you implement it in Python?

- using abc module import ABC , abstractmethod

```py
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape"""

class Circle(Shape):
    def __init__(self, r: float):
        self.r = r
    def area(self) -> float:
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h
    def area(self) -> float:
        return self.w * self.h

shapes = [Circle(1.0), Rectangle(2.0, 3.0)]
for s in shapes:
    print(type(s).__name__, "area =", s.area())

```

### What are magic methods in Python? Give examples.

Magic methods (also known as dunder methods, short for double underscore methods) are special predefined methods in Python that begin and end with double underscores — like __init__, __str__, or __add__.

| Magic Method  | Purpose                          | Example                           |
| ------------- | -------------------------------- | --------------------------------- |
| `__init__`    | Object initializer (constructor) | Called when an object is created  |
| `__str__`     | String representation            | Called by `str()` or `print()`    |
| `__repr__`    | Developer representation         | Called by `repr()` or in the REPL |
| `__add__`     | Addition operator (`+`)          | Defines custom addition           |
| `__len__`     | Length of object                 | Called by `len()`                 |
| `__getitem__` | Index access                     | Enables `obj[key]` syntax         |
| `__setitem__` | Assigning with index             | Enables `obj[key] = value`        |
| `__delitem__` | Deleting with index              | Enables `del obj[key]`            |
| `__eq__`      | Equality comparison (`==`)       | Defines equality behavior         |
| `__lt__`      | Less than comparison (`<`)       | Defines comparison                |
| `__iter__`    | Iteration protocol               | Makes object iterable             |
| `__next__`    | Next item in iteration           | Works with loops and iterators    |


### Explain __str__ vs __repr__. ? 

__str__ — User-Friendly Representation

Purpose: To return a readable, nicely formatted string for end users.

```py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

book = Book("1984", "George Orwell")
print(book)         # Uses __str__
print(str(book))    # Uses __str__

```

🔹 __repr__ — Developer/Debug Representation

Purpose: To return a precise and unambiguous string that can help developers understand the object (ideally, a string that could be used to recreate the object).

```py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book = Book("1984", "George Orwell")
print(repr(book))   # Uses __repr__

```

| Aspect      | `__str__`                                       | `__repr__`                  |
| ----------- | ----------------------------------------------- | --------------------------- |
| Purpose     | User-friendly display                           | Developer/debug display     |
| Used by     | `print()`, `str()`                              | `repr()`, interactive shell |
| Readability | Focuses on clarity                              | Focuses on precision        |
| Fallback    | If `__str__` is missing, Python uses `__repr__` | No fallback to `__str__`    |
