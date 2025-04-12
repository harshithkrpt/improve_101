def your_decorator(func):
    def wrapper():
        print("Before func!")
        func()
        print("After func!")
    return wrapper

@your_decorator
def foo():
    print('Hello World!')


foo()


# Decorator with arguments
def your_dec_args(func):
    def wrapper2(*args, **kwargs):
        print("Before func!")
        func(*args, **kwargs)
        print("After func!")
        
    return wrapper2

@your_dec_args
def foo(bar):
    print(bar)

foo("Harshith")


# TODO: Learn the advanced decorators concepts