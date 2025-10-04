# producer_consumer_multi_producer_multi_consumer.py
"""
Multi-producer / multi-consumer demo with instrumentation.

- Multiple producers each produce ITEMS_PER_PRODUCER items.
- After all producers finish, main places NUM_CONSUMERS sentinel objects (one per consumer).
- Each consumer processes items until it sees the sentinel, then exits.
- All queue puts (including sentinels) are paired with task_done() so q.join() works.
- Thread-safe counters track produced and consumed *real* items (not sentinels).
"""

import threading
import queue
import time
import random

# ---- CONFIG ----
NUM_PRODUCERS = 3
ITEMS_PER_PRODUCER = 5   # items per producer
NUM_CONSUMERS = 2

PRODUCER_DELAY = 0.05    # simulate I/O latency in producers
CONSUMER_DELAY = 0.02    # simulate processing time in consumers

QUEUE_MAXSIZE = 10

# unique sentinel so normal data can't equal it
SENTINEL = object()

# results storage: one list per consumer (indexed 0..NUM_CONSUMERS-1)
CONSUMER_SOL = [[] for _ in range(NUM_CONSUMERS)]

# instrumentation counters & locks (count only real data items, not sentinels)
produced_count = 0
produced_lock = threading.Lock()

consumed_count = 0
consumed_lock = threading.Lock()

# optional: record which producer produced which item (for debugging)
producer_logs = []   # list of tuples (producer_id, item_id, value)
producer_logs_lock = threading.Lock()


def producer(q: queue.Queue, producer_id: int, n_items: int):
    """Produce n_items and put them onto the queue."""
    global produced_count
    for i in range(1, n_items + 1):
        time.sleep(PRODUCER_DELAY)               # simulate I/O
        item_value = random.randint(1, 100)
        q.put((producer_id, i, item_value))      # put a tuple so data and provenance are obvious
        with produced_lock:
            produced_count += 1
        with producer_logs_lock:
            producer_logs.append((producer_id, i, item_value))
        print(f"[Producer-{producer_id}] put item #{i}: {item_value}")


def consumer(q: queue.Queue, consumer_id: int):
    """Consume until sentinel seen. Append processed results to CONSUMER_SOL."""
    global consumed_count
    while True:
        data = q.get()   # blocks until available
        try:
            if data is SENTINEL:
                # mark sentinel task done and exit (do not re-put sentinel)
                print(f"[Consumer-{consumer_id}] got sentinel -> exiting")
                break

            # data is (producer_id, item_id, value)
            producer_id, item_id, value = data
            # simulate processing work
            time.sleep(CONSUMER_DELAY)
            result = value * value
            CONSUMER_SOL[consumer_id - 1].append((producer_id, item_id, value, result))

            with consumed_lock:
                consumed_count += 1

            print(f"[Consumer-{consumer_id}] processed (P{producer_id}-#{item_id}) {value} -> {result}")
        finally:
            q.task_done()  # always call task_done(), including for sentinels


def main():
    q = queue.Queue(maxsize=QUEUE_MAXSIZE)

    # start consumers first (so they are ready)
    consumers = []
    for i in range(NUM_CONSUMERS):
        t = threading.Thread(target=consumer, args=(q, i+1), name=f"Consumer-{i+1}")
        t.start()
        consumers.append(t)

    # start producers
    producers = []
    for p in range(NUM_PRODUCERS):
        t = threading.Thread(target=producer, args=(q, p+1, ITEMS_PER_PRODUCER), name=f"Producer-{p+1}")
        t.start()
        producers.append(t)

    # wait for all producers to finish producing
    for p in producers:
        p.join()
    print("[Main] All producers finished producing.")

    # Now put one sentinel per consumer so each consumer will exit
    for _ in range(NUM_CONSUMERS):
        q.put(SENTINEL)

    # Wait until the queue is fully processed (this waits for all task_done calls)
    q.join()
    print("[Main] Queue join complete: all tasks (including sentinels) processed.")

    # Join consumers (they should exit after seeing sentinel)
    for c in consumers:
        c.join()

    # Summary / sanity checks
    expected_produced = NUM_PRODUCERS * ITEMS_PER_PRODUCER
    print("\n===== SUMMARY =====")
    print(f"Configured: producers={NUM_PRODUCERS}, items_per_producer={ITEMS_PER_PRODUCER}, consumers={NUM_CONSUMERS}")
    print(f"Produced count (instrumented) : {produced_count} (expected {expected_produced})")
    print(f"Consumed count (instrumented) : {consumed_count} (should equal produced)")
    total_consumed = sum(len(lst) for lst in CONSUMER_SOL)
    print(f"Sum of per-consumer processed items: {total_consumed}")
    print(f"Per-consumer breakdown (counts): {[len(lst) for lst in CONSUMER_SOL]}")

    # optional: sort and display a few processed items
    print("\nSample processed items (consumer_id -> (producer_id, item_id, value, squared))")
    for cid, lst in enumerate(CONSUMER_SOL, start=1):
        print(f" Consumer-{cid} processed {len(lst)} items; first 5 entries: {lst[:5]}")

    # cross-check invariants
    if produced_count != consumed_count:
        print("\nWARNING: produced_count != consumed_count — something's off!")
    else:
        print("\nInvariant holds: every produced data item was consumed exactly once. 🎉")

    # show producer logs for inspection (first 10)
    print("\nFirst 10 produced items (producer_id, item_id, value):", producer_logs[:10])


if __name__ == "__main__":
    main()
