import random

print(random.random())  
# Example output: 0.672345

fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))


print(random.sample(fruits, 2))
# Example output: ['banana', 'cherry']

print(random.choices(fruits, k=3))
# Example output: ['cherry', 'cherry', 'apple']

cards = ['A', 'K', 'Q', 'J', 10, 9]
random.shuffle(cards)
print(cards)

print(random.gauss(0, 1))  # mean=0, std_dev=1
print(random.expovariate(1/5))  # mean = 5
print(random.betavariate(2, 5))
print(random.normalvariate(10, 2))  # mean=10, std_dev=2
