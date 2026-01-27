Here’s a clean, practical set of **notes on Apache Kafka**—focused on **topics, partitions, offsets, and data streams**. Think of Kafka as a very fast, very disciplined postal system for data, where nothing gets lost unless you explicitly throw it away.

---

## Big picture first (mental model)

Kafka is a **distributed event streaming platform**. Applications don’t talk to each other directly. They **publish events** to Kafka, and other applications **subscribe** to those events. Kafka sits in the middle, calmly buffering reality.

![Image](https://dz2cdn1.dzone.com/storage/temp/14018426-kafka-architecture-topics-producers-consumers.png)

![Image](https://daxg39y63pxwu.cloudfront.net/images/blog/apache-kafka-architecture-/image_589142173211625734253276.png)

![Image](https://i.imgur.com/hHJeiWX.png)

![Image](https://developer.confluent.io/698d59117f80f85dca31d38f0474a2a7/event-streaming-platform.svg)

---

## 1. Topics – the named streams of events

A **topic** is a **logical channel** where related events are written.

Think of a topic as:

* A folder
* A logbook
* A conveyor belt of messages

Examples:

* `user-signups`
* `order-events`
* `payment-transactions`

Important properties:

* Topics are **append-only** (events are never changed).
* Topics are **durable** (stored on disk).
* Topics are **multi-producer, multi-consumer**.

Kafka does not care what your data *means*. It only guarantees how it is **stored, ordered, and delivered**.

---

## 2. Partitions – how Kafka scales

A topic is split into **partitions**.

Each partition is:

* An **ordered, immutable log**
* Written **sequentially**
* Stored on a broker

![Image](https://www.cloudkarafka.com/img/blog/apache-kafka-partition.png)

![Image](https://daxg39y63pxwu.cloudfront.net/images/blog/apache-kafka-architecture-/image_589142173211625734253276.png)

![Image](https://miro.medium.com/1%2AxnGngkxdXB9MImIFZwpT8Q.png)

![Image](https://camo.githubusercontent.com/659dd04c092f0e94f4e861651c8ee15f9e1a5a08fddd8d762f60acc91d183fb2/68747470733a2f2f696d6167652e6175746f6d712e636f6d2f77696b692f626c6f672f6b61666b612d6c6f67732d636f6e636570742d686f772d69742d776f726b732d666f726d61742f312e706e67)

Why partitions exist:

* **Parallelism** → many consumers can read at once
* **Scalability** → data spread across machines
* **Performance** → sequential disk writes are fast

Key rules:

* **Order is guaranteed only within a partition**
* No ordering guarantee **across partitions**

Example:

```
Topic: orders
Partitions: orders-0, orders-1, orders-2
```

---

## 3. Offsets – Kafka’s idea of position

An **offset** is a **monotonically increasing number** assigned to each message **within a partition**.

Example:

```
Partition 0:
offset 0 → event A
offset 1 → event B
offset 2 → event C
```

Key ideas:

* Offset is **not global**, only per partition
* Offset is **not deleted when read**
* Offset is **controlled by the consumer**

Kafka doesn’t ask:

> “Did you process this message?”

It asks:

> “What offset do you want next?”

This is why Kafka is powerful—and unforgiving.

---

## 4. Consumers and Consumer Groups

A **consumer** reads data from topics.
A **consumer group** is a set of consumers working together.

Rules inside a consumer group:

* One partition → consumed by **only one consumer**
* One consumer → can read **multiple partitions**

![Image](https://cloudurable.com/images/kafka-architecture-consumer-group-to-partition.png)

![Image](https://editor.analyticsvidhya.com/uploads/36339Screen%20Shot%202022-07-25%20at%201.05.14%20PM.png)

![Image](https://tomlee.co/img/KafkaRebalance.png)

![Image](https://www.tothenew.com/blog/wp-ttn-blog/uploads/2023/11/first-1.jpeg)

Why this matters:

* Horizontal scaling is trivial
* If a consumer dies, Kafka **rebalances**
* No duplicate processing *within a group*

Different consumer groups can read the **same topic independently**.

---

## 5. Data streams – what Kafka really gives you

A **data stream** in Kafka is:

> A continuous, ordered (per partition), immutable sequence of events.

Kafka streams are:

* **Unbounded** (no fixed end)
* **Replayable** (rewind offsets)
* **Time-ordered** (by write time)

This enables:

* Event sourcing
* Stream processing
* Real-time analytics
* Audit logs
* Microservice decoupling

Kafka treats time as a **first-class concept**, not an afterthought.

---

## 6. Retention – why data doesn’t disappear immediately

Kafka stores data based on **retention policies**, not consumption.

Retention types:

* **Time-based** (e.g., keep 7 days)
* **Size-based** (e.g., keep 100 GB)
* **Compaction** (keep latest value per key)

This means:

* Consumers can crash and restart
* New consumers can read old data
* Debugging becomes archaeology, not guesswork

---

## 7. Ordering & keys – subtle but critical

If you send messages **with a key**:

* Same key → same partition
* Order is preserved for that key

Example:

```
key = userId
→ all events for one user stay ordered
```

Without a key:

* Kafka distributes messages round-robin
* Order across related events is lost

This is the difference between:

* “User paid before order confirmed”
* and
* “Reality, but shuffled”

---

## 8. Why Kafka feels different from queues

Kafka is **not** a traditional queue.

| Traditional Queue           | Kafka                |
| --------------------------- | -------------------- |
| Messages deleted after read | Messages retained    |
| One consumer gets message   | Many consumer groups |
| Pull until empty            | Continuous stream    |
| Hard to replay              | Replay by offset     |

Kafka is closer to a **distributed commit log** than a queue.

---

## One-sentence summaries (for memory)

* **Topic**: A named stream of events
* **Partition**: An ordered log that enables scale
* **Offset**: Your position in that log
* **Consumer group**: Parallel readers without duplication
* **Data stream**: Replayable, immutable event history

Kafka doesn’t move data *between* services.
It records **what happened**, and lets services decide **what to do about it**.

That philosophical shift is why Kafka quietly runs half the modern internet.
