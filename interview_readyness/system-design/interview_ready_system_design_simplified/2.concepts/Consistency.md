# 📏 Linearizable Consistency

## ✅ Definition

**Linearizability** (also known as **atomic consistency**) is the **strongest consistency model** in distributed systems. It guarantees that **operations appear to occur instantaneously at some point between their start and end time**.

In other words:

> Every read reflects the **most recent completed write** as if all operations were executed **sequentially** in **real-time order**.

---

## 🧠 Key Properties

- **Single global order** of operations
- **Real-time** awareness: if one operation completes before another begins, then that order is preserved
- Ensures **atomic visibility**: once a write is visible, it’s visible to all

---

## 📦 Example

Let’s say we have a distributed key-value store.

T1: Client A writes x = 5
T2: Client B reads x → gets 5 ✅

Even if they are served by **different replicas**, Client B’s read reflects the latest write because linearizability guarantees a single consistent timeline.

---

## ⛓️ Difference from Other Models

| Model           | Real-Time Order Preserved | All Clients See Same Order | Example   |
|----------------|---------------------------|-----------------------------|-----------|
| **Linearizable** | ✅ Yes                    | ✅ Yes                      | Strongest |
| **Sequential**   | ❌ No (can be reordered) | ✅ Yes                      | Weaker    |
| **Eventual**     | ❌ No                    | ❌ No                      | Weakest   |

---

## ⚠️ Trade-offs

- **Pros:**
  - Easier reasoning for developers
  - Ensures **predictability** and **correctness** in financial or critical systems

- **Cons:**
  - Expensive in terms of **latency and availability**
  - Cannot be achieved in presence of **network partitions** (as per the **CAP theorem**)

---

## 🔁 In Practice

Systems like:

- **Etcd**
- **ZooKeeper**
- **Consul**

aim to provide **linearizable reads/writes** for coordination and configuration management.

---

## 🧪 Test: Is a system linearizable?

You can test a system’s linearizability by checking:

- Are operations appearing to take effect in **real-time order**?
- Is **there a single timeline** of events that respects start and end times?

Tools like [Jepsen](https://jepsen.io) are often used to test consistency models.

---

## 📚 Summary

- Linearizability = **Strong consistency + Real-time ordering**
- Great for: **critical systems, leader election, locks**
- Costly: comes with **performance and availability trade-offs**


# 🚧 Head-of-Line (HOL) Blocking

## ✅ Definition

**Head-of-Line Blocking** occurs when the **first request** in a queue is delayed, which **blocks all subsequent requests**, even if they could have been processed independently.

> In other words, the entire line gets **stuck behind a slow request** at the front.

---

## 🧠 Where It Happens

### 1. **Networking**
- **TCP** is a reliable protocol that delivers packets **in order**.
- If a packet is lost, **all following packets must wait**, even if they’ve already arrived.
- This causes latency and poor throughput.

### 2. **HTTP/1.1**
- Uses **pipelining** over a single TCP connection.
- If the **first response** is slow, all subsequent responses are delayed.
- Solution: **HTTP/2** introduces multiplexing to solve this.

### 3. **Queues (Message Brokers, DBs)**
- In FIFO queues, one slow message **blocks the entire queue**.
- If consumer logic is slow or faulty, the system can **back up**.

---

## 📦 Example (Networking)

Imagine you're loading 3 images over HTTP/1.1:

Image1 -> delayed 3s
Image2 -> ready in 100ms
Image3 -> ready in 100ms


Since Image1 is at the front of the pipeline, Image2 and Image3 **wait** even though they are fast. That’s HOL blocking.

---

## ⚠️ Problems Caused

- Increased latency
- Reduced throughput
- Poor resource utilization
- Bad user experience

---

## 🛠️ Solutions

| Context        | Solution                          |
|----------------|-----------------------------------|
| **TCP**        | Use **QUIC** or UDP protocols     |
| **HTTP/1.1**   | Upgrade to **HTTP/2 or HTTP/3**   |
| **Queues**     | Use **priority queues**, **sharding**, or **multiple consumers** |
| **Switches**   | Use **Virtual Output Queuing (VOQ)** to isolate head blockage |

---

## 🧪 Summary

- **HOL Blocking = One slow item blocks everything behind it**
- Common in **networking, queues, protocols**
- Solved using **parallelism**, **multiplexing**, and **protocol upgrades**

> Optimize systems to avoid putting critical paths behind slow operations!

# 🌐 Eventual Consistency

## ✅ Definition

**Eventual Consistency** is a **weak consistency model** used in distributed systems. It guarantees that, **if no new updates are made to a given data item**, **all accesses will eventually return the last updated value**.

> In simple terms: **all replicas will become consistent... eventually**.

---

## 🧠 Key Characteristics

- **No guarantee of immediate consistency**
- **Updates propagate asynchronously**
- Reads might return **stale data**
- **High availability and partition tolerance** (as per the CAP theorem)

---

## 📦 Example

A user updates their profile picture.

- Region A server gets the update.
- Region B still shows the old picture.
- After some time, the update **replicates**, and both regions show the new picture.

This **delay in propagation** is allowed under eventual consistency.

---

## ⏱️ Real-World Analogy

Think of **WhatsApp status sync**:
- You post a status
- It might take a few seconds to appear on a friend's phone
- But eventually, it shows up the same for everyone ✅

---

## 🔁 Use Cases

- **DNS** (Domain Name System)
- **Amazon DynamoDB**
- **Cassandra**
- **Couchbase**
- **Shopping carts**, **social feeds**, **caches**

---

## 🔄 Eventual vs Strong Consistency

| Feature                | Eventual Consistency     | Strong Consistency (Linearizable) |
|------------------------|--------------------------|------------------------------------|
| Read after write       | Might be stale           | Always up to date                  |
| Availability           | High                     | Lower                              |
| Performance            | Fast                     | Slower                             |
| Use case               | Fault-tolerant systems   | Critical systems (e.g. banking)    |

---

## ⚠️ Caveats

- Application logic must tolerate **temporary inconsistency**
- May require **conflict resolution mechanisms** (e.g., **last write wins**, **vector clocks**)
- Harder to reason about correctness

---

## 🛠️ Techniques to Manage

- **Read Repair**: Fix stale data during reads
- **Anti-Entropy**: Periodic sync between replicas
- **Quorum Reads/Writes**: Read from/write to majority

---

## 📚 Summary

- **Eventually consistent systems** sacrifice immediate consistency for **availability** and **partition tolerance**
- Perfect for **high-scale**, **distributed** environments where **latency and uptime** are critical
- Must be **carefully designed** to handle **inconsistencies** gracefully

> Not everything needs to be strongly consistent. Know your system’s trade-offs.

# 🔗 Causal Consistency

## ✅ Definition

**Causal Consistency** is a **middle-ground consistency model** that ensures **causally related operations are seen in the same order by all nodes**, but **concurrent operations may be seen in different orders**.

> If one operation **causes** another, all observers must see them in that causal order.

---

## 🧠 Key Concepts

- **Causal relationship**: If Operation A happens-before Operation B, then B is **causally dependent** on A.
- Independent or **concurrent operations** can be seen in **any order**.
- Guarantees:
  - **Read-your-writes**
  - **Monotonic reads**
  - **Writes-follow-reads**

---

## ⛓️ Example

```
User A: Post "Hello world!" → Post ID: 1
User B: Likes Post 1 → Like depends on Post 1
```

All users must see the **post before the like**, because the like **causally depends** on the post.

However, if:
- User C posts "Good Morning"
- User D comments on an unrelated post

These can be observed in **any order**, because they are **independent** events.

---

## 🔁 Where It’s Used

- **Social media feeds**
- **Collaborative editing tools**
- **CRDTs (Conflict-free Replicated Data Types)**
- **Systems like COPS, Bayou, and some Dynamo-style databases**

---

## ⚖️ Causal vs Eventual vs Strong Consistency

| Feature                | Causal Consistency        | Eventual Consistency       | Strong Consistency       |
|------------------------|---------------------------|-----------------------------|---------------------------|
| Order of causally related ops | ✅ Preserved         | ❌ Not guaranteed           | ✅ Guaranteed              |
| Order of concurrent ops       | ❌ Not guaranteed     | ❌ Not guaranteed           | ✅ Single global order     |
| Availability                 | High                   | Highest                    | Lower                     |
| Complexity                  | Medium                 | Low                        | High                      |

---

## 🛠️ Implementation Techniques

- **Vector clocks**: Track causality with logical timestamps
- **Session guarantees**: Read-your-writes, monotonic reads, etc.
- **Dependency tracking** between updates and replicas

---

## 📚 Summary

- **Causal Consistency** = Respect causal order, relax order of unrelated events
- More intuitive for users (e.g., **likes don’t come before posts**)
- Strikes a balance between **availability**, **consistency**, and **performance**
- Stronger than eventual consistency, **weaker than linearizability**

> Useful when **user-perceived order matters**, but **performance and availability are also priorities**