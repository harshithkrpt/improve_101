def double_resunt(fn):
    def res(*args, **kwargs):
        return 2 * fn(*args, **kwargs)
    return res


@double_resunt
def increment(n):
    return n + 1

print(increment(10))

# 3. Preserve metadata with functools.wraps
from functools import wraps

def verbose(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"calling {fn.__name__}")
        return fn(*args, **kwargs)
    return wrapper


# 4. Parameterized decorator (decorator factory)

def repeat(n):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(x):
    print(x)

say(10)


def log_method(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        print(f"In {self.__class__.__name__} class , {fn.__name__} called")
        return fn(self, *args, **kwargs)
    return wrapper


class Beware:
    @log_method
    def method_name(self):
        print("This is First Print")

b = Beware()
b.method_name()


class memoize:
    def __init__(self, fn):
        wraps(fn)(self)
        self.fn = fn
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        result = self.fn(*args)
        self.cache[args] = result
        return result



import time

def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = fn(*args, **kwargs)
        dt = time.perf_counter() - t0
        print(f"{fn.__name__} took {dt:.6f}s")
        return result
    return wrapper


@timeit
@memoize
def fib(n):
    if n < 2: return n
    return fib(n - 1) + fib(n - 2)

print(fib(10) == 55)