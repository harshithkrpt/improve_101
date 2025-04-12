def hello_word(name):
    print(f'Ciao {name}!')

hello_word("Harshith")

# Keyword arguments
def key(first, second):
    print(f'{first} {second}')

key(second="Harshith", first="Kurapati")


# return values

def square(num):
    if(num >= 0):
        return num * num
    print("Number should be >= 0")


print(square(2))
print(square(-2))


# Scope
globalV = "Access Everywhere"
def spam():
    global eggs
    eggs = 'spam'

spam()
print(eggs)


# Lambda Functions
var = lambda x,y: x * y

print(var(10, 20))