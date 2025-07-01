names = ['lorem', 'ipsum', 'bypass', 'cathode']

new_names = []

for name in names:
    new_names.append(name.upper())

print(new_names)

lower_case = [name.lower() for name in names]
print(lower_case)

upper_case = [name.upper() for name in names]
print(upper_case)

# n_100 = [(a,b) for a in range(1,10) for b in range(1,4)]
# print(n_100)

start_with_c = [name for name in names if name.startswith('c')]
print(start_with_c)

# if else conditions -> if even square it else add
list_100 = list(range(1,101))
calc = [num * num if num % 2 == 0 else num + num for num in list_100]
print(calc)


# Set Comprehendions
b = {'abc', 'def'}
up = { s.upper() for s in b }
print(up)

# Dictionary Comprehendions
c = {
    'name': 'one',
    'naming': 'two'
}

d = {
    v: k
    for k, v in c.items()
}
print(d)

print(["{}:{}".format(k.upper(),v) for k,v in c.items()])