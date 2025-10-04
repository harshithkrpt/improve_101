from multiprocessing import Process, Queue
import random
import time


def producer(q):
    for _ in range(10):
        item = random.randint(1,100)
        q.put(item)
        print("Item Added -> ", item)
        time.sleep(0.5)
    q.put(None)


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"consumer calc {item} as -> {item**2}")
        time.sleep(0.1)
    

if __name__ == "__main__":
    q = Queue()
    p = Process(target=producer, args=(q,))
    c = Process(target=consumer, args=(q,))

    p.start()
    c.start()

    p.join()
    c.join()

    print("All Done!")