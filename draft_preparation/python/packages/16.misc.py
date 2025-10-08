from decimal import Decimal, getcontext

# Set precision (number of digits)
getcontext().prec = 6

x = Decimal('1.1')
y = Decimal('2.2')
print(x + y)       # 3.3 exactly!
print(1.1 + 2.2)   # 3.3000000000000003 (float inaccuracy)

from fractions import Fraction

a = Fraction(1, 3)
b = Fraction(2, 3)

print(a + b)  # 1
print(a * b)  # 2/9


import itertools as it

# Infinite iterators
count = it.count(start=10, step=2)
print(next(count))  # 10
print(next(count))  # 12

# Finite combinatorics
print(list(it.permutations([1, 2, 3], 2)))  # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]
print(list(it.combinations([1, 2, 3], 2)))  # [(1,2), (1,3), (2,3)]

# Utilities
print(list(it.chain([1, 2], [3, 4])))       # [1, 2, 3, 4]
print(list(it.cycle('AB')))                 # infinite loop (careful!)


from functools import lru_cache, partial, reduce

# Example 1: Caching function results
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # 55, computed fast due to memoization

# Example 2: Partial application
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25

# Example 3: Reduce
nums = [1, 2, 3, 4]
print(reduce(lambda a, b: a * b, nums))  # 24
