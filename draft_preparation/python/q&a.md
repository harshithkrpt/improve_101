# Python Memory, References, and Data Behavior – Q&A Notes

---

### Q: What is the LEGB rule in Python?  
**A:** LEGB stands for **Local, Enclosing, Global, and Built-in scope**.  
Python searches for a variable in this order when resolving names.
Python looks in this order L → E → G → B when resolving a variable. If it doesn’t find it in any of these scopes, you get a NameError.
```py
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # Local is picked first
    inner()

outer()  # prints "local"

```
---

### Q: What is the difference between mutable and immutable objects?  
**A:**  

Immutable Objects

Once created, their value cannot be changed.

Any “modification” creates a new object in memory.

Examples: int, float, str, tuple, frozenset.
```py
x = "hello"
print(id(x))   # memory address of x
x = x + " world"   # creates a new string object
print(id(x))   # different memory address

```
Mutable Objects

Their contents can be changed without creating a new object.

The variable still points to the same memory address.

Examples: list, dict, set, bytearray.
```py
y = [1, 2, 3]
print(id(y))   # memory address of y
y.append(4)    # modifies the list in place
print(id(y))   # same memory address
print(y)       # [1, 2, 3, 4]

```

Safety: Immutable objects are thread-safe since they can’t be altered.
Surprises with default arguments: Mutable default arguments can lead to tricky bugs.

```py
def add_item(item, basket=[]):  # mutable default
    basket.append(item)
    return basket

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['apple', 'banana']  <-- surprise!

```
---

### Q: How does garbage collection work in Python?  
**A:** Python has an **automatic garbage collector** that reclaims memory from objects that are no longer referenced.  
It primarily uses **reference counting**, with **cycle detection** for circular references.

---

### Q: What is the difference between `is` and `==`?  
**A:**  

== (Equality operator)

Checks if two objects have the same value (contents).

Doesn’t care if they are the exact same object in memory.

```py
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True  (same contents)
print(a is b)  # False (different objects in memory)

```
is (Identity operator)

Checks if two variables point to the exact same object in memory.

Essentially compares object IDs (id(a) == id(b)).

```py
x = "python"
y = "python"

print(x == y)  # True  (same value)
print(x is y)  # True or False?  

# Often True because of "string interning"

```

---

### Q: What is the difference between a list and a tuple?  
**A:**  
- **List**: mutable, allows modifications, slightly slower.  
- **Tuple**: immutable, faster, can be used as dictionary keys.

---

### Q: How are variables stored in memory in Python?  

1. Objects live in the heap
Every value you create in Python (an int, list, str, even a function) is an object stored on the heap.
2. Variables are references
```py
x = [1, 2, 3]
y = x   # y points to the same list as x

```
Immutables vs mutables
Immutable objects (int, str, tuple) can’t be modified in place. Reassignment creates a new object in memory.
Mutable objects (list, dict, set) can be modified in place; the reference stays the same.

---


### Q: Why can’t you reassign to a variable inside a function without global or nonlocal?

1. Assignment = “new local variable”

When Python sees an assignment inside a function, it assumes that name belongs to the function’s local scope, unless told otherwise.

```py
x = 10  # global

def foo():
    x = 20  # creates a NEW local x
    print(x)

foo()        # prints 20
print(x)     # still 10 (global unchanged)

```

```py
x = 10

def foo():
    global x
    x += 1  # modifies the global x
    print(x)

foo()  # 11

```

```py
def outer():
    y = 5
    def inner():
        nonlocal y
        y += 1  # modifies y from outer()
        print(y)
    inner()
    print(y)

outer()
# prints 6 and then 6

```

---

### What happens when you do x = 1000; y = 1000; print(x is y)?

That line is a Python trick question — it depends on how Python manages integer caching (interning).

1. Small integer caching

Python pre-creates and caches integers in the range -5 to 256.
Any variable assigned to those values reuses the same object in memory.

```py
a = 256
b = 256
print(a is b)  # True (cached)

```

2. Larger integers
Integers outside -5 to 256 are not guaranteed to be cached.

So 1000 typically creates a new object each time.

Result:

```py
x = 1000
y = 1000
print(x is y)  # False (different objects in memory)

```

---

### Difference between list, tuple, set, dict?

1. List
1.1 Ordered -> elemets in the memory are stored in order
1.2 Mutable -> you can change items, add, remove, slice etc..
1.3 duplicates allowed

```py
    nums = [10,20,30]
    nums.append(40) # [10, 20, 30, 40]
```

2. Tuple
2.1 Ordered: Keeps insertion order
2.2 Immutable -> if you change it will create complete new object
2.3 Duplicates allowed
Ex : 

```py
    point = (1,2)
```

3. Set
3.1 Unordered: no gaurenteed order 
3.2 Mutable: can add/remove 
3.3 Unique Elements only: {1,2,3,2} -> {1,2,3}
Ex: 
```py
items = {1,2,3}
items.add(4) # {1,2,3,4}
```

4. Dict (Dictionary)
4.2 Ordered: Since 3.7 keeps insertion order
4.3 Mutable: Keys and values can be added/removed/updated
4.4 Unique Keys, but values can be repeated

Ex:
```py
user = {"name": "Harshith", "age": 25}
print(user["name"]) # Harshith
```
---

| Feature    | List | Tuple | Set | Dict             |
| ---------- | ---- | ----- | --- | ---------------- |
| Ordered    | ✅    | ✅     | ❌   | ✅ (since 3.7)    |
| Mutable    | ✅    | ❌     | ✅   | ✅                |
| Duplicates | ✅    | ✅     | ❌   | Keys ❌, Values ✅ |
| Indexing   | ✅    | ✅     | ❌   | Keys-based       |

---

### Why are strings immutable in Python?

1. Efficiency & Interning
Python uses string interning (storing common strings only once in memory, like "yes", "no", "python").
In multithreaded programs, immutability means two threads can share the same string without locking.
---

### How is a tuple different from a list?

| Feature     | List      | Tuple                                     |
| ----------- | --------- | ----------------------------------------- |
| Syntax      | `[ ]`     | `( )`                                     |
| Mutability  | ✅ Mutable | ❌ Immutable                               |
| Ordered     | ✅         | ✅                                         |
| Performance | Slower    | Faster                                    |
| Use as Key  | ❌ No      | ✅ Yes (hashable if elements are hashable) |


---

### What is a shallow copy vs deep copy (copy vs deepcopy)?

Shallow Copy
- makes a new container but does not recursively copy the objects inside
- instead it just copies the references to the inner objects


```py
import copy

a = [[1,2],[3,4]]
b = copy.copy(a)
b[0][0] = 99
print(a) # [[99,2], [3,4]]
print(b)
```

Deep Copy

Makes a new container and recursively copies all the inner objects.

```py
c = copy.deepcopy(a)
c[0][0] = 111

print(a)  # [[99, 2], [3, 4]]
print(c)  # [[111, 2], [3, 4]]

```
| Feature       | Shallow Copy (copy) | Deep Copy (deepcopy) |
| ------------- | ------------------- | -------------------- |
| Outer object  | New                 | New                  |
| Inner objects | Shared (same refs)  | New (fully cloned)   |
| Performance   | Faster              | Slower (recursive)   |
| Independence  | ❌ Not independent   | ✅ Fully independent  |

---

### How does Python store bool(True) internally?

1. Booleans are just special integers
where True and False aren’t just floaty concepts but actual little C structs sitting in memory.
```py
isinstance(True, int)   # True
True + 5                # 6
```
---

### Cheat sheet for python conditions 

# 🐍 Python Conditionals Cheat Sheet

### Basic structure
```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...
```

---

### Truthiness
Falsy values:
- `False`, `None`
- `0`, `0.0`, `0j`
- empty: `''`, `[]`, `{}`, `set()`
- objects with `__bool__ → False` or `__len__ → 0`

---

### Comparisons & Operators
- `==`, `!=`, `<`, `<=`, `>`, `>=`
- `is`, `is not` → identity
- `in`, `not in` → membership
- `and`, `or`, `not` → logical
- Chaining: `0 < x <= 10`

---

### Idioms
```python
# Ternary expression
status = "even" if x % 2 == 0 else "odd"

# Short-circuit
result = a or b      # returns a if truthy else b
guard = a and func() # calls func() only if a truthy

# Early return
if not data:
    return None
```

---

### Walrus Operator (Python 3.8+)
```python
if (n := len(items)) > 5:
    print(f"{n} items")
```

---

### Pattern Matching (Python 3.10+)
```python
match value:
    case 0:
        ...
    case [x, y]:
        ...
    case {"type": "A", "data": d}:
        ...
    case _:
        ...
```

---

### Collection checks
```python
if any(x % 2 == 0 for x in nums):
    ...
if all(isinstance(x, int) for x in items):
    ...
```

---

### EAFP vs LBYL
```python
# EAFP (preferred in Python)
try:
    v = d["key"]
except KeyError:
    v = default

# LBYL
if "key" in d:
    v = d["key"]
else:
    v = default
```

---

### DO ✅
- Use `is None` / `is not None`
- Use `any()` / `all()` for bulk checks
- Use early returns to reduce nesting
- Use `match` for structured branching

### DON’T ❌
- Use `is` for value equality
- Rely on hidden truthiness in unclear cases
- Compare floats with `==` (use `math.isclose`)
