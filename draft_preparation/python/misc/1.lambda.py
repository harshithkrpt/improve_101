from functools import reduce


list_number = [1,2,3,4,5]

result = list(map(lambda n: n ** 2, list_number))

print(result)


data_fruits = [(1, 'apple'), (2, 'citrus'), (3, 'banana')]

data_fruits.sort(key=lambda x: x[1])

print(data_fruits)

# filtering data

even = list(filter(lambda x: x % 2 == 0, list_number))

print(even)


def power(n):
    return lambda x: x ** n

square = power(2)
cube = power(3)

print(square(2))
print(cube(3))


print(reduce(lambda a,b: a + b, [1,2,3,4, 10]))

funcs = [lambda x: x + i for i in range(3)]

print([f(10) for f in funcs]) # [12, 12, 12]

# but as i is referencing same variable , pass in the default value so that it remembers its value
funcs_value = [lambda x,index=i: x + index for i in range(3)]
print([f(10) for f in funcs_value]) # [10, 11, 12]