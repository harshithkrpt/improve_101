lists = ['apple', 'ball', 'cat', 'dog']

# Access
lists[0]

print(lists[-1])

lists.append("eagle")


print(lists)

# length
print(len(lists))

# change value 
lists[0] = "Apple"


# Concatanation
lists3 = lists + lists
print(lists3)

# Replication
lists2 = lists * 2
print(lists2)


# Enumerate
for index, item in enumerate(lists):
    print(index, item)


# Multiple Lists with zip
list1 = ['one', 'two', 'three']
list2 = [1,3,2]

for item,amount in zip(list1, list2):
    print(item, amount)

print('one' in list1)
print('one' not in list2)

one, two, three = list1
print(one)
print(two)
print(three)

a, b = 'one', 'two'
print(a)
print(b)


# index method 
print(list1.index('one'))

# insert at a given position
list1.insert(0, '01')

print(list1)

# deleting 
del list1[0]
print(list1)

# remove
list1.remove('one')
print(list1)



# pop
list1.pop()
print(list1)
list1.pop(0)
print(list1)


list2.sort()
print(list2)


# Lists are Mutable 
# Tuples are Immutable Objects

furniture = ('table', 'chair', 'sofa', 'shelf', 'mirror')
print(furniture[0])
print(len(furniture))

fur_list = list(furniture)
print(fur_list)


# Dictionary are the key value pairs simillar to hashMap data structures

my_cat = {
    'size': 'fat',
    'mat': 'rat',
    'dis': '3'
}

print(my_cat['size'])

my_cat['dis'] = '4'

print(my_cat)

print(my_cat.keys())
print(my_cat.values())
print(my_cat)

for key, value in my_cat.items():
    print(key, value)

for item_tuple in my_cat.items():
    print(item_tuple)


# get 
print(my_cat.get('size'))


if 'new_key' not in my_cat:
    my_cat['new_key'] = 'new_value'

print(my_cat)
print(my_cat.keys())
print(my_cat.values())
print(my_cat)


my_cat.pop('new_key')
print(my_cat)

my_cat.popitem()
print(my_cat)

my_cat.clear()
print(my_cat)


dict_two = {
    'dict': 'one'
}

merged  = {**my_cat, **dict_two}
print(merged)

# Sets

s1 = {1,2,3,2}
print(s1)

# passing list as constructor
s2 = set([1,2,3,2])
print(s2)

s2.add(3)
print(s2)

s2.remove(1)
print(s2)

# update 
s2.update([2,3,4,4,4,4])
print(s2)

s2.remove(4)
# s2.remove(4)

s2.discard(4)
print(s2)

# union
s3 = s1 | s2
print(s3)

# intersection
s4 = s1 & s2
print(s4)

# difference
s5 = s1 - s2
print(s5)

# symmetric difference
s6 = s1 ^ s2
print(s6)