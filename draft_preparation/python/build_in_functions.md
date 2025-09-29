# Python Built-in Functions: Top 30 Deep Cheatsheet

## print()

**Description:** Built-in function `print()` with common usecases.


```python
print("Hello, World!")  
print(1, 2, 3, sep="-", end="!\n")
```

---

## len()

**Description:** Built-in function `len()` with common usecases.


```python
len("Python")  # 6
len([1,2,3])  # 3
```

---

## range()

**Description:** Built-in function `range()` with common usecases.


```python
for i in range(5): print(i)
list(range(2, 10, 2))  # [2,4,6,8]
```

---

## type()

**Description:** Built-in function `type()` with common usecases.


```python
type(42)      # <class 'int'>
type([1,2,3]) # <class 'list'>
```

---

## int()

**Description:** Built-in function `int()` with common usecases.


```python
int("42")   # 42
int(3.99)   # 3
```

---

## str()

**Description:** Built-in function `str()` with common usecases.


```python
str(123)      # '123'
str([1,2,3])  # '[1, 2, 3]'
```

---

## list()

**Description:** Built-in function `list()` with common usecases.


```python
list("abc")    # ['a', 'b', 'c']
list((1,2,3))  # [1, 2, 3]
```

---

## dict()

**Description:** Built-in function `dict()` with common usecases.


```python
dict(a=1, b=2)         # {'a':1,'b':2}
dict([("x",1),("y",2)]) # {'x':1,'y':2}
```

---

## set()

**Description:** Built-in function `set()` with common usecases.


```python
set([1,2,2,3])   # {1,2,3}
set("hello")     # {'o','h','e','l'}
```

---

## sum()

**Description:** Built-in function `sum()` with common usecases.


```python
sum([1,2,3])          # 6
sum(range(10), 5)     # 50 (adds initial 5)
```

---

## max()

**Description:** Built-in function `max()` with common usecases.


```python
max(3,7,2)            # 7
max(["a","z","m"])    # 'z'
```

---

## min()

**Description:** Built-in function `min()` with common usecases.


```python
min(3,7,2)            # 2
min(["a","z","m"])    # 'a'
```

---

## sorted()

**Description:** Built-in function `sorted()` with common usecases.


```python
sorted([3,1,2])                   # [1,2,3]
sorted(["apple","banana"], key=len) # ['apple','banana']
```

---

## enumerate()

**Description:** Built-in function `enumerate()` with common usecases.


```python
for i, val in enumerate(["a","b"]): print(i, val)
# 0 a
# 1 b
```

---

## zip()

**Description:** Built-in function `zip()` with common usecases.


```python
list(zip([1,2,3],['a','b','c'])) # [(1,'a'),(2,'b'),(3,'c')]
```

---

## map()

**Description:** Built-in function `map()` with common usecases.


```python
list(map(str, [1,2,3]))      # ['1','2','3']
list(map(lambda x: x*2,[1,2])) # [2,4]
```

---

## filter()

**Description:** Built-in function `filter()` with common usecases.


```python
list(filter(lambda x: x>2, [1,2,3,4])) # [3,4]
```

---

## any()

**Description:** Built-in function `any()` with common usecases.


```python
any([False, False, True])  # True
```

---

## all()

**Description:** Built-in function `all()` with common usecases.


```python
all([True,1,3])   # True
all([True,0])     # False
```

---

## isinstance()

**Description:** Built-in function `isinstance()` with common usecases.


```python
isinstance(5,int)          # True
isinstance("hi",(list,str)) # True
```

---

## open()

**Description:** Built-in function `open()` with common usecases.


```python
with open("file.txt","w") as f: f.write("hello")
with open("file.txt","r") as f: data=f.read()
```

---

## round()

**Description:** Built-in function `round()` with common usecases.


```python
round(3.14159,2)  # 3.14
round(5.5)        # 6
```

---

## abs()

**Description:** Built-in function `abs()` with common usecases.


```python
abs(-5)   # 5
abs(3.14) # 3.14
```

---

## pow()

**Description:** Built-in function `pow()` with common usecases.


```python
pow(2,3)       # 8
pow(2,3,5)     # 3 (modulo)
```

---

## help()

**Description:** Built-in function `help()` with common usecases.


```python
help(len)    # Shows docstring
```

---

## globals()

**Description:** Built-in function `globals()` with common usecases.


```python
globals().keys()   # all global vars
```

---

## locals()

**Description:** Built-in function `locals()` with common usecases.


```python
def foo(x): print(locals())
foo(10)   # {'x':10}
```

---

## id()

**Description:** Built-in function `id()` with common usecases.


```python
a=42; b=42; id(a)==id(b)  # True (interned int)
```

---

## chr()

**Description:** Built-in function `chr()` with common usecases.


```python
chr(97)  # 'a'
```

---

## ord()

**Description:** Built-in function `ord()` with common usecases.


```python
ord('a')  # 97
```

---

