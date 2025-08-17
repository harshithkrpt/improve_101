# Database Sharding Notes

## What is Database Sharding?

Database sharding is the process of dividing the data into partitions
which can then be stored in multiple database instances.\
It uses a key (an attribute of the data) to partition the data.

### Example (Range-Based Sharding)

-   Suppose there are **1000 users** and **5 database servers**.\
-   Shard by `userID`:
    -   userID 000--199 → Database 1\
    -   userID 200--399 → Database 2\
    -   userID 400--599 → Database 3\
    -   userID 600--799 → Database 4\
    -   userID 800--999 → Database 5

If `userID = 546` performs read/write operations → only connects to
**Database 3**.\
Since the dataset per server is smaller, queries are faster.

------------------------------------------------------------------------

## Types of Sharding Architectures

### 1. Range-Based Sharding

-   Partition data based on ranges of the key.\
-   ✅ Easy to implement.\
-   ❌ Data may not be evenly distributed.

### 2. Key-Based / Hash-Based Sharding

-   Use a **hash function** of the key to determine the shard.\
-   Example: `h(x) = x % 3`.\
-   ✅ Simple, distributes data fairly.\
-   ❌ Risk of uneven distribution → solved by **Consistent Hashing**.

### 3. Directory-Based Sharding

-   Use a **lookup table** to map keys to shards.\
-   ✅ More flexible than range/hash-based sharding.\
-   ❌ Lookup table = **single point of failure**.

------------------------------------------------------------------------

## Horizontal Partitioning vs Sharding

-   **Horizontal Partitioning** → split table into multiple tables in
    **same database instance**.\
-   **Sharding** → split table across **multiple database instances**.

Key differences:\
- Partitioned tables in same DB → different names.\
- Sharded tables in different DBs → same names allowed.

------------------------------------------------------------------------

## Advantages of Sharding

-   **High Availability** → if one shard fails, others still work.\
-   **Security** → different shards = different access controls.\
-   **Faster Query Processing** → smaller datasets & indexes.\
-   **Increased Read/Write Throughput** → parallelism across shards.\
-   **High Scalability** → spreads load across machines, reduces memory
    & network bottlenecks.

------------------------------------------------------------------------

## Disadvantages of Sharding

-   **Complexity** → routing queries to correct shard adds overhead.\
-   **Transactions & Rollbacks** → not possible across multiple shards.\
-   **Joins Across Shards** → expensive & slow.\
-   **Higher Infrastructure Cost** → requires multiple machines.\
-   **Hierarchical Sharding Challenges** →
    -   Fixed shard count makes scaling difficult.\
    -   Some shards may grow too large → need re-sharding.

------------------------------------------------------------------------

## Hierarchical Sharding

-   Shards can be partitioned further using another method
    (range/hash).\
-   Example: First level → Directory-based, then **Shard 0** → further
    divided using **key-based sharding**.

------------------------------------------------------------------------

## Master-Slave Architecture (for High Availability)

-   **Writes** → handled by master.\
-   **Reads** → distributed across slaves.\
-   If master fails → slaves elect a new master.\
-   Ensures **fault tolerance** & **availability**.

------------------------------------------------------------------------