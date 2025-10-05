class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person named {self.name}"
    
    def __repr__(self):
        return f"Person(name={self.name!r})"

p = Person("Harshith")
print(p)        # Person named Harshith
print(repr(p))  # Person(name='Harshith')


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(2, 3)
print(v1 + v2)   # Vector(3, 5)
print(v1 == v2)  # False

# __truediv__
# __floordiv__
# __lt__
# __gt__
# __hash__

class MyList:
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]
    
    def __iter__(self):
        return iter(self.data)

ml = MyList([1,2,3])
print(len(ml))      # 3
print(ml[1])        # 2
for x in ml:
    print(x)
