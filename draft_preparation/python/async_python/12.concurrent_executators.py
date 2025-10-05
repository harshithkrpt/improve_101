# ProcessPoolExecutor = for cpu intensive things
from concurrent.futures import ThreadPoolExecutor, as_completed
import time, random

def do_work(n):
    t = random.random()
    time.sleep(t)
    return f"task slept for {t:.2f} sec", "Hello World ", random.random() 


def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(do_work, i) for i in range(10)]
        for f in as_completed(futures):
            print(f.result())

if __name__ == "__main__":
    main()
