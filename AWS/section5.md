![Image](https://edrawcloudpublicus.s3.amazonaws.com/work/1067864/2022-1-24/1642996262/main.png)

![Image](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2017/03/28/QueueTypes-1.jpg)

![Image](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/sqs-visibility-timeout-diagram.png)

Here’s a clean, exam-and-interview-friendly set of **basic notes on Amazon SQS**—the queue that quietly keeps distributed systems from screaming at each other.

---

## 1. Basics (Producer & Consumer)

**Amazon Simple Queue Service (SQS)** is a fully managed **message queue** used to decouple components in a distributed system.

**Producer**

* Any service that **sends messages** to a queue
* Example: API server, Lambda, ECS task
* Uses `SendMessage` / `SendMessageBatch`

**Consumer**

* Any service that **polls and processes messages**
* Uses `ReceiveMessage`
* After processing, must call `DeleteMessage`

**Queue types**

* **Standard Queue**

  * At-least-once delivery
  * Best-effort ordering
  * Very high throughput
* **FIFO Queue**

  * Exactly-once processing
  * Strict ordering
  * Lower throughput
  * Requires `MessageGroupId`

**Key concepts**

* **Visibility Timeout**: time during which a message is invisible after being read
* **Long polling**: wait up to 20s to reduce empty receives
* **DLQ (Dead Letter Queue)**: failed messages after `maxReceiveCount`

Mental model:

> SQS is not a pipeline. It’s a **buffer with amnesia**—once deleted, the past is gone.

---

## 2. Encryption

SQS supports **encryption at rest** using **AWS Key Management Service (KMS)**.

**Options**

* **SSE-SQS** (AWS-managed key) – simplest
* **SSE-KMS** (customer-managed CMK) – more control & auditability

**What’s encrypted**

* Message body
* Message attributes
* Queue metadata

**What’s NOT encrypted**

* Data in transit → handled by HTTPS automatically

**Important note**

* Consumer/producer **don’t encrypt manually**
* IAM role must have `kms:Decrypt` / `kms:GenerateDataKey`

---

## 3. IAM (Who Can Do What)

IAM controls **who can interact with the queue**.

Typical permissions:

* Producer → `sqs:SendMessage`
* Consumer → `sqs:ReceiveMessage`, `sqs:DeleteMessage`
* Admin → `sqs:*`

**Best practice**

* Use **IAM roles**, not access keys
* Attach permissions to:

  * **AWS Lambda**
  * **Amazon ECS**
  * EC2 instance profiles

Least privilege always wins. Over-permissioned queues age badly.

---

## 4. Access Policies (Resource-Based)

SQS also supports **queue policies** (resource-based), similar to S3 bucket policies.

**Used when**

* Cross-account access
* Allowing AWS services (SNS, EventBridge) to send messages

**Example policy (SNS → SQS)**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {"Service": "sns.amazonaws.com"},
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:ap-south-1:123456789012:my-queue",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:sns:ap-south-1:123456789012:my-topic"
        }
      }
    }
  ]
}
```

Think of it as:

> IAM = **who you are**
> Queue policy = **who I allow**

---

## 5. Common Use Cases

* **Async processing**

  * API → SQS → worker
* **Traffic buffering**

  * Handle spikes without scaling everything
* **Microservices decoupling**

  * Services communicate indirectly
* **Retry & failure handling**

  * DLQ + reprocessing
* **Fan-out (with SNS)**

  * SNS → multiple SQS queues
* **Order processing, email sending, video jobs**

  * Anything slow or failure-prone

Rule of thumb:

> If something doesn’t need to happen **right now**, SQS is a candidate.

---

## 6. Code Snippets

### Send Message (Node.js – AWS SDK v3)

```js
import { SQSClient, SendMessageCommand } from "@aws-sdk/client-sqs";

const client = new SQSClient({ region: "ap-south-1" });

await client.send(
  new SendMessageCommand({
    QueueUrl: process.env.QUEUE_URL,
    MessageBody: JSON.stringify({ orderId: 123 }),
  })
);
```

---

### Receive & Delete Message

```js
import {
  ReceiveMessageCommand,
  DeleteMessageCommand
} from "@aws-sdk/client-sqs";

const messages = await client.send(
  new ReceiveMessageCommand({
    QueueUrl: process.env.QUEUE_URL,
    MaxNumberOfMessages: 1,
    WaitTimeSeconds: 20
  })
);

if (messages.Messages) {
  for (const msg of messages.Messages) {
    // process message
    await client.send(
      new DeleteMessageCommand({
        QueueUrl: process.env.QUEUE_URL,
        ReceiptHandle: msg.ReceiptHandle
      })
    );
  }
}
```

---

### FIFO Send Example

```js
await client.send(
  new SendMessageCommand({
    QueueUrl: FIFO_QUEUE_URL,
    MessageBody: "payment",
    MessageGroupId: "order-123",
    MessageDeduplicationId: "msg-001"
  })
);
```

---

## One-Line Summary

SQS is a **durable, boring, extremely reliable middleman**.
It doesn’t compute, it doesn’t think—but it **prevents chaos**.

If you want, the next natural extensions are:

* **SQS vs SNS vs EventBridge**
* **Visibility timeout tuning**
* **Lambda + SQS batch processing**
* **Exactly-once myths vs reality**

The queue is calm. The system survives.
