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
```

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


### What is a module in Python?

A module in Python is simply a file that contains Python code — it can define functions, classes, and variables, and can also include runnable code.


```py
# my_module.py
def greet(name):
    return f"Hello, {name}!"
```


Key Points

Purpose: Modules help you organize code logically and reuse it across multiple programs.

Types:

Built-in modules: Provided by Python (e.g., math, os, sys).

User-defined modules: Created by you.

Third-party modules: Installed using pip (e.g., requests, numpy).

Importing modules:

import module_name

from module_name import function_name

import module_name as alias

### What is the difference between a module and a package?


🧩 Module -> A module is just a single Python file (.py) that contains code — functions, classes, or variables.
📦 Package -> A package is a collection of modules organized in a directory. It must contain a special file named __init__.py 

```md
my_package/
│
├── __init__.py
├── math_utils.py
└── string_utils.py
```

### How does Python locate modules?

- Current directory (the script’s folder)
- Directories listed in sys.path or Any directories listed in the PYTHONPATH environment variable.
- build in modules

```py
ModuleNotFoundError: No module named 'my_module'
```

### What is the use of __init__.py?

- it is required for creation a package 
- Without it, Python treats the folder as a normal directory (not importable as a package).
- When a package is imported, the code inside __init__.py runs automatically.


### What is the difference between import and from-import?

- Both import and from ... import are used to bring external code (modules or functions) into your Python program — but they differ in how you access that code. 

- This imports the entire module. (Import)

```py
import math
print(math.sqrt(25))
```

- This imports specific attributes (functions, classes, or variables) directly from a module. (From Import)

```py
from math import sqrt
print(sqrt(25))
```

| Feature           | `import module` | `from module import name` |
| ----------------- | --------------- | ------------------------- |
| What it imports   | Entire module   | Specific names            |
| Access syntax     | `module.name`   | `name` directly           |
| Namespace clarity | Clear           | Can cause conflicts       |
| Typical use       | Larger modules  | Using specific functions  |


### Explain the concept of virtual environments in Python ?

- A virtual environment in Python is an isolated workspace that lets you manage dependencies for a specific project — without interfering with other projects or your system-wide Python installation.

```sh
# creating
python -m venv venv
# activating
source venv/bin/activate
```

### What is a closure in Python?

- A closure in Python is a function that remembers and has access to variables from its enclosing scope, even after that scope has finished executing.

```py
def outer_function(x):
    def inner_function(y):
        return x + y  # inner function uses x from outer scope
    return inner_function  # returning the inner function (not calling it)

add_five = outer_function(5)
print(add_five(10))  # Output: 15
```

### What are decorators in Python and when to use them?

- decorators are the function which will enhance or modify the function behaviour before or after the function call

```py
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")


say_hello()


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

```

### What is a generator? How is it different from a normal function?
 
- generator is a function which will return one value at a time when calling next, It uses the yield keyword instead of return. Each time the function yields a value, it pauses its state — and can resume from where it left off when called again.

```py
def nums():
    for i in range(1,6):
        yield i
nums_g = nums()
print(nums_g)
print(next(nums_g))
```

### What is a context manager?

- object that manages setup and cleanup actions often used with the "with" keyword

```py
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
```

A context manager defines two special methods:


| Method        | Purpose                                   |
| ------------- | ----------------------------------------- |
| `__enter__()` | Runs when the `with` block starts         |
| `__exit__()`  | Runs when the `with` block ends (cleanup) |


```py
class MyContext:
    def __enter__(self):
        print("Entering context...")
        return "Resource Ready"
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context...")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # suppresses the exception if True

with MyContext() as val:
    print(val)
    raise ValueError("Something went wrong!")
```

- custom contextlib we can create the managers using generators

```py
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering...")
    yield "Resource"
    print("Exiting...")

with my_context() as res:
    print(res)
```

### What is the Global Interpreter Lock (GIL)?

- gil is a thread safety mechanism for metex locking ofter helps in avoiding race conditions 
- it helps in multithreading to lock simillarly accessed varaibles to wait until a resource is keeping it on hold

Impact on performance

Single-threaded programs: No problem — the GIL doesn’t affect performance much.

Multi-threaded CPU-bound programs: Bad news. Even with multiple cores, Python threads can’t execute in true parallel. They’ll take turns running.

Multi-threaded I/O-bound programs: Fine. While one thread waits for I/O (network, file, etc.), another can use the GIL.


### What is the difference between threading and asyncio?

- The difference between threading and asyncio in Python lies in how they handle concurrency — that is, running multiple tasks seemingly at the same time.

| Aspect                 | **Threading**                                                          | **Asyncio**                                     |
| ---------------------- | ---------------------------------------------------------------------- | ----------------------------------------------- |
| **Type**               | Multi-threaded concurrency                                             | Single-threaded, asynchronous concurrency       |
| **Concurrency model**  | Uses **operating system threads**                                      | Uses an **event loop** and **coroutines**       |
| **Parallel execution** | Threads can run truly in parallel (but limited by GIL for Python code) | Tasks take turns cooperatively — no parallelism |
| **Control**            | Preemptive — OS decides when to switch threads                         | Cooperative — tasks yield control using `await` |
| **Best for**           | I/O-bound tasks with blocking APIs                                     | I/O-bound tasks with async-compatible APIs      |


```py
import threading
import time

def task(name):
    print(f"{name} Starting")
    time.sleep(2)
    print(f"{name} ending")

threads = [threading.Thread(target=task, args=(f"Thread {i}",)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()
```

- async io

```py
import asyncio
async def task(name):
    print(f"{name} starting")
    await asyncio.sleep(2)
    print(f"{name} ending")

async def main():
    await asyncio.gather(task("Task 1"), task("Task 2"), task("Task 3"))

asyncio.run(main())
```

In short:
Threading is concurrent via multiple threads (but limited by the GIL),
Asyncio is concurrent via cooperative multitasking in one thread.

### What are coroutines in Python?

- provide a way for pause and resume of async and cooperative multitasking within a single thread
- it is a non blocking i/o 

```py
import asyncio

async def greet():
    print("Hello...")
    await asyncio.sleep(2)
    print("...World!")

asyncio.run(greet())

```

explanation:
async def defines a coroutine.
await tells Python: “Pause here until this async task completes.”
The event loop (asyncio.run) manages these pauses efficiently.

### What is the difference between __iter__() and __next__()?

| Method       | Purpose                                         | Used by                                                             |
| ------------ | ----------------------------------------------- | ------------------------------------------------------------------- |
| `__iter__()` | Returns an **iterator object** (usually `self`) | Called when iteration starts (e.g., by `iter(obj)` or a `for` loop) |
| `__next__()` | Returns the **next item** in the sequence       | Called repeatedly by the iterator until it raises `StopIteration`   |


### What is a generator expression?

A generator expression in Python is a compact way to create a generator — that is, an iterator that yields items one at a time without storing them all in memory.

```py
squares = (x*x for x in range(5))
print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4
```

### How are exceptions handled in Python?

```py
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Division by zero not allowed.")
except ValueError:
    print("That wasn’t a number.")

try:
    risky = 10 / int("x")
except (ZeroDivisionError, ValueError) as e:
    print("Error:", e)

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("No error, result:", result)
finally:
    print("This runs no matter what.")

class NegativeNumberError(Exception):
    pass

def check(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers not allowed!")

try:
    check(-10)
except NegativeNumberError as e:
    print("Custom error caught:", e)

```

### What is the difference between Exception and Error?

```py
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    ├── OverflowError
      │    └── FloatingPointError
      ├── ImportError
      ├── IndexError
      ├── KeyError
      ├── ValueError
      ├── TypeError
      ├── ...

```
| Aspect           | **Exception**                                      | **Error**                                                 |
| ---------------- | -------------------------------------------------- | --------------------------------------------------------- |
| **Meaning**      | Any unusual event during program execution         | A subclass of Exception representing a *fault*            |
| **Parent class** | `BaseException` → `Exception`                      | `Exception` (and its subclasses ending in “Error”)        |
| **Examples**     | `StopIteration`, `KeyboardInterrupt`, `SystemExit` | `ValueError`, `TypeError`, `IOError`, `ZeroDivisionError` |
| **Usage**        | Used for both control flow and error handling      | Used specifically for reporting failures                  |


### How do you create custom exceptions?

- In Python, you create custom exceptions by defining a new class that inherits from Exception (or one of its subclasses).

```py
class MyCustomError(Exception):
    pass


try:
    raise MyCustomError("Oops, custom issue here")
except MyCustomError as e:
    print("Caught custom exception:", e)

```

### What happens if you don’t handle an exception?

If you don’t handle an exception in Python — that is, you let it propagate without a matching try–except block — Python will:

Immediately stop executing the current function (or block of code),

Unwind the call stack to find an enclosing try–except that can handle it, and

If no handler is found, terminate the program and display an error traceback to the user.

### How do you open and close a file in Python?


```py
file = open("data.txt", "w")  # opens file for writing
file.write("Hello, Python!\n")
file.close()

```

- modern way

```py
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# file is automatically closed here
```


### What are file modes in Python (r, w, a, etc.)?

When you open a file using open(filename, mode), the mode defines what you intend to do with the file — whether you want to read, write, or append data, and whether it’s text or binary.

| Mode   | Meaning                 | Behavior                                                                         |
| ------ | ----------------------- | -------------------------------------------------------------------------------- |
| `'r'`  | **Read (default)**      | Opens file for reading. Error if file doesn’t exist.                             |
| `'w'`  | **Write**               | Opens file for writing (creates new file or overwrites existing one).            |
| `'a'`  | **Append**              | Opens file for writing but appends at the end. Creates file if it doesn’t exist. |
| `'x'`  | **Exclusive creation**  | Creates new file, raises error if it already exists.                             |
| `'r+'` | **Read + Write**        | Opens existing file for both reading and writing.                                |
| `'w+'` | **Write + Read**        | Overwrites file if it exists, creates if not.                                    |
| `'a+'` | **Append + Read**       | Opens for reading and appending. File pointer at the end.                        |
| `'b'`  | **Binary mode**         | Used with other modes (e.g., `'rb'`, `'wb'`) for binary data.                    |
| `'t'`  | **Text mode (default)** | Used with text files — strings are encoded/decoded automatically.                |


### What is the difference between read(), readline(), and readlines()?

- read method reads entire file
- readline -> reads one line at a time
- readlines -> reads all lines as a list 

### How do you handle binary files?

- we have to use "rb" , "wb" which are read binary & write binary

### What is duck typing in Python?

- Duck typing is central to Python’s dynamic typing and polymorphism:
- if the attribute is not present it will throw attribute error "AttributeError"

```py
class Duck:
    def quack(self):
        print("Quack! Quack!")

class Person:
    def quack(self):
        print("I’m imitating a duck!")

def make_it_quack(thing):
    thing.quack()

duck = Duck()
person = Person()

make_it_quack(duck)    # Output: Quack! Quack!
make_it_quack(person)  # Output: I’m imitating a duck!
```

### What are type hints and how do they help?

- Type hints in Python are annotations that specify the expected data types of variables, function parameters, and return values — but without enforcing them at runtime.

```py
def add(a: int, b: int) -> int:
    return a + b
```

- advanced

```py
from typing import List, Dict, Optional, Union

def greet(name: Optional[str] = None) -> str:
    return f"Hello, {name or 'Guest'}!"

def total(values: List[int]) -> int:
    return sum(values)

def get_user_data() -> Dict[str, Union[int, str]]:
    return {"id": 1, "name": "Alice"}

```


### What is monkey patching?

- Monkey patching in Python means modifying or extending code at runtime — usually by changing classes, methods, or modules after they’ve already been defined.

```py
class Animal:
    def speak(self):
        print("Some sound")

# Original behavior
a = Animal()
a.speak()   # Output: Some sound

# Monkey patching the class method
def new_speak(self):
    print("Woof! Woof!")

Animal.speak = new_speak   # Reassign the method

a.speak()   # Output: Woof! Woof!

```

### What is __slots__ and why use it?

- slots is a special attruibute to restrict what attributes can a class have
- pass it as a tuple , & it will throw attributeerror

```py
class Person:
    __slots__ = ('name', 'age')  # Only these attributes allowed

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Bob", 30)
p.name = "Robert"  # Works fine
p.address = "London"  # ❌ Raises AttributeError

```

### How do you optimize performance in Python applications?

- always measure first (@profile) decorators , 
- use correct data strucutes and optimised algorighms with lowest possible time complexity
- use numpy and pandas for vectorised work
- cache data when possible

### What is pickling and unpickling?

- Pickling is the process of converting a Python object into a byte stream (a sequence of bytes).
- for pickle and json use dump , load for file , when in memory use dumps and loads
```py
import pickle
data = {"name": "Alice", "age": 25, "skills": ["Python", "AI", "ML"]}
# Serialize (pickle) the object and save it to a file
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

```

### json ?

```py
import json

data = {"name": "Alice", "age": 25, "skills": ["Python", "AI", "ML"]}

json_string = json.dumps(data)
print(json_string)

data = json.loads(json_string)
```

### differece between json & picke ?

| Aspect          | **JSON**                                             | **Pickle**                                        |
| --------------- | ---------------------------------------------------- | ------------------------------------------------- |
| **Goal**        | Data exchange between systems (language-independent) | Save and restore Python objects (Python-specific) |
| **Format type** | Text (human-readable)                                | Binary (machine-readable)                         |


### what is weak reference ?

- once actual object is deleted the refernced object is also deleted if used as weak reference

```py
import weakref

class MyClass:
    pass

obj = MyClass()
weak_obj = weakref.ref(obj)  # Create weak reference

print(weak_obj())   # Access the object via the weak reference
del obj             # Delete the strong reference
print(weak_obj())   # Now returns None (object garbage-collected)

```


### What are memory leaks and how can they be avoided?

1. Unintentional Object References
2. Reference Cycles

```py
leak_list = []

def add_data():
    data = [i for i in range(10000)]
    leak_list.append(data)  # Object never released

for _ in range(1000):
    add_data()

class A:
    def __init__(self):
        self.b = B(self)

class B:
    def __init__(self, a):
        self.a = a

```

### What is the difference between __new__ and __init__?

__new__ is called before the object exists.

__init__ is called after the object exists.


## Coding Questions Most asked as per Chat GPT : 

### Write a program to check if a number is prime

```py
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

```


### Print Fibonacci series up to N terms.

```py
def fibonacci(num):
    if num <= 0:
        return []
    a, b = 0, 1
    result = []
    for _ in range(num):
        result.append(a)
        a, b = b, a + b
        
    print(result)
    
fibonacci(10)
```

### Reverse a string without using slicing.

```py
string = "helloworld"

rev = ""

for i in range(len(string) - 1,-1,-1):
    rev = rev + string[i]
    
print(rev)
```

### Count vowels and consonants in a string.

```py
def count_alphabet(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    cons_count = 0

    for ch in string:
        if ch.isalpha():  # only count letters
            if ch in vowels:
                vowel_count += 1
            else:
                cons_count += 1

    print(f"Vowels: {vowel_count}, Consonants: {cons_count}")

count_alphabet("helloworld")
```

### Find the factorial of a number using recursion.

```py

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(3))

```

### Check if a string is a palindrome.

```py
def is_palindrome(string):
    string = string.lower()
    rev = ""
    for i in range(len(string) - 1, -1,-1):
        rev += string[i]
    return string == rev
word = "cac"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
```

### Swap two numbers without using a third variable.

```py
a = 10
b = 20
a, b = b, a
print(a, b)

a = 10
b = 20

a = a + b
b = a - b
a = a - b
```

### Find maximum and minimum elements in a list.

```py
li = [10, 20, 30, -10]
li = sorted(li)
print(li[0])
print(li[-1])

numbers = [10, 25, 3, 56, 78, 2, 45]

max_num = max(numbers)
min_num = min(numbers)

print("Maximum:", max_num)
print("Minimum:", min_num)

numbers = [10, 25, 3, 56, 78, 2, 45]

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Maximum:", max_num)
print("Minimum:", min_num)
```

### Check if two strings are anagrams.

```py
def is_anagram(str1, str2):
    # Remove spaces and make lowercase for fairness
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

# Example
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
```

```py
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    count = {}

    for ch in str1:
        count[ch] = count.get(ch, 0) + 1

    for ch in str2:
        if ch in count:
            count[ch] -= 1
        else:
            return False

    for val in count.values():
        if val != 0:
            return False

    return True

# Example
print(is_anagram("listen", "silent"))  # True
print(is_anagram("evil", "vile"))      # True
print(is_anagram("rat", "car"))        # False
```

### Find the second largest number in a list.

```py
numbers = [10, 25, 3, 56, 78, 78, 45]

unique_numbers = list(set(numbers))  # remove duplicates
unique_numbers.sort()

print("Second largest number:", unique_numbers[-2])

```

```py
numbers = [10, 25, 3, 56, 78, 45]

first = second = float('-inf')

for num in numbers:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print("Second largest number:", second)
```


### Flatten a nested list (one level) using list comprehension.

```py
nested = [[1,2,3], [4,5,6]]
flat = [item for sub in nested for item in sub]
print(flat)
```

### Remove duplicates from a list.

```py
numbers = [1, 2, 3, 2, 4, 1, 5]

unique_numbers = list(set(numbers))

print(unique_numbers)

```


### Merge two dictionaries in Python.

```py
# ✅ Method 1: Using the merge (|) operator — Python 3.9+
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1 | dict2
print(merged)
dict1 |= dict2

# ✅ Method 2: Using dictionary unpacking (Python 3.5+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = {**dict1, **dict2}
print(merged)


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
# ✅ Method 3: Using .update() method
dict1.update(dict2)
print(dict1)
```

### Sort a dictionary by key or value using lambda.

```py
sorted_by_key = dict(sorted(data.items(), key=lambda x: x[0]))
print(sorted_by_key)

```

### Convert a list of tuples into a dictionary.

```py
pairs = [('a', 1), ('b', 2), ('c', 3)]

result = dict(pairs)

print(result)


pairs = [('a', 1), ('b', 2), ('c', 3)]

result = {key: value for key, value in pairs}

print(result)

```

### Find common elements in two lists.


```py
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

common = list(set(list1) & set(list2))
all_ = list(set(list1) | set(list2))

print(common)
print(all_)
```


### Convert two lists into a dictionary.


```py
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

my_dict = dict(zip(keys, values))
print(my_dict)

```

### Sort a list of dictionaries by a specific key.

```py
li = [
    {
        name: "harshith",
        age: 26
    },
    {
        name: "sadvika",
        age: 21
    }
]

print(sorted(li, key=lambda x: x['name'], reverse=True))
```

### Group elements of a list by their first letter.

```py
from collections import defaultdict
words = ['apple', 'banana', 'apricot', 'cherry', 'blueberry', 'avocado']

grouped = defaultdict(list)
for word in words:
    first_letter = word[0].lower()
    grouped[first_letter].append(word)

print(dict(grouped))
```

### Write a basic decorator to log function calls.


```py
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Logging Function {func.__name__} with {args} {kwargs}")
        func(*args, **kwargs)
        print("Function Call Complete")
    return wrapper

@logger
def hello(name, age):
    print(f"hello world {name} {age}")
    
hello("john", age=10)
```

### Create a decorator that measures function execution time.

```py
import time

def calcule_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Total Execution Time = {time.time - start} milliseconds")
    return wrapper

@calculate_time
def hello():
    for i in range(1000):
        print(i)
```

### Create a decorator that measures function execution time.

```py
import time

import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution Time: {end - start:.4f} seconds")
        return res
    return wrapper


@calculate_time
def hello():
    for _ in range(100000000):
        pass
    
hello()
```

### Implement a closure that remembers the last 3 results.

```py
def remember_last_three():
    results = []  # enclosed variable — will persist between calls

    def inner(new_result):
        results.append(new_result)
        if len(results) > 3:        # keep only the last 3
            results.pop(0)
        return results[:]           # return a copy to prevent external modification
    return inner

```

### Write a function that returns a generator for even numbers.


```py
def even_numbers:
    counter = 0
    while True:
        counter += 2
        yield i
it = iter(even_numbers)
for i in range(10):
    print(next(it))
```

### Write a recursive function to calculate the sum of digits of a number.


```py
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

num = 12345
print("Sum of digits:", sum_of_digits(num))
```

### Write a lambda function to filter even numbers from a list.


```py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
```

### Write a function that accepts variable arguments (*args) and sums them.

```py
def sum_all(*args):
    return sum(args)

# Example
print(sum_all(1, 2, 3))         # 6
print(sum_all(5, 10, 15, 20))   # 50

```

### Write a function to check if a given year is a leap year.

```py
def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

# Example
print(is_leap_year(2020))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True

```

### Write a function that finds the intersection of multiple lists.

```py
def intersection_of_lists(*lists):
    if not lists:
        return []

    # Convert first list to a set and intersect with the rest
    result = set(lists[0])
    for lst in lists[1:]:
        result &= set(lst)
    return list(result)

# Example
print(intersection_of_lists([1, 2, 3, 4], [2, 3, 5], [3, 6, 2]))

```


### Implement a custom context manager using __enter__ and __exit__.

```py
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file  # This object will be assigned to the variable in 'with'

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        if self.file:
            self.file.close()

        # Handle exceptions if needed
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
        # Returning False means exceptions (if any) will still propagate
        return False

# Example usage
with FileManager("example.txt", "w") as f:
    f.write("Hello, context managers!")

print("File operation complete.")

```

### Create a class Employee with attributes and methods to display details.


```py
class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ₹{self.salary}")

# Example usage
emp1 = Employee("Alice", 101, "HR", 50000)
emp2 = Employee("Bob", 102, "IT", 75000)

emp1.display_details()
print("-" * 25)
emp2.display_details()

```

- dataclasses

```py
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    emp_id: int
    department: str
    salary: float

# Example usage
emp1 = Employee("Alice", 101, "HR", 50000)
emp2 = Employee("Bob", 102, "IT", 75000)

print(emp1)
print(emp2)

```

- @propery

```py
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # underscore indicates "internal" use

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

    @salary.deleter
    def salary(self):
        print("Deleting salary...")
        del self._salary

# Example usage
emp = Employee("John", 50000)
print(emp.salary)   # calls getter

emp.salary = 60000  # calls setter
print(emp.salary)

# emp.salary = -1000  # would raise ValueError

del emp.salary       # calls deleter

```

### Demonstrate inheritance using two classes.


```py
# Base class
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ₹{self.salary}")

# Derived class (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        # Call the base class constructor
        super().__init__(name, emp_id, salary)
        self.department = department

    # Add or override methods
    def display_details(self):
        super().display_details()  # reuse parent logic
        print(f"Department: {self.department}")

# Example usage
emp = Employee("Alice", 101, 50000)
mgr = Manager("Bob", 102, 80000, "IT")

print("Employee Details:")
emp.display_details()

print("\nManager Details:")
mgr.display_details()

```


### Implement abstraction using ABC module.

```py
from abc import ABC, abstractmethod

# Abstract base class
class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        """Subclasses must implement this method"""
        pass

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

# Concrete subclass
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

# Another subclass
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Example usage
full_time = FullTimeEmployee("Alice", 101, 60000)
part_time = PartTimeEmployee("Bob", 102, 500, 80)

print("Full-Time Employee:")
full_time.display_details()
print("Salary:", full_time.calculate_salary())

print("\nPart-Time Employee:")
part_time.display_details()
print("Salary:", part_time.calculate_salary())

```

### Create a class with private variables and access them using methods.

```py
class Employee:
    def __init__(self, name, salary):
        self.__name = name        # private variable
        self.__salary = salary    # private variable

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for salary
    def get_salary(self):
        return self.__salary

    # Setter method for salary
    def set_salary(self, salary):
        if salary < 0:
            print("Salary cannot be negative!")
        else:
            self.__salary = salary

# Example usage
emp = Employee("Alice", 50000)

# Accessing private data using getter methods
print("Name:", emp.get_name())
print("Salary:", emp.get_salary())

# Modifying private data using setter methods
emp.set_name("Alicia")
emp.set_salary(60000)

print("\nAfter update:")
print("Name:", emp.get_name())
print("Salary:", emp.get_salary())

# Trying invalid update
emp.set_salary(-10000)

```

### Write a class method and static method example.


```py
class Employee:
    company = "TechCorp"   # class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Class method: accesses or modifies class-level data
    @classmethod
    def set_company(cls, new_name):
        cls.company = new_name

    # Static method: utility function, no access to class or instance data
    @staticmethod
    def is_workday(day):
        return day.lower() not in ['saturday', 'sunday']

# Example usage
emp1 = Employee("Alice", 50000)

# Access class variable
print("Company:", Employee.company)

# Change class variable using class method
Employee.set_company("NextGenTech")
print("Updated Company:", emp1.company)

# Using static method
print("Is Monday a workday?", Employee.is_workday("Monday"))
print("Is Sunday a workday?", Employee.is_workday("Sunday"))

```

### Overload the + operator in a custom class.


```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Example usage
p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2  # calls p1.__add__(p2)
print(p3)

```

### Serialize a Python dictionary to JSON.


```py
import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "department": "IT",
    "skills": ["Python", "SQL", "Machine Learning"]
}

# Serialize dictionary to JSON string
json_data = json.dumps(data)

print(json_data)


with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

```

### Read and write a file in Python.

```py
# Writing data to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a file handling example.")

# Reading data from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


```

### Count number of lines, words, and characters in a file.

```py
def count_file_stats(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)

    return num_lines, num_words, num_chars

# Example usage
with open("sample.txt", "w") as f:
    f.write("Python is fun.\n")
    f.write("File handling is easy to learn.\n")
    f.write("Keep practicing!")

lines, words, chars = count_file_stats("sample.txt")

print(f"Lines: {lines}")
print(f"Words: {words}")
print(f"Characters: {chars}")


```

### Implement a singleton class.

```py
class Singleton:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Example usage
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True → both refer to the same instance

```

