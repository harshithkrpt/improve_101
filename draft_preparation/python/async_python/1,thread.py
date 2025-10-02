import threading
import time

def print_summary(name):
    for i in range(10):
        if name is not None:
            print(f"hello, {name}!")
        else:
            print("hello world!")
        time.sleep(1)
    
a = threading.Thread(target=print_summary, args=("Thread-A",))
b = threading.Thread(target=print_summary, args=("Thread-B",))
a.start()
b.start()
a.join()
b.join()
