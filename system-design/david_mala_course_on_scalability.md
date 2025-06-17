# 🚀 Lecture Notes: Web Scalability & Architecture
_From a single server to a globally distributed, fault-tolerant system._

---

## 🌐 1. Web Hosting Options
Deploying an application starts with choosing the right hosting environment.

### Key Features to Look For
* **SFTP (Secure File Transfer Protocol):** A must-have for security. Unlike FTP, it encrypts your credentials and data.
* **Resource Guarantees:** Be skeptical of "unlimited" plans on the cheap; they almost always imply a shared, resource-constrained environment.

### Hosting Models
* **Shared Hosting:**
    * ✅ **Pro:** Very inexpensive.
    * ❌ **Con:** You compete for resources with other users. Not suitable for scaling.
* **Virtual Private Server (VPS):**
    * ✅ **Pro:** Guaranteed resources, more control, and better privacy.
    * ❌ **Con:** More expensive; the hosting company can still technically access your data.

---

## ⚖️ 2. Scaling Strategies
When traffic grows, you need a plan to handle the increased load.

### Vertical Scaling (Scaling Up)
> **Definition:** Adding more resources (CPU, RAM, Disk) to a **single machine**. It's like making one server more powerful.

* **Limitation:** You eventually hit a physical and financial ceiling. There's a limit to how powerful one machine can be.

### Horizontal Scaling (Scaling Out)
> **Definition:** Distributing the load across **multiple machines**. Instead of one powerful server, you use a fleet of cheaper ones.

* **Core Challenge:** How do you effectively distribute traffic across all the servers? This leads to load balancing.

---

## 🔀 3. Load Balancing
A load balancer acts as a "traffic cop" for your servers, distributing requests efficiently.

### Method 1: DNS Round Robin
* **How it works:** The DNS server cycles through a list of IP addresses, sending each new request to the next server in the list.
* **Pros:** Simple to configure.
* **Cons:** Not intelligent. It can't detect if a server is overloaded or down, and DNS caching can cause users to get "stuck" on one server.

### Method 2: Dedicated Load Balancer
* **How it works:** A single, dedicated service sits in front of your web servers. It receives all traffic and intelligently forwards it to the healthiest backend server.
* **Pros:** Smart routing, health checks, and improved security by hiding your internal network.
* **Challenge:** The load balancer itself becomes a **single point of failure**.
    * **Solution:** Use a redundant pair of load balancers (Active/Passive or Active/Active).

---

## 💾 4. The State Problem: Sticky Sessions
When you have multiple servers, user sessions become a major challenge.

* **The Problem:** If a user's shopping cart is on Server A, but their next click sends them to Server B, their cart appears empty.
* **"Sticky Sessions":** The goal is to ensure a user's requests are either always sent to the same server, or the session data is accessible to all servers.

### Solutions
1.  **Shared Storage:** All servers read/write session data from a central location (e.g., a shared database like MySQL or a file server).
2.  **Load Balancer Cookies:** The load balancer sets a cookie on the user's browser that tells it which server to send them back to on subsequent requests.

---

## ⚡ 5. Caching Strategies
Caching dramatically improves performance by storing frequently accessed data in a faster location (like RAM) to avoid slow operations (like disk reads).

* **File-Based Caching:** Pre-generating dynamic pages as static `.html` files. It's incredibly fast but makes site-wide updates very difficult.
* **Database Caching:** Using built-in features like the **MySQL Query Cache** to store the results of identical queries.
* **In-Memory Caching (e.g., Memcached):** A high-speed, key-value store that keeps data in RAM.
    * **Workflow:** Check the cache first. If data isn't there (a *cache miss*), get it from the database and then store it in the cache for next time.

---

## 🗄️ 6. Database Architecture & Redundancy
Your database is often the biggest bottleneck. Scaling it correctly is critical.

### Storage Redundancy (RAID)
* **RAID (Redundant Array of Independent Disks):** Protects against physical hard drive failure.
    * **RAID 1 (Mirroring):** An exact 1:1 copy of data is written to two drives. If one fails, the other keeps running.

### Database Replication
* **Master-Slave Replication:**
    * All writes go to the **Master**. The Master copies the data to **Slaves**.
    * ✅ **Benefit:** Excellent for read-heavy sites, as `SELECT` queries can be spread across many slaves.
    * ❌ **Weakness:** The Master is a single point of failure for writes.
* **Master-Master Replication:**
    * Two masters replicate to each other. Writes can go to either.
    * ✅ **Benefit:** Provides high availability for writes. If one master fails, the other takes over.

---

## 🏗️ 7. Putting It All Together: A Resilient Architecture
A professional, scalable architecture combines these concepts to eliminate single points of failure.

### A Typical Multi-Tier Architecture
1.  **Global DNS:** Directs users to the nearest physical data center.
2.  **Redundant Load Balancers:** An active/passive pair to handle incoming traffic and terminate SSL.
3.  **Web Tier:** A fleet of identical, stateless web servers.
4.  **Database Tier:** A cluster of replicated databases (e.g., a Master-Master pair for writes and multiple read slaves).
5.  **Redundant Networking:** All components are connected to redundant switches and power supplies.

### Security: The Principle of Least Privilege
* **Firewall Rules:** Strictly control what traffic is allowed between tiers.
    * `Internet -> Load Balancer:` Allow only ports **80 (HTTP)** & **443 (HTTPS)**.
    * `Web Servers -> Database:` Allow only port **3306 (MySQL)**.
* **Goal:** Compartmentalize the system. If a web server is compromised, the attacker's ability to access the database or other components is severely limited.