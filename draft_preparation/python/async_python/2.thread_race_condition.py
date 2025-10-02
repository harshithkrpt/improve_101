import threading
import time

counter = 0

lock = threading.Lock()

def increment():
    for _ in range(10 ** 6):
        global counter
        with lock:
            counter = counter + 1

a = threading.Thread(target=increment)
b = threading.Thread(target=increment)
c = threading.Thread(target=increment)
a.start()
b.start()
c.start()
a.join()
b.join()
c.join()

print(counter)