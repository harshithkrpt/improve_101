name = "Hello World"

print(name)

print("\' \" \t \n \\ \b \ooo \r")

print(""" 
    We can write as many lines as we want
""")

# Indexing & slicing
print(name[0])
print(name[0:])
print(name[0:-1])
print(name[-1])

# Reverse 
print(name[::-1])


# In and Not In Operator

print("Name" in "Namaste Name")
print("Name" not in "Namaste Name")


# Method
print("name".upper())
print("NAME".lower())


# Join and Split
print(''.join(['name', 'one', '1']))
print(' '.join(['name', 'one', '1']))

print('This is my name'.split(' '))


print("Hello".rjust(10))
print("Hello".ljust(10))
print("Hello".center(10))

print("Hello".center(20, '-'))

# Strip
print("Hello   ".strip())

# Count
print("Hello".count('l'))

# Replace 
print("HELLI".replace('L', 'l'))

# String Formating


name = 'Harshith'
print("Name %s" % name)

number = 100
print("Number %d" % number)


print("This is name {} and some number {}".format(name, number))
print("This is number {1} and some name {0} and another number but simillar {1}".format(name, number))

print(f"Hello {name}, this is number {number}")

print(f"""

(
... f'Hi, {name}. '
... f'You have {number} unread messages'
... )
""")



from datetime import datetime
now = datetime.now().strftime("%b/%d/%Y - %H:%M:%S")
print(f'date and time {now}')
print(f'date and time {now=}')


# Formating digits
a = 100000
print(f'{a:,}')

# Rounding
a  = 0.4333
print(f'Rounding {a:.2f}')
print(f'Percentage {a:.2%}')