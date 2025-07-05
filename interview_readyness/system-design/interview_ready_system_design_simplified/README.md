# System Design by GKCS

---

## Evaluation Criteria for System Design

When designing a system, we must evaluate the solution based on three key parameters:

1. **Simplicity**:  
   - Is the system easy to understand and maintain?
   - Are we avoiding unnecessary complexity?
   - Simpler systems are less error-prone and easier to scale and modify.

2. **Fidelity** (Requirement Coverage):  
   - Does the system meet all functional and non-functional requirements?
   - Are edge cases and scalability considered?
   - Ensures the design does not miss critical business needs.

3. **Cost Effectiveness**:  
   - Is the solution economically viable?
   - Are we avoiding overengineering or underutilizing resources?
   - Crucial for startups and small businesses with limited budgets.

---

## Cloud vs Local Machine (Server) – For Startups and Small Businesses

### Cloud Solution

- **Simplicity**: Cloud platforms (like AWS, GCP, Azure) offer serverless and managed services that reduce the need for infrastructure management.
- **Fidelity**: Both cloud and on-premise can offer similar fidelity in terms of functionality and features.
- **Cost**: Cheaper initially due to pay-as-you-go pricing, reduced operations cost, and built-in scalability.

#### Benefits:
- Serverless architectures reduce devops burden.
- Automatic scaling, managed services like databases, queues, and caching.
- Global accessibility and easier integration with CI/CD tools.

#### Drawbacks:
- Costs may increase at scale.
- Slightly higher latency compared to local hosting in specific regions.
- Less control over the underlying hardware.

### Local Server

- **Efficiency**: Can be faster and more responsive for small local user bases.
- **Complexity**: Higher setup and maintenance effort.
- **Cost**: Potentially higher upfront cost but predictable expenses.

---

## Where Are the Pages Hosted?

### UI Code Hosting

- **CDN (Content Delivery Network)**:  
  Examples: Akamai, CloudFront  
  - Ideal for hosting **static files** like HTML, CSS, JS, images, and videos.
  - Files are cached on edge servers across the globe, reducing latency.
  - Updates require cache invalidation, which might take time.

- **Cloud Hosting (AWS, GCP, etc.)**:  
  - Used for **dynamic content** such as APIs and server-side rendering.
  - Offers compute, storage, and advanced deployment options.
  - More expensive and complex than CDN hosting.

---

## How Are Files Added to the CDN?

- **Amazon S3** is commonly used as the origin storage.
- **CloudFront** (or similar) pulls files from S3.
- Diff checking ensures only changed files are updated.
- CDN then distributes the files across global edge servers.

---

## How Does the Internet Work?

1. User enters a domain (e.g., www.google.com).
2. Request goes through ISP to a **router**.
3. Router contacts the **DNS (Domain Name System)**.
   - DNS is like the phonebook of the internet.
   - Resolves domain names to IP addresses (e.g., facebook.com → 192.5.6.8).
4. Response returns with the resolved IP address.
5. Browser connects to that IP and loads the webpage.

### DNS Providers:
- GoDaddy
- Amazon Route 53
- Cloudflare

---

## What Kind of Database Should We Use?

### Recommendation:
- Choose a **database you’re comfortable with**.
- For most cases, start with **SQL** (e.g., PostgreSQL, MySQL).

### SQL vs NoSQL:

- **SQL**:
  - Relational, structured schema.
  - ACID compliance for transactional systems.
  - Great for analytics and complex queries.

- **NoSQL**:
  - Schema-less, supports horizontal scaling.
  - Good for document storage, key-value pairs, large-scale apps.
  - Examples: MongoDB, Cassandra, DynamoDB.

---


## How to Debug the Systems

Debugging and maintaining distributed systems is crucial for reliability. Here are key strategies:

### 1. Add Logging and Monitoring

- Capture logs at different levels (INFO, DEBUG, ERROR).
- Logs help track system behavior, errors, and performance issues.
- **Example Tool**: AWS CloudWatch, ELK Stack (Elasticsearch, Logstash, Kibana)

### 2. Observability and Anomaly Detection

- Observability is the ability to understand internal states from external outputs.
- Monitor metrics such as CPU usage, memory, request latency, error rates.
- **Example Tools**: Prometheus + Grafana, Datadog, New Relic

### 3. Business Analytics and Dashboards

- Visual tools to identify anomalies and trends in usage or performance.
- **Example Tools**: Power BI, Google Analytics, Looker

### Best Practices:

- Set up alerts for threshold breaches.
- Implement distributed tracing for microservices (e.g., Jaeger, Zipkin).
- Maintain structured and centralized logging.

## How Reliable Is This System?

Reliability refers to the system’s ability to function correctly and consistently over time. Consider the following when evaluating reliability:

### 1. Single Point of Failure (SPOF)

- A **single point of failure** is any component that, if it fails, brings down the entire system.
- **Example**: If your system relies on one database instance without a replica, database failure causes a full outage.

### Strategies to Avoid SPOFs:
- Use load balancers with multiple backend instances.
- Implement database replication and automatic failover.
- Ensure high availability zones and redundancy.

### 2. External Dependencies

- Any **third-party service** your system depends on (e.g., payment gateways, CDN, email services) is a potential failure point.
- Even if your internal system is robust, an external service outage can impact users.

### Mitigation Techniques:
- Implement retries and exponential backoff.
- Fallback mechanisms and circuit breakers (e.g., Hystrix).
- Use service meshes like Istio for better control over service communication.

---
