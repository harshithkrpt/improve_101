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


### What is method overriding and overloading?

- overriding (When a child class defines a method with the same name, parameters, and return type as a method in its parent class, it overrides the parent’s method.)

ex: 

```py
class Parent:
    def __init__(self):
        pass
    def thoughts(self):
        print("Parents ask everything")

class Child(Parent):
    def __init__(self):
        pass
    def thoughts(self):
        print("Why parents care too much man !!!")

```

- method overloading 
- same function name but different number of arguments 
- but python does not support method overloading 

```py
class MathOps:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):   # Replaces the previous definition
        return a + b + c

obj = MathOps()
print(obj.add(2, 3))  # ❌ Error: missing 1 required positional argument

```

### What are dataclasses in Python ?

- python feature in 3.7 which automatically handles data storing + few dunder methods like repr , __eq__ , __repr__ ...

__init__() → Initializes fields

__repr__() → Returns readable string representation

__eq__() → Compares objects by value

```py
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    email: str

```

### What are metaclasses in python ?

A metaclass in Python is essentially the “class of a class.”
Similarly, every class itself is also an object, created by another class — and that creator class is called a metaclass.

```py
# Define a metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        dct['created_by_meta'] = True
        return super().__new__(cls, name, bases, dct)

# Use it to create a class
class MyClass(metaclass=MyMeta):
    pass

print(MyClass.created_by_meta)  # True

```

### Difference between arguments and parameters ?

- 1. Parameters → in function definition

```py
def greet(param):
    print(f"Hello, {param}!")
``

- 2. Arguments → in function call

```py
greet("Alice")
```

| Term          | Appears In          | Role                 |
| ------------- | ------------------- | -------------------- |
| **Parameter** | Function definition | Placeholder variable |
| **Argument**  | Function call       | Actual value passed  |


### What are *args and **kwargs?

1. *args → Non-keyword variable arguments. Collects positional arguments (those without names).
- The * means “pack all extra positional arguments into a tuple.”

```py
def add_numbers(*args):
    print(args)
    return sum(args)

print(add_numbers(2, 3, 5))  # Output: (2, 3, 5) → sum = 10

```

2. **kwargs → Keyword variable arguments

Collects named (keyword) arguments into a dictionary.
The ** means “pack all extra keyword arguments into a dict.”

```py
def show_details(**kwargs):
    print(kwargs)

show_details(name='harshith',age=26)
```

| Syntax     | Collects        | Data Type | Example Input | Stored As        |
| ---------- | --------------- | --------- | ------------- | ---------------- |
| `*args`    | Positional args | Tuple     | `f(1, 2, 3)`  | `(1, 2, 3)`      |
| `**kwargs` | Keyword args    | Dict      | `f(a=1, b=2)` | `{'a':1, 'b':2}` |


### What are default arguments?

Default arguments in Python are parameters that take a predefined value if no argument is provided during a function call.

```py
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet("Alice")   # Output: Hello, Alice!
greet()          # Output: Hello, Guest!

```


Important rule:

Default parameters must come after non-default ones.

❌ Wrong:

```py
def func(a=1, b):  # Error!
    pass

```
✅ Correct:
```py
def func(a, b=1):
    pass

```

### What are anonymous (lambda) functions?

Anonymous functions, also known as lambda functions, are small, unnamed functions in Python — created using the keyword lambda instead of the regular def.

lambda arguments: expression

```py
square = lambda x: x ** 2
square(4)

```
- map, filter, and sorted

```py
numbers = [1,2,3,4]
print(list(map(lambda n: n ** 2, numbers)))
print(list(filter(lambda n: n % 2 == 0, numbers)))

data = [(1, 'b'), (3, 'a'), (2, 'c')]
data.sort(key=lambda x: x[1])
```

### What are higher-order functions?

A higher-order function (HOF) is a function that either:
Takes another function as an argument, or
Returns a function as its result.

```py
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func, message):
    print(func(message))

speak(shout, "hello world")   # HELLO WORLD
speak(whisper, "HELLO WORLD") # hello world

```

- function returns another function

```py
def greet(name):
    def message():
        return f"Hello, {name}!"
    return message

say_hi = greet("Alice")
print(say_hi())  # Hello, Alice!

```

### What is recursion and how does Python handle it?

Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem.

A recursive function always has:

A base case — the condition that stops recursion.

A recursive case — where the function calls itself.

```py
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:                  # recursive case
        return n * factorial(n - 1)

print(factorial(5))  # 120

```

- recursion for every call stores in new call stack once base case is reached it starks poping from stack and return result . below example show how we can increase the recursion limit by 2000 from default of 1000

```py
import sys
print(sys.getrecursionlimit())  # usually 1000

sys.setrecursionlimit(2000)  # not recommended unless needed
```


### What is the super() function?

In Python, the super() function is used to call a method from the parent (or superclass) inside a child (or subclass).
```py
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()   # Call Parent’s greet method
        print("Hello from Child")

c = Child()
c.greet()

```