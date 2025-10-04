from multiprocessing import Pool
import time

def square(n):
    time.sleep(0.1)
    return n * n

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(square, range(100))
    print(results)
