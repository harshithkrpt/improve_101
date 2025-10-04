from multiprocessing import Process
import os
import time

def worker(n):
    print(f"Executing Process with {os.getpid()} with worker number {n}")
    time.sleep(10)
    print(f"Exiting Process with {os.getpid()} with worker number {n}")

if __name__ == "__main__":
    a = Process(target=worker, args=(1,), name="Python_Process_A")
    b = Process(target=worker, args=(2,), name="Python_Process_B")

    a.start()
    b.start()

    a.join()
    b.join()

    print("Completed!!!")