import contextlib

@contextlib.contextmanager
def con(num):
    print("Entering")
    yield num + 1
    print("Exit")

with con(2) as num:
    print(num)




# Class Based

class ConMan:
    def __enter__(self, *args, **kwargs):
        print("Entering")
    
    def __exit__(self, *args, **kwargs):
        print("Exit")

with ConMan() :
    print('hello')