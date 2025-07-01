# Any
print(any([0, False, True]))

# All
print(all([0, False, True]))

print(all([1,True,10]))

print(all((0,True, False)))

# bin -> convert integer to binary string
print(bin(10))

# bool return boolean value
bool(1) # True
bool(0) # False

# breakpoint()


# Enumerate
enumeratedObject = enumerate([1,2,3,4,5])

for index, item in enumeratedObject:
    print(index, item)

# Eval
print(eval("1 + 2"))

eval('print("Hello World!")')

# Filter

def is_even(num):
    return num % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]

# returns about filter object
print(filter(is_even, numbers))

print(list(filter(is_even, numbers)))

# Float 
print(float("3.44"))

# Format
print("Name {} and working in {}".format("Abc", 'Def'))
print("Name {1} and working in {0}".format("Abc", 'Def'))
print(f'Name {"Abc"} and working in {"Def"}')

# iter
iterator = iter([1,2,3,4,5])
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# len
print(len([1,2,3,4,5]))

# map -> map(func, iterables) & iterables are tuple , list , range, dictionary, set, string
def square(nums):
    numbers = map(lambda x: x * x, nums)
    return list(numbers)

print(square([1,2,3,4,5]))

# min
print(min([1,2,3,4,5]))

# max
print(max([1,2,3,4,5]))

# pow
print(pow(2,3))


list_name = [1,2,3,4,5]
print(list_name)

list_name[0]
print(list_name[0:3])
print(list_name[1:-1])
print(list_name[:])

print(sorted([3,3,1,693], reverse=True))

print(list(reversed(list_name)))

