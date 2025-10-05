def gen_squares(n):
    for i in range(n):
        yield i*i

g = gen_squares(4)
print(next(g))  # 0
print(next(g))  # [1,4]
print(list(g))
print(list(g))
g = gen_squares(10)
print(list(g))

gexp = (x*x for x in range(5)) # generator
listexp = [x*x for x in range(5)]
print(gexp)
print(listexp)


class CountTo:
    def __init__(self, stop):
        self.stop = stop
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter >= self.stop:
            raise StopIteration
        val = self.counter
        self.counter += 1
        return val
    
print([i ** i for i in CountTo(4)])