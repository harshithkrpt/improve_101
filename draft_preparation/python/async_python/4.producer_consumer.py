# producer_consumer_threading.py
import threading
import queue
import time
import random

NUM_ITEMS = 10         # total items producer will produce
PRODUCER_DELAY = 0.2   # seconds between produces (simulated I/O)
CONSUMER_DELAY = 0.1   # seconds to "process" each item
SENTINEL = None        # sentinel value to signal consumer(s) to stop

def producer(q: queue.Queue, n_items: int):
    """Simulates fetching/generating n_items and putting them on the queue."""
    for i in range(n_items):
        time.sleep(PRODUCER_DELAY)                 # simulate I/O wait
        item = random.randint(1, 100)              # fetched/generated item
        q.put(item)
        print(f"[Producer] produced {item} (#{i+1}/{n_items})")
    # Put sentinel to tell consumer we're done
    q.put(SENTINEL)
    print("[Producer] done — sentinel put")

def consumer(q: queue.Queue, consumer_id: int = 1):
    """Consumes items from queue and processes them until sentinel is seen."""
    while True:
        item = q.get()                 # blocks until item available
        try:
            if item is SENTINEL:      # shutdown signal
                # If there might be multiple consumers, re-put sentinel for others:
                q.put(SENTINEL)
                print(f"[Consumer-{consumer_id}] received sentinel — exiting")
                break
            # Process item (square it)
            time.sleep(CONSUMER_DELAY)   # simulate processing
            result = item * item
            print(f"[Consumer-{consumer_id}] processed {item} -> {result}")
        finally:
            q.task_done()              # mark the queued task as done

def main():
    q = queue.Queue(maxsize=5)           # bounded to show blocking behavior
    prod = threading.Thread(target=producer, args=(q, NUM_ITEMS), name="Producer")
    cons = threading.Thread(target=consumer, args=(q, 1), name="Consumer-1")

    prod.start()
    cons.start()

    # Wait until all produced items have been processed
    q.join()          # blocks until q.task_done() called for every put()
    # At this point consumer received sentinel and exited; join threads:
    prod.join()
    cons.join()
    print("All done!")

if __name__ == "__main__":
    main()
