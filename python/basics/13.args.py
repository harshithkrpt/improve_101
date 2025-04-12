def some_function(*args, **kwargs):
    if len(args):
        print(args)
    if len(kwargs):
        print(kwargs)


some_function(1,2,2)
some_function(one=2,two=3)