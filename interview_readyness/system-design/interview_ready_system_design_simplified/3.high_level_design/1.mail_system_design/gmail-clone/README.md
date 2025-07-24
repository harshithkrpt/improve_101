
# Gmail System Design - Documentation

![System Diagram](./gmail_system_architecture.png)

---

## 📌 Key Requirements
- User Registration & Two-Factor Authentication
- Email Send/Receive with Attachment Support
- Keyword-Based Search
- Spam and Virus Detection
- Contact & Group Management

---

## 🧱 High-Level Components

### 1. Gateway Service
- Entry point for all requests.
- Handles IP blocking and request translation.

### 2. Service Manager
- Registers all services with heartbeat monitoring.
- Routes external/internal requests.

### 3. Authentication Service
- Handles login, registration, and 2FA validation.

### 4. Message Service
- Sends OTP via email/SMS.
- Stores message templates.

### 5. Profile Service
- Manages user profiles and profile pictures.

### 6. Email Service
- Sends and receives emails.
- Publishes to message queue.

### 7. Message Queue
- Enables asynchronous processing for services like spam, search, and preferences.

### 8. Search Engine
- Uses inverted index for keyword-based email search.

### 9. Spam Detector
- Classifies email based on subject, content, and frequency.

### 10. Virus Detector
- Scans attachments for malware.

### 11. Distributed File Service
- Stores and serves email attachments.

### 12. Contacts Manager
- Maintains mappings of senders and receivers for contacts and groups.

### 13. IMAP & SMTP Servers
- Handles external communication.

---

## ⚙️ Design Trade-offs

| Component           | Decision                                    | Reason                                                                 |
|--------------------|---------------------------------------------|------------------------------------------------------------------------|
| Service Registry    | Use service manager                         | Reduces gateway load, improves modularity                             |
| Token Storage       | Use distributed cache                       | Avoids cache duplication and update fan-out in memory                 |
| Spam/Virus Checking | Asynchronous via message queue              | Scalability and fault isolation                                       |
| Attachments Storage | Distributed file system                     | Redundancy and fast retrieval                                         |

---

## 📊 Capacity Estimation

### Storage Per Day
- **Emails**: ~20TB
- **Attachments**: ~5PB
- **Total (3x redundancy)**: ~15PB → Optimized to ~4.5PB with de-duplication and compression

### Profile Storage
- Without images: ~100GB
- With images: ~20TB → Total with redundancy: ~60TB

### Processing Power (Per Day)
- **Virus Checker**: Needs ~6000 parallel processes
- **Spam Detector**: Needs ~24 processes

### Cache for Contacts
- Active users: 20M
- Estimated cache: 200GB → ~120 machines (with redundancy and locality)

---

## ✅ API Contracts Summary

See PDF for full API contract list (Auth, Profile, Email, Contacts, Drive, Search Engine).

---


## 🚀 Project Overview

A beginner-friendly, full-stack Gmail-like system built using **Docker**, **Kubernetes**, and **Nginx**, along with Redis, MySQL, and various microservices.

---

## ⚙️ Tech Stack

| Layer               | Tools                                                  |
|---------------------|--------------------------------------------------------|
| **Frontend**         | React.js                                               |
| **API Gateway**      | Nginx                                                  |
| **Containerization** | Docker                                                 |
| **Orchestration**    | Kubernetes (Minikube or kind)                          |
| **Message Queue**    | RabbitMQ or Kafka                                      |
| **Search**           | Elasticsearch                                          |
| **Cache**            | Redis                                                  |
| **Databases**        | MySQL                                                  |
| **File Storage**     | MinIO or Persistent Volume                             |
| **Auth**             | JWT + Redis                                            |

---

## 🧱 Microservices Architecture

| Service Name         | Description                                            |
|----------------------|--------------------------------------------------------|
| `gateway-service`     | Nginx reverse proxy to all microservices               |
| `auth-service`        | Signup/Login, JWT tokens, Redis session store          |
| `profile-service`     | User profiles, images (MinIO or DB)                    |
| `email-service`       | Compose, send, receive emails via SMTP/IMAP            |
| `message-service`     | OTP, SMS templates, internal messaging via MQ          |
| `contacts-service`    | Contact and group management                           |
| `search-service`      | Elasticsearch-based email search                       |
| `virus-checker`       | Simulate file scan (ClamAV or mock)                    |
| `file-service`        | Upload/download attachments                            |
| `service-manager`     | Service registry & heartbeat manager                   |
| `spam-detector`       | Flag spam (Bayesian or rule-based for now)             |

---

## 📁 Folder Structure

```
gmail-clone/
├── docker-compose.yml
├── nginx/
│   └── default.conf
├── k8s/
│   ├── gateway.yaml
│   ├── auth.yaml
│   └── ...
├── services/
│   ├── auth-service/
│   ├── email-service/
│   ├── profile-service/
│   └── ...
├── redis/
├── mysql/
├── elasticsearch/
└── frontend/
```

---

## 🧪 Development Milestones

| Milestone              | Tasks                                                        |
|------------------------|--------------------------------------------------------------|
| 🔐 **Auth Service**     | JWT Auth, Redis session, 2FA (email OTP)                     |
| 👤 **Profile Service**  | Profile CRUD, picture upload, MinIO or FS                    |
| 📧 **Email Service**    | Send/Receive emails using SMTP & IMAP                        |
| 📂 **File Upload**      | File upload, virus scan simulation                           |
| 🔎 **Search Service**   | Use Elasticsearch to index email content                     |
| ✉️ **Message Queue**    | Use RabbitMQ or Kafka for spam/virus/search queue            |
| 🛡️ **Spam/Virus Checker** | Background services consuming email events                 |
| 📬 **Contacts Service** | Store user contacts in MySQL                                 |
| 📥 **Inbox Page**       | Show paginated, searchable emails using tag and keyword      |

---

## 🔁 Docker & Kubernetes

### Docker
- Individual `Dockerfile` for each service.
- Use `.dockerignore`, multi-stage builds.

### Kubernetes
- Minikube or kind for local development.
- YAML configs: `Deployment`, `Service`, `ConfigMap`, `Secrets`, `PV`

### Nginx Example Config

```nginx
location /auth/ {
    proxy_pass http://auth-service:3000/;
}
location /profile/ {
    proxy_pass http://profile-service:3000/;
}
```

---

## 🧠 Concepts Covered

| Concept               | Where It's Applied                                          |
|------------------------|-------------------------------------------------------------|
| **Nginx LB**          | Fronting all microservices                                   |
| **Docker**            | Each service containerized                                   |
| **Kubernetes**        | Orchestration, scaling, health checks                        |
| **Redis**             | Session storage, spam result cache                           |
| **MySQL**             | Structured data: Users, profiles, email metadata             |
| **Elasticsearch**     | Full-text email search                                       |
| **Service Discovery** | Consul or custom heartbeat monitoring                        |
| **MQ (Kafka/Rabbit)** | Asynchronous email processing                                |
| **Virus Scanner**     | ClamAV or simulation                                         |
| **2FA**               | OTP via email/message-service                                |

---

## 📌 Next Steps

You can now:
- Develop each microservice step by step.
- Use Docker Compose to test locally.
- Deploy to Kubernetes with Nginx Gateway.

Happy Coding! 🚀
