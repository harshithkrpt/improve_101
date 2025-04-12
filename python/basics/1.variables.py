addition = 2 + 3
multiplication = 2 * 3
subtraction = 2 - 3
division = 2 / 3
print(addition)
print(multiplication)
print(subtraction)
print(division)

integer_division = 5 // 2
print(integer_division)

remainder = 5 % 2
print(remainder)

exponentiation = 2 ** 3
print(exponentiation)

# assignment
vars = 0 
vars += 1
print(vars)


addition += 1
print(addition)
multiplication *= 2
print(multiplication)  
subtraction -= 1
print(subtraction)
division /= 2
print(division)
integer_division //= 2
print(integer_division)
remainder %= 2
print(remainder)
exponentiation **= 2
print(exponentiation)

# Walrus Operator - in a expression while returning the variable
print(add_val:= 2 + 3) # 5
print(add_val) 


# Data Types
-2 # integer
1.25 # floating point numbers
'a' # strings

new_variable = 'name' + 'true'
concatation = 'name ' 'two' 'three'
repeating = 'name' * 4

print(concatation)
print(repeating)

# This is a comment

#  Multi 
#  Line

a = 1 # code with a comment

# Function DocString
def name():
    """
        This is a Function Doc String
            Function Name
    """
    print(name.__doc__)

name()


# End keyword
phrase = ['name','one','two','three','four']
for word in phrase:
    print(word, end="-")


# Sep
print('cats', 'dogs', 'mice', sep=',')

# Input Function Takes a data in the terminal
# my_name = input("What is your name? ")
# print("Hi, {}".format(my_name))

# print(f"nameing {my_name}")


# Length Function 
print(len('name'))
print(len([1,2,3,4,5])) 


# Inbuild functions
str(20) # '20'
str(20.5) # '20.5'

int('20') # 20
float('20.5') # 20.5

bool(1) # True
bool(0) # False

abs(20) # 20
abs(-20) # 20

