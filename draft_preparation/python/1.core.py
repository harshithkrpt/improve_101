x = 10 # int 
z = "Hello" # str 
y = True # bool
a = 11.2 # float
b = [1,2,3,4,5] # list # mutable 
c = (1,2,3,4,5) # tuple # immutable 
d = {1,2,3,4,5} # set # mutable
e = {1: "one", 2: "two", 3: "three"} # dict # mutable
f = None # NoneType

# int, str, float, bool, bytes, 
# list, tuple, set, dict
# NoneType, complex, frozenset
# mutable, immutable
    # mutable: list, set, dict
    # immutable: int, str, float, bool, bytes, tuple, frozenset
# typecasting
a = int("10")
b = str(10)
c = list("abc") # ['a', 'b', 'c']
d = tuple("abc") # ('a', 'b', 'c')
e = set("abc") # {'a', 'b', 'c'}


# TODO: Deep Dive into List, Tuple, Set, Dict

li = [1,2,3,4,5]
li[0] = 10
print(li) # [10,2,3,4,5]

# Built in Methods

lst = [1, 2]; lst.append(3)  # [1, 2, 3]
print(lst)

lst.extend([4, 5])  # [1, 2, 3, 4, 5]
print(lst)

lst.insert(0, 0)  # [0, 1, 2, 3, 4, 5]
print(lst)


# Remove based on first occurance of the value
lst.remove(0)  # [1, 2, 3, 4, 5]
print(lst)

# pop removes the last element
lst.pop()  # [1, 2, 3, 4]
print(lst)

# or we can pass the index
lst.pop(0)  # [2, 3, 4]
print(lst)

# clear the list
lst.clear()  # []
print(lst)

# reverse the list
lst.reverse()  # [4, 3, 2, 1]
print(lst)

# sort the list
lst.sort()  # [1, 2, 3, 4]
print(lst)

# sort the list in descending order
lst.sort(reverse=True)  # [4, 3, 2, 1]
print(lst)

sorted(lst)  # [1, 2, 3, 4] # returns a new list
print(lst)

# sort the list in descending order
sorted(lst, reverse=True)  # [4, 3, 2, 1] # returns a new list
print(lst)

# count the number of elements in the list
lst.count(2)  # 1
print(lst)

# copy
lst.copy()  # [1, 2, 3, 4] # returns a new list with shallow copy
print(lst)

## Operators of List with Dunder Methods

lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]

print(lst1 + lst2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst1 * 2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(1 in lst1)  # True
print(10 not in lst1)  # True
print(lst1 == lst2)  # False


# list comprehension
lst = [1,2,3,4,5]
lst = [x * 2 for x in lst]
print(lst) # [2, 4, 6, 8, 10]

# list comprehension with if
lst = [1,2,3,4,5]
lst = [x * 2 for x in lst if x % 2 == 0]
print(lst) # [4, 8]

# list comprehension with if else
lst = [1,2,3,4,5]
lst = [x * 2 if x % 2 == 0 else x for x in lst]
print(lst) # [2, 4, 6, 8, 10]

# list comprehension with nested loops
lst = [1,2,3,4,5]
lst = [x * y for x in lst for y in lst]
print(lst) # [1, 2, 3, 4, 5, 2, 4, 6, 8, 10, 3, 6, 9, 12, 15, 4, 8, 12, 16, 20, 5, 10, 15, 20, 25]

# list comprehension with nested loops with if
lst = [1,2,3,4,5]
lst = [x * y for x in lst for y in lst if x % 2 == 0 and y % 2 == 0]
print(lst) # [4, 8, 12, 16, 20]

# trick to remember list comprehension
# [expression for item in iterable if condition]
# [expression for item in iterable]
# [expression if condition else expression for item in iterable]


# Tuple

t = (1, "hello", 1.3, (1,2), True)
single = (1,)  # the comma is essential
not_a_tuple = (1)  # just an int

# Indexing & Slicing Works List List
t[0] # 1
t[-1] # True
t[1: 3] # ('hello', 1.3) 

# Tuples are immutable, but if they contain mutable elements, those can still be changed.
t = (1, [2,3])
t[1].append(4)  # (1, [2,3,4])

# Tuple Methods  .count,index()
(1,2,2,3).count(2) # 2
(1,2,3).index(3) # 2


# Operations with Tuppels

(1,2) + (2,3) # (1,2,2,3) 
(1,) * 3 # (1,1,1)
2 in (1,2,3)
# Iteration
for x in (1,2,3): print(x)

# Packing & Unpacking
a, b, c = (1,2,3)

# Nested Tuples
nested_tuples = ((1,2,3), (4,5,6), (7,8,9))


# Dictionary
person = {"name": "Harshith", "age": 25, "skills": ["Python", "Rust"]}
person["name"]  # "Harshith"
person["city"] = "Hyderabad"
del person["skills"]
person["age"] = 26

# Dictionary Methods
d = {"a": 1}
d.update({"b": "new value", "c": "donation"})
d.get("x", 0) # get x if present if not return 0
d.keys() # returns all keys
d.values() # returns all values
d.items() # returns dict_list in tuple format
d.pop("a")  # returns 1
d.clear()
d.copy() # shallow copy


# looping throught dictionaries
for key, val in person.items():
    print(key, val)

squares = {x: x*x for x in range(10)}


# Sets
s = {1, 2, 3, 3}
print(s)  # {1, 2, 3} → duplicates vanish
s = set([1, 2, 2, 3])  # {1, 2, 3}
# Adding & Removing
# add(x) → Add element.
# update(iterable) → Add multiple elements.

# remove(x) → Remove element, error if not present.

# discard(x) → Remove element, no error if not present.

# pop() → Remove and return a random element.

# clear() → Empty the set.

# Create a set
s = {1, 2, 3}

# Add single element
s.add(4)  
print(s)  # {1, 2, 3, 4}

# Add multiple elements from iterable
s.update([5, 6, 7])
print(s)  # {1, 2, 3, 4, 5, 6, 7}

s = {1, 2, 3, 4, 5}

# Remove element (raises error if not found)
s.remove(3)
print(s)  # {1, 2, 4, 5}

# Discard element (safe, no error if not found)
s.discard(10)  
print(s)  # {1, 2, 4, 5}

# Pop random element
removed = s.pop()
print("Popped:", removed, "Remaining:", s)

# Clear entire set
s.clear()
print(s)  # set()

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all unique elements from both sets)
print(a.union(b))   # {1, 2, 3, 4, 5, 6}
print(a | b)        # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print(a.intersection(b))  # {3, 4}
print(a & b)              # {3, 4}

# Difference (elements in a but not in b)
print(a.difference(b))  # {1, 2}
print(a - b)            # {1, 2}

# Symmetric Difference (elements in either but not both)
print(a.symmetric_difference(b))  # {1, 2, 5, 6}
print(a ^ b)                      # {1, 2, 5, 6}

x = {1, 2}
y = {1, 2, 3, 4}
z = {5, 6}

# Subset: is x inside y?
print(x.issubset(y))   # True

# Superset: does y contain x?
print(y.issuperset(x))  # True

# Disjoint: no elements in common
print(x.isdisjoint(z))  # True
print(x.isdisjoint(y))  # False


# Conditionals 
x = 10
if x < 0:
    print("negative")
elif x == 0:
    print("zero")
else:
    print("positive")


"""
Falsy values include:

False, None

numeric 0, 0.0, 0j

empty sequences/collections: '', (), [], {}, set()

objects with __bool__ returning False or __len__ returning 0
"""

# comparision and logical operators
if 0 < x <= 10:
    print(x)

# is and is not (checks object identity)
# in, not in (checks membership)
# and , or , not 

# short circuit evaluation 
a = False
b = 10
if a and print("this wont print"):
    print("") 

# ternary operators
status = "No..." if a == False else "Yes..."

def handle(value):
    match value:
        case 0:
            return "Zero"
        case [x, y]:
            return f"pair {x}, {y}"
        case _:
            return "something else"

number = 10

while number > 0:
    print(number)
    number -= 1


number = 6

while number > 0:
    number -= 1
    if number == 2:
        break
    print(number)

print("Loop ended")

number = 6

while number > 0:
    number -= 1
    if number == 2:
        continue
    print(number)

print("Loop ended")

requests = ["first request", "second request", "third request"]

it = iter(requests)
while True:
    try:
        request = next(it)
    except StopIteration:
        break
    
    print(f"Handling {request}")

colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)

points = [(1, 4), (3, 6), (7, 3)]
for x,y in points:
    print(f"{x =} and {y =}")

# for loops
for i in range(10):
    print(i)

text = "abcde"
for character in text:
    print(character)

# for with else
for i in range(2):
    print(i)
else:
    print("Done")

teams = {
     "Colorado": "Rockies",
     "Chicago": "White Sox",
     "Boston": "Red Sox",
     "Minnesota": "Twins",
     "Milwaukee": "Brewers",
     "Seattle": "Mariners",
 }

for student in teams:
    print(student , teams[student])

fruits = ["orange", "apple", "mango", "lemon"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

numbers = [1, 2, 3]
letters = ["a", "b", "c"]

for number, letter in zip(numbers, letters):
    print(number , "->", letter)

numbers = [2, 4, 6, 8]

for number in numbers[:]:
    if number % 2 == 0:
        number.remove(number)


cubes = []

for i in range(10):
    cubes.append(i ** 3)

cubes = [i ** 3 for i in range(10)]
print(cubes)

import asyncio

class AsyncRange:
    def __init__(self, start, end):
        self.data = range(start, end)

    async def __aiter__(self):
        for index in self.data:
            await asyncio.sleep(0.5)
            yield index

async def main():
    async for index in AsyncRange(0, 5):
        print(index)

asyncio.run(main())

# ...

try:
    with open("file.log") as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except RuntimeError as error:
    print(error)
    print("Linux linux_interaction() function wasn't executed.")


# ...

try:
    linux_interaction()
except RuntimeError as error:
    print(error)
else:
    try:
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("Cleaning up, irrespective of any exceptions.")


from pathlib import Path

def read_file_contents(file_path):
    path = Path(file_path)

    if not path.exists():
        print(f"Error: The file '{file_path}' does not exist.")
        return

    if not path.is_file():
        print(f"Error: '{file_path}' is not a file.")
        return

    return path.read_text(encoding="utf-8")

# Returning Generator Iterators

def cumulative_average(numbers):
    total = 0
    for items, number in enumerate(numbers, 1):
        total += number
        yield total / items

values = [5, 3, 8, 2, 5]  # Simulates a large data set

for cum_average in cumulative_average(values):
    print(f"Cumulative average: {cum_average:.2f}")

# Creating Closures
def function():
    value = 42
    def closure():
        print(f"The value is: {value}!")
    return closure

reveal_number = function()
reveal_number()

def greet(name="World"):
    print(f"Hello, {name}!")


def append_to(item, target=[]):
    target.append(item)
    return target

append_to(1)
append_to(2)
append_to(3) # [1,2,3]

# as target only initialzed once and uses same memory


def function(*args):
    print(args)
    print(type(args))

function(1,2,3,4,5)


def function(**kwargs):
    print(kwargs)

function(name="one",age=25)


def report(**kwargs):
    print("Report : ")
    for key, value in kwargs.items():
        print(f"{key} -> {value}")
report(name="computer", price="300$", category="PC")

# Positional-Only Arguments
# below first_name, last_name are positional only args as they are before /
def format_name(first_name, last_name, /, title=None):
    pass


def sum_numbers(*numbers, precision=2):
    return round(sum(numbers), precision)

sum_numbers(1.3467, 2.5243, precision=3)

# Keyword-Only Arguments
def calculate(x, y, *, operator):
    pass

# calculate(3, 4, "+") -> error 

import asyncio

async def get_number():
    return 42


asyncio.run(get_number())

"""
print() – Output to console.

len() – Get size/length.

range() – Sequence of numbers.

type() – Get an object’s type.

int() – Convert to integer.

str() – Convert to string.

list() – Make lists.

dict() – Make dictionaries.

set() – Make sets / deduplicate.

sum() – Add items in an iterable.

max() – Largest value.

min() – Smallest value.

sorted() – Return sorted iterable.

enumerate() – Index + value when looping.

zip() – Pair items from multiple iterables.

map() – Apply function to items.

filter() – Keep items by condition.

any() – Check if any item is True.

all() – Check if all items are True.

isinstance() – Safe type check.

open() – File handling.

round() – Round numbers.

abs() – Absolute value.

pow() – Power/exponentiation.

help() – Interactive documentation.

globals() – Current global symbol table (common in debugging/dynamic code).

locals() – Current local symbol table.

id() – Object’s memory identity.

chr() – Convert code point → character.

ord() – Convert character → code point.
"""