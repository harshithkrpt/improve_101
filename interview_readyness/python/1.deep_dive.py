x = 42          # int
y = 3.14        # float
z = "Python"    # str
is_active = True # bool


# List: mutable, ordered
fruits = ["apple", "banana", "cherry"]

# Tuple: immutable, ordered
coords = (10, 20)

# Set: unique, unordered
unique_nums = {1, 2, 3, 2}

# Dict: key-value store
person = {"name": "Alice", "age": 25}


age = 20
if age >= 18:
    print("Adult")
elif age > 13:
    print("Teen")
else:
    print("Child")


for fruit in fruits:
    print(fruit)

n = 3
while n > 0:
    print(n)
    n -= 1


for i in range(5):
    if i == 3:
        break
else:
    print("Loop finished without break")


def greet(name="World"):
    return f"Hello, {name}"

print(greet())           # Hello, World
print(greet("Harshith")) # Hello, Harshith


def demo(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

demo(1, 2, 3, 4, x=5, y=6)
# 1 2 (3, 4) {'x': 5, 'y': 6}


def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

times3 = make_multiplier(3)
print(times3(10))  # 30


def debug(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@debug
def square(x): return x * x
square(4)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

buddy = Dog("Buddy")
print(buddy.speak())  # Woof!


class Vector:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)
    def __str__(self): return f"({self.x}, {self.y})"

v1, v2 = Vector(1, 2), Vector(3, 4)
print(v1 + v2)  # (4, 6)


# # file: mymodule.py
# def say_hi(): print("Hi!")

# # file: main.py
# import mymodule
# mymodule.say_hi()


try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can’t divide by zero!")
finally:
    print("Cleanup runs here.")


if x < 0:
    raise ValueError("x must be non-negative")


nums = [1, 2, 3]
it = iter(nums)
print(next(it)) # 1
print(next(it)) # 2


squares = [x*x for x in range(5)]         # list comprehension
evens = {x for x in range(10) if x % 2==0} # set comprehension


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)


with open("data.txt", "w") as f:
    f.write("Hello, file!")

with open("data.txt") as f:
    print(f.read())


x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()  # local
# Use global or nonlocal to modify outer scopes.

nums = [1, 2, 3, 4]
print(list(map(lambda x: x*2, nums)))   # [2, 4, 6, 8]
print(list(filter(lambda x: x%2==0, nums))) # [2, 4]

from functools import reduce
print(reduce(lambda a,b: a+b, nums))  # 10


import threading
def worker(): print("working")
t = threading.Thread(target=worker)
t.start()


import asyncio

async def greet():
    await asyncio.sleep(1)
    print("Hello async")

asyncio.run(greet())

a, b = 1, 2
a, b = b, a


nums = [1,2,3,4]
print(nums[::-1])  # reversed list

if []: print("won’t run")
if [1]: print("runs")
