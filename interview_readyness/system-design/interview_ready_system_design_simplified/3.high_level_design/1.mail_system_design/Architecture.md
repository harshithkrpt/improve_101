
# 📬 Mini Gmail Clone - System Design & Implementation Guide

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