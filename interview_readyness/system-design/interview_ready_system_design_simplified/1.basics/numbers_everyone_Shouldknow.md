# ⚡ Numbers Everyone Should Know (System Design)

## 🖥️ CPU & Memory

  Operation                     Approx Time
  ----------------------------- -------------
  L1 cache reference            \~0.5 ns
  L2 cache reference            \~7 ns
  L3 cache reference            \~15 ns
  Main memory (RAM) reference   \~100 ns
  Mutex lock/unlock             \~25 ns

------------------------------------------------------------------------

## 💾 Storage (Local Disk)

  Operation                Approx Value
  ------------------------ --------------------
  SSD sequential read      500 MB/s -- 3 GB/s
  SSD random read          \~100 µs (0.1 ms)
  HDD sequential read      50 -- 200 MB/s
  HDD random seek (read)   5 -- 10 ms
  Write 1 MB to SSD        \~1 ms

------------------------------------------------------------------------

## 🌐 Networking

  Operation                           Approx Value
  ----------------------------------- --------------
  Datacenter round-trip (same rack)   \~0.5 ms
  Cross-datacenter round-trip         40--100 ms
  Send 1 KB over 1 Gbps network       \~10 µs
  Send 1 MB over 1 Gbps network       \~10 ms
  Send 1 MB over 10 Gbps network      \~1 ms

------------------------------------------------------------------------

## 📦 Database Operations

  Operation                                      Approx Time
  ---------------------------------------------- -------------
  In-memory KV lookup (Redis/Memcached)          \~0.1 ms
  SQL query (single row, no index, cold cache)   \~10 ms
  SQL query (indexed, warm cache)                \~1 ms
  Cross-shard query (distributed DB)             100+ ms

------------------------------------------------------------------------

## 📱 User Perception Thresholds

  Threshold   Meaning
  ----------- ----------------------
  100 ms      Feels instantaneous
  \<1 s       Flow uninterrupted
  \~10 s      User loses attention

------------------------------------------------------------------------

## 📊 Back-of-the-envelope Data Sizes

  Item                Approx Size
  ------------------- -------------
  Integer             4 bytes
  UUID                16 bytes
  Tweet (no media)    \~300 bytes
  Email (text only)   \~75 KB
  HD Photo (JPEG)     2--5 MB
  1 min of HD video   \~100 MB

------------------------------------------------------------------------

## 🔢 Rule-of-Thumb Scaling

  Metric                                          Approx Value
  ----------------------------------------------- ------------------------
  1 commodity server (32 cores, 64--128 GB RAM)   10k--100k HTTP req/sec
  Concurrent TCP connections/server               \~100k
  CDN latency reduction                           50--90%
  Cache hit ratio                                 80--95% realistic

------------------------------------------------------------------------

# 📌 Why These Matter

-   Estimate **bottlenecks quickly** (RAM vs network vs disk).\
-   Decide **caching, sharding, denormalization** needs.\
-   Helps in **capacity planning** (e.g., "Can 3 servers handle 10M
    req/day?").