# Comparision Operators
print(10 == 20)
print(10 != 20)
print(10 > 20)
print(10 < 20)
print(10 >= 20)
print(10 <= 20)
print(42 == 42.0) 

# Boolean Operators - and , or & not
True and True
True and False
False and True
False and False

True or True
True or False
False or True
False or False

not True
not False

name = "one"

# name = "two"

if name == "One".lower():
    print("it is one")
elif name == "two":
    print("it is two")
else:
    print("it is not one")

print("Hello World") if name == 'one' else print("Bye World") # ternary operator



# switch case
code = 204

match code:
    case 200 | 204:
        print("OK")
    case 201:
        print("Created")
    case 202:
        print("Accepted")
    case _:
        print("Not Found")
    

# match with length

length = [1,2,3]

match length:
    case [a]:
        print(a)
    case [a,b]:
        print(a,b)
    case [a,b,c]:
        print(a,b,c)
    case _:
        print("Not Found")


i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Done")


# while True:
#     inputName = input("What is your Name")
#     if len(inputName) < 5:
#         break



# while True:
#     inputName = input("What is your Name")
#     if len(inputName) < 5:
#         continue
#     print("Hello < 5")


for pet in ["Helo", 'balo', 'chao']:
    print(pet)


for i in range(5):
    for j in range(5):
        print(i,j)
   
print(list(range(5)))


for i in range(0, 20, 2):
    print(i)

for i in range(5, 0, -1):
    print(i)
else:
    print("Done")


