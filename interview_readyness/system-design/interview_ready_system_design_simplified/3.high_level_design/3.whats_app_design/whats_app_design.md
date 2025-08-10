
# WhatsApp‑Style Messaging System — Deep‑Dive System Design

> A comprehensive, interview‑ready, production‑minded reference. Every **keyword** you see marked like **(see Glossary: _term_)** is defined at the end.

---

## Table of Contents
1. [Scope & Requirements](#scope--requirements)
2. [Assumptions & Capacity Estimation](#assumptions--capacity-estimation)
3. [High‑Level Architecture](#high-level-architecture)
4. [Client Connectivity & Protocols](#client-connectivity--protocols)
5. [Message Lifecycle](#message-lifecycle)
6. [Receipts: Sent/Delivered/Read](#receipts-sentdeliveredread)
7. [Presence & Last Seen](#presence--last-seen)
8. [Group Messaging](#group-messaging)
9. [Media Pipeline](#media-pipeline)
10. [Multi‑Device Sync](#multi-device-sync)
11. [Storage Model, Sharding & Indexing](#storage-model-sharding--indexing)
12. [Ordering, Consistency, Idempotency](#ordering-consistency-idempotency)
13. [Reliability, Retries & Backpressure](#reliability-retries--backpressure)
14. [Search & Message Discovery](#search--message-discovery)
15. [Notifications](#notifications)
16. [Security & End‑to‑End Encryption](#security--end-to-end-encryption)
17. [APIs & Events](#apis--events)
18. [Data Models](#data-models)
19. [Observability & SRE](#observability--sre)
20. [Scalability & DR](#scalability--dr)
21. [Failure Scenarios & Resilience](#failure-scenarios--resilience)
22. [Trade‑offs & Alternatives](#trade-offs--alternatives)
23. [Glossary](#glossary)

---

## Scope & Requirements

### Functional
- **1:1 chat** with receipts and **online/last‑seen** (see Glossary: _Presence_).
- **Groups** (small to large), mentions, replies.
- **Media**: images, audio, video, documents (see Glossary: _Object Storage_, _CDN_).
- **Message search** over recent history.
- **Multi‑device** (linked devices), **offline sync** and **reconnect** flows.
- **Push notifications** on mobile (see Glossary: _APNs_, _FCM_).
- **Rate limiting** and **abuse controls**.

### Non‑Functional
- **Low latency**: P50 < 100 ms gateway→gateway, P95 < 300 ms end‑to‑end.
- **High availability**: 99.99% **SLO** (see Glossary: _SLO_).
- **Scalable** to tens of millions of concurrent connections.
- **Privacy‑first**: end‑to‑end encryption (E2EE). Servers see only metadata needed to route.
- **Cost‑effective** media delivery via CDN and hot/cold storage tiers.

### Explicitly Out of Scope (for this doc)
- Account auth/phone verification.
- Voice/video calls.
- Payments.

---

## Assumptions & Capacity Estimation

- **DAU**: 50,000,000
- **Messages per DAU per day**: 40
- **Total messages/day**: 2,000,000,000
- **Average messages/sec**: 23,148.15 msg/s
- **Peak messages/sec** (≈ 5×): 115,740.74 msg/s
- **Concurrent connections** (~10% DAU): 5,000,000
- **Avg text payload**: 640 B (incl. metadata, headers)
- **Text storage/day** (no replicas): 1,192.09 GB
- **Text storage/day with RF=3**: 3.49 TB
- **Media share**: 15% @ ~400 KB avg → ~111.76 TB/day raw

> These are ballpark figures for capacity planning; real systems use per‑region numbers and margin (20–40%).

---

## High‑Level Architecture

**Edge LB** → **Gateway** (stateless) → **Session Service** (user⇄connection map) → **Chat Service** (ingest + routing) → **Streaming Log** (see Glossary: _Kafka_) → **Inbox/Outbox** (see Glossary: _Outbox Pattern_) → **Storage** (messages in **Wide‑column DB**, media in **Object Storage**) → **Notifier** (APNs/FCM) → **Search Index** → **Analytics/Monitoring**.

- Gateways are pooled behind Anycast/GeoDNS (see Glossary: _Anycast_) and speak **WebSocket over TLS** (see Glossary: _WebSocket_).
- Session Service tracks `userId → connectionId,gatewayId,deviceId` in **Redis Cluster** (see Glossary: _Redis_).
- Chat Service performs **validation**, assigns **per‑conversation sequence numbers**, writes to the **streaming log**, and triggers **fan‑out** (push) or **cursor‑based pull** for large groups.
- Media uploads go directly from client to **Object Storage** via **pre‑signed URLs**; messages carry only opaque handles.
- Everything is **multi‑region** and **active‑active** with per‑conversation **shard keys** (see Glossary: _Sharding_).

```
[Client] ⇄ [Edge LB] ⇄ [Gateway] ⇄ [Chat Service] ⇄ {Kafka/Pulsar}
                                    ↘︎ [Notifier]
                                     ↘︎ [Storage: Cassandra/Scylla] 
                                      ↘︎ [Search: Elasticsearch]
```

---

## Client Connectivity & Protocols

- **Primary**: **WebSocket (WSS)** for full‑duplex messaging (see Glossary: _WebSocket_).
- **Fallbacks**: **Long‑polling**/**SSE** for constrained networks.
- **Keep‑alives**: Heartbeats every 30–60s; **idle timeouts** and **backoff** on failures.
- **Compression**: Per‑message gzip for text; avoid for already‑compressed media.
- **Congestion signals**: Server issues **`flow_control`** events to slow senders.

**Why not plain HTTP?** Pull would require long‑polling; WSS avoids needless requests and reduces tail latency.

---

## Message Lifecycle

1. **Send** (`client → gateway`): Client assigns **clientMsgId** and timestamp.
2. **Ingest** (`gateway → chat`): Basic validation (size, ACL, device session).
3. **Persist**: Append to **stream** (Kafka) and **store** in DB (idempotent write).
4. **Sequence**: Per‑conversation **monotonic sequence** assigned (see Glossary: _Sequencer_).
5. **Fan‑out**: 
   - 1:1 → push to recipient device sessions if online; else **enqueue in inbox**.
   - Group → **small groups push**, **large groups pull** (cursor per member).
6. **Acks & Receipts**: Sender gets **`sent`**, then **`delivered`** when any target device acks, then **`read`** when recipient marks viewed.
7. **Sync**: Offline devices catch up via **cursor** or **since watermark**.
8. **Retention/TTL**: Ephemeral chats may set per‑message **TTL** (see Glossary: _TTL_).

---

## Receipts: Sent/Delivered/Read

- **Sent**: Server durably persisted (stream + DB). 
- **Delivered**: Any active device for the recipient confirms receipt.
- **Read**: Explicit client signal upon view; privacy settings may aggregate or delay.

Receipts are **events** on the same stream, correlated by `conversationId, messageId` (see Glossary: _Correlation ID_).

---

## Presence & Last Seen

- **Presence** states: `online`, `recently`, `offline`. Last‑seen timestamp kept in **Redis** with TTL refresh on user activity (typing, read, send).
- **Threshold** (e.g., 5s) below which we show **online** instead of exact time.
- **Privacy**: Only emit presence deltas to **contacts**/**groups**; sample/batch to avoid fan‑out storms.
- **Health**: Gateways emit **heartbeats**; missed heartbeats mark session stale.

---

## Group Messaging

- **Membership Service**: `groupId → members[]`, roles, and mute settings.
- **Fan‑out model**:
  - **Push (write‑time fan‑out)** for small groups (< 256): low read latency.
  - **Pull (read‑time fan‑out)** for large/broadcast: single group log; members **pull** via cursors (see Glossary: _Cursor_).
- **Ordering**: Per‑group **sequencer** partition.
- **Reliability**: At‑least‑once delivery; dedupe on `messageId` (see Glossary: _Idempotency_).

---

## Media Pipeline

- **Client‑side encrypt** media with a random **media key**; upload to **Object Storage** via **pre‑signed URL** (see Glossary: _Pre‑signed URL_).
- **Store** only: content hash, size, MIME, thumbnails, and encrypted handle in DB.
- **CDN** distribution; **range requests** for videos; **transcode** for previews.
- **Safety**: Optional AV scan, size caps, type allow‑list.
- **Retention tiers**: Hot (recent), Warm (30–90d), Cold/Glacier beyond.

Daily media order‑of‑magnitude: ~111.76 TB/day raw before CDN/cache and dedupe.

---

## Multi‑Device Sync

- Each device has a **device session** and **identity keys** (see Glossary: _Device Session_).
- Sender encrypts separately per recipient **device**; **linked devices** receive via the same fan‑out path.
- **Catch‑up** uses per‑device **cursors** + **since** APIs; conflict‑free because ordering is per‑conversation sequence.

---

## Storage Model, Sharding & Indexing

- **Messages DB**: Wide‑column (Cassandra/Scylla) or Dynamo‑style KV.
  - **Partition key**: `conversationId` (or `(conversationId, day)` to bound partitions).
  - **Clustering**: `sequenceNumber ASC`.
  - **Indexes**: Secondary index for **unread by user** (or maintain per‑user **inbox CF**).
- **Session map** in **Redis**: `userId → (gatewayId, connectionIds[])`, TTL 2–5 min with heartbeat refresh.
- **Search index** (Elasticsearch/OpenSearch) for full‑text across recent history.
- **Hot keys**: celebrity groups → split by **epoch** or **range partition** to avoid hotspots.
- **Schema evolution**: append‑only, versioned payloads.

---

## Ordering, Consistency, Idempotency

- **Per‑conversation ordering** via **sequencer** partitions keyed by `conversationId`.
- **Consistency**: Readers follow **read‑your‑writes** by reading from the log tail + DB.
- **Idempotency**: Client provides `clientMsgId`; server keeps a **dedupe store** with TTL. Retries are safe (see Glossary: _Dedupe_).

---

## Reliability, Retries & Backpressure

- **At‑least‑once** semantics on the stream; consumers commit offsets after durable write.
- **Outbox Pattern** at Chat Service to avoid dual‑write anomalies.
- **Backpressure**:
  - Per‑connection **send window**.
  - **Credit‑based flow control** events to clients.
  - **Rate limits** per user/group/API key (token bucket).
- **Queues** size caps with **dead‑letter** lanes for poison messages.

---

## Search & Message Discovery

- **Ingest** trusted plaintext only on the **client** for E2EE; server indexes metadata or, if allowed, user‑opt‑in plaintext in a secure service.
- **Queries**: prefix, fuzzy, mentions, file types, date ranges.
- **Retention**: shard by time; ILM to downsample/expire (see Glossary: _ILM_).

---

## Notifications

- **Mobile**: APNs/FCM with minimal content (conversation label only).
- **Collapse keys** to avoid floods; **high‑priority** for calls/mentions.
- **Desktop/Web**: WSS keeps you live; OS notifications optional.

---

## Security & End‑to‑End Encryption

- **E2EE** with modern **asymmetric identity keys**, per‑session **ephemeral keys**, and **forward secrecy** (see Glossary: _Forward Secrecy_).
- **Server** stores only ciphertext + routing metadata.
- **Safety**: replay protections (nonce), device revocation, safety‑number change UX.
- **Transport**: TLS 1.3 everywhere, cert pinning on mobile, HSTS on web.

---

## APIs & Events

### WebSocket Events (examples)
```json
// client → server: send message
{
  "type": "message.send",
  "conversationId": "u:alice|u:bob",
  "clientMsgId": "c3f7...",
  "payload": { "text": "hey" },
  "ts": 1733880000000
}

// server → client: ack + sequence
{
  "type": "message.sent",
  "conversationId": "u:alice|u:bob",
  "clientMsgId": "c3f7...",
  "messageId": "m:...",
  "sequence": 128934,
  "ts": 1733880000123
}

// server → client: delivered
{ "type": "message.delivered", "conversationId": "...", "messageId": "m:..." }

// client → server: read
{ "type": "message.read", "conversationId": "...", "messageId": "m:..." }
```

### REST (selected)
- `POST /media/presign` → pre‑signed upload URL (see Glossary: _Pre‑signed URL_).
- `GET /conversations/{id}/messages?since=cursor`
- `POST /typing` (rate‑limited, best‑effort).

---

## Data Models

### Messages (wide‑column example)
```
Partition key:  conversationId (or (conversationId, day))
Clustering:     sequenceNumber ASC

Columns:
- messageId (UUID)
- clientMsgId (string)           -- for idempotency
- senderUserId (string)
- payload (bytes)                -- ciphertext or minimal plaintext
- type (text, image, audio, video, doc)
- mediaHandle (string)           -- if media
- ts (millis)                    -- client/server timestamps
- ttl (seconds)                  -- optional
- statusByUser (map<userId, enum{sent,delivered,read}>)
```

### Session Map (Redis)
```
user:{userId} → {
  "gatewayId": "...",
  "connections": [ "conn-1", "conn-2" ],
  "deviceIds": [ "ios:...", "web:..." ],
  "lastSeen": 1733880000
}  EX 300
```

---

## Observability & SRE

- **Golden signals**: latency, traffic, errors, saturation (see Glossary: _Golden Signals_).
- **Key SLIs**: 
  - send→sent ack latency (p50/p95/p99)
  - sent→delivered, delivered→read
  - connect success rate
  - dropped notifications
- **Tracing**: Propagate **traceId**/**spanId** over WSS (see Glossary: _Distributed Tracing_).
- **Chaos**: region failover drills; auto‑remediation runbooks.

Target: **99.99% SLO** with error budget policies.

---

## Scalability & DR

- **Sharding**: `conversationId` → sequencer partition → Kafka topic/partition → DB shard.
- **Multi‑region**: Active‑active; **home shard** per conversation; cross‑region replication async (seconds).
- **DR**: Cross‑region snapshots (DB), versioned object storage (media), infra as code.
- **Capacity**: Gateways sized for ~5,000,000 concurrent sockets; autoscale on CPU and open‑file descriptors.

---

## Failure Scenarios & Resilience

- **Gateway crash** → clients reconnect with **resumption tokens**.
- **Sequencer partition down** → automatic leader failover; monotonicity preserved per partition.
- **DB hot partition** → split by time bucket; apply cache + write coalescing.
- **Notifier outage** → queue notifications; retry with exponential backoff and jitter.
- **Duplicate sends** (user retries) → dedupe by `clientMsgId`.
- **Clock skew** → sequence numbers dominate ordering; timestamps used for UI only.

---

## Trade‑offs & Alternatives

- **Protocol**: WebSocket vs **XMPP** vs **MQTT**.
  - WSS: ubiquitous, simple; XMPP: mature IM semantics; MQTT: IoT‑friendly.
- **DB**: Cassandra/Scylla (wide‑column) vs DynamoDB vs Postgres (partitioned).
- **Stream**: Kafka vs Pulsar; Kafka simpler ops, Pulsar built‑in multi‑tenant and tiered storage.
- **Fan‑out**: push for latency vs pull for scalability.
- **Search**: server‑side vs client‑side (with E2EE constraints).

---

## Glossary

- **Anycast** – Routing technique where the same IP is announced from multiple locations so clients hit the nearest POP.
- **APNs/FCM** – Apple/Google push notification services for iOS/Android.
- **CDN** – Content Delivery Network that caches media near users.
- **Correlation ID** – An ID used to tie together related events across services.
- **Cursor** – A bookmark for where a client is in a stream of messages.
- **Dedupe** – Dropping duplicate operations by remembering their IDs for a window.
- **Device Session** – A device’s authenticated, stateful session used for routing and keys.
- **Distributed Tracing** – End‑to‑end request tracing across services (traceId/spanId).
- **Forward Secrecy** – Property of encryption where past sessions remain safe even if long‑term keys leak.
- **Golden Signals** – Latency, Traffic, Errors, Saturation; the core metrics for SRE.
- **Idempotency** – Same request can be safely retried without changing the result.
- **ILM** – Index Lifecycle Management (rollover, shrink, delete) for search indices.
- **Kafka** – A distributed commit log used for durable, ordered streaming.
- **Outbox Pattern** – Persist events in the same transaction as state changes, then publish.
- **Pre‑signed URL** – Short‑lived URL allowing direct client upload/download to object storage.
- **Presence** – Whether a user appears online and their last‑seen time.
- **Redis** – In‑memory data store used for caching and fast maps/sets.
- **Sequencer** – Component that assigns a monotonic per‑conversation sequence number.
- **Sharding** – Splitting data across nodes by a key to scale horizontally.
- **SLO** – Service Level Objective, the reliability target users experience.
- **TTL** – Time to Live; automatic expiration for stored records.
- **WebSocket** – Full‑duplex, persistent TCP channel over TLS.
