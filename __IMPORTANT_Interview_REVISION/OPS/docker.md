# Docker Commands

- running a docker image

```sh
docker run nginx
```

- list containers 

```sh
docker ps
```

- list all running and exited use -a option

```sh
docker ps -a
```

- stop a container

```sh
docker stop <container-name>
```

> find out container-name using docker ps

- remove a container

```sh
docker rm <container-name>
```

- list images 

```sh
docker images
```

- remove a image

> to remove an image , all the dependant containers should be stopped and removed

```sh
docker rmi <image-name>
```

- download an image but not run it 

```sh
docker pull <image-name>
```

- to run a command inside a container

```sh
docker exec <container-name> cat /etc/hosts
```

- run a image and detach

```sh
docker run -d kodukloud/simple-webapp 
```

- to attach the container

```sh
docker attach <container-id> # first 5 chars are enough
```


- to connect to the integrated terminal use -it

```sh
docker exec -it <container_name_or_id> bash
```

Here’s a clean, power-packed rundown of all the important **Dockerfile keywords**, but explained in a way that clicks—what they are *really doing* inside the container universe.

These are the commands you actually need as a 3-year full-stack dev building production images.

---

## FROM

The base layer of your image.
Everything begins here.

Example:

```dockerfile
FROM node:18-alpine
```

This is the “genetic parent” of your container.

---

## WORKDIR

Sets the working directory for all following commands.

```dockerfile
WORKDIR /app
```

It’s like `cd` but baked into the image.

---

## COPY

Copy files from host → image.

```dockerfile
COPY package.json .
```

Predictable and boring—in the best way. Prefer this over `ADD`.

---

## ADD

COPY + extras (like fetching URLs, auto-extracting tar files).
Use ONLY when you need those extras.

```dockerfile
ADD https://example.com/app.tar.gz /app/
```

Otherwise it’s a mischievous cousin of COPY.

---

## RUN

Execute commands during build time (not container runtime).
Each RUN = new layer.

```dockerfile
RUN apk add --no-cache git
```

This is how you set up the filesystem inside the image.

---

## CMD

Default command when the container starts.
Overridden by args passed to `docker run`.

```dockerfile
CMD ["node", "server.js"]
```

This becomes PID 1.

---

## ENTRYPOINT

Locks the base command so arguments extend it, not replace it.

```dockerfile
ENTRYPOINT ["python3"]
```

With this:
`docker run image script.py` → actually runs `python3 script.py`.

CMD = default.
ENTRYPOINT = mandatory.

---

## EXPOSE

Documentation + hint for container → host ports.
Doesn’t actually publish ports.

```dockerfile
EXPOSE 3000
```

Publishing happens with `-p 3000:3000`.

---

## ENV

Set environment variables inside the image.

```dockerfile
ENV NODE_ENV=production
```

Careful: these stay in image history (never put secrets).

---

## ARG

Build-time variables (don’t exist at runtime).

```dockerfile
ARG APP_VERSION
RUN echo $APP_VERSION
```

Passed using:
`docker build --build-arg APP_VERSION=1.0 .`

Great for parameterizing builds.

---

## USER

Set which user will run the container.

```dockerfile
USER node
```

Running as root in production is the cosmic equivalent of juggling knives greased in butter.

---

## VOLUME

Mark a directory as a mount point.

```dockerfile
VOLUME /data
```

Sometimes useful; often replaced by docker-compose.

---

## LABEL

Attach metadata to the image.

```dockerfile
LABEL maintainer="harshith@example.com"
LABEL version="1.2"
```

Registries love this stuff.

---

## HEALTHCHECK

Defines how Docker checks if your container is alive.

```dockerfile
HEALTHCHECK CMD curl --fail http://localhost:3000 || exit 1
```

This affects container orchestration systems too.

---

## SHELL

Change the default shell for RUN instructions.

```dockerfile
SHELL ["/bin/bash", "-c"]
```

Useful for cross-platform images.

---

## ONBUILD

“Trigger hooks” that fire when this image is used as a base image.

```dockerfile
ONBUILD COPY . /app
```

Rare. Potentially surprising. Use sparingly.

---

## STOPSIGNAL

Define which signal PID 1 should receive on stop.

```dockerfile
STOPSIGNAL SIGTERM
```

Helpful for graceful shutdowns.

---

## ENTRYPOINT + CMD combo (the professional pattern)

ENTRYPOINT defines the program.
CMD defines the default args.

```dockerfile
ENTRYPOINT ["node"]
CMD ["server.js"]
```

You get flexibility AND predictable behavior.

---

### Summary Table (quick scan)

| Keyword     | Purpose                          |
| ----------- | -------------------------------- |
| FROM        | Base image                       |
| WORKDIR     | Set working directory            |
| COPY        | Copy files                       |
| ADD         | Copy + extra behaviors           |
| RUN         | Build commands                   |
| CMD         | Default command                  |
| ENTRYPOINT  | Command that can’t be overridden |
| EXPOSE      | Document ports                   |
| ENV         | Runtime env vars                 |
| ARG         | Build-time vars                  |
| USER        | Switch user                      |
| VOLUME      | Persistent dir                   |
| LABEL       | Metadata                         |
| HEALTHCHECK | Container health logic           |
| SHELL       | Custom shell                     |
| ONBUILD     | Instructions for child images    |
| STOPSIGNAL  | Stop behavior                    |

---

If you want, I can build a cheat sheet PDF or give you a fully optimized sample Dockerfile for Node, React, Java, or Rust—your pick.


# Docker setup — Node (Express) + MySQL + Redis

A compact, production-minded multi-image example that demonstrates all the important Dockerfile keywords and best practices. Files below form a small project you can drop into a repo and run.

---

## Project layout (what you'll see in this document)

```
/docker-node-mysql-redis/
├─ app/
│  ├─ Dockerfile
│  ├─ .dockerignore
│  ├─ package.json
│  ├─ server.js
│  └─ healthcheck.sh
├─ db/
│  └─ init.sql
├─ docker-compose.yml
└─ README.md
```

---

## `app/Dockerfile` (multi-stage, small final image)

```dockerfile
# --- build stage -----------------------------------------------------------
# ARG: build-time variable
ARG NODE_VERSION=18
FROM node:${NODE_VERSION}-alpine AS builder

LABEL maintainer="harshith@example.com"

# set workdir
WORKDIR /usr/src/app

# copy package metadata first to allow caching
COPY package.json package-lock.json* ./

# install dependencies (no dev in final stage)
RUN npm ci --production=false

# copy rest of source
COPY . .

# build step (if any) - for typical Node apps this might be a transpile
RUN npm run build || echo "no build step"

# --- final stage -----------------------------------------------------------
FROM node:${NODE_VERSION}-alpine

# create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

WORKDIR /usr/src/app

# copy only what we need from builder
COPY --from=builder /usr/src/app/package.json ./
COPY --from=builder /usr/src/app/node_modules ./node_modules
COPY --from=builder /usr/src/app/dist ./dist
COPY --from=builder /usr/src/app/server.js ./server.js
COPY --from=builder /usr/src/app/healthcheck.sh ./healthcheck.sh

# expose the port (documentation + hint)
EXPOSE 3000

# env variables (avoid secrets here)
ENV NODE_ENV=production
ARG APP_VERSION=1.0.0
LABEL version=${APP_VERSION}

# use a simple healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s CMD ["/bin/sh", "-c", "./healthcheck.sh"]

# ensure shell for scripts
SHELL ["/bin/sh", "-c"]

# stop signal for graceful shutdown
STOPSIGNAL SIGTERM

# entrypoint + default cmd pattern
ENTRYPOINT ["node"]
CMD ["server.js"]
```

Notes: multi-stage build keeps the final image tiny. We add a non-root user, use ARG/ENV/LABEL, HEALTHCHECK, EXPOSE, SHELL, STOPSIGNAL, ENTRYPOINT + CMD.

---

## `app/.dockerignore`

```
node_modules
npm-debug.log
Dockerfile
.dockerignore
.env
.git
dist
```

---

## `app/package.json` (minimal)

```json
{
  "name": "demo-express",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js",
    "build": "echo 'no build'"
  },
  "dependencies": {
    "express": "^4.18.2",
    "mysql2": "^3.2.0",
    "ioredis": "^5.3.2"
  }
}
```

---

## `app/server.js` (tiny example showing DB + Redis usage)

```javascript
const express = require('express');
const mysql = require('mysql2/promise');
const Redis = require('ioredis');

const app = express();
const port = process.env.PORT || 3000;

// connection pools use environment variables provided via compose
const mysqlConfig = {
  host: process.env.MYSQL_HOST || 'db',
  user: process.env.MYSQL_USER || 'app',
  password: process.env.MYSQL_PASSWORD || 'apppass',
  database: process.env.MYSQL_DATABASE || 'appdb',
};

let pool;
let redis;

async function init() {
  pool = mysql.createPool({
    ...mysqlConfig,
    waitForConnections: true,
    connectionLimit: 5,
  });

  redis = new Redis({ host: process.env.REDIS_HOST || 'redis' });

  // simple test
  try {
    const [rows] = await pool.query('SELECT 1 AS ok');
    console.log('MySQL ok:', rows[0]);
    await redis.set('hello', 'world');
    console.log('Redis ok:', await redis.get('hello'));
  } catch (e) {
    console.error('DB init error', e);
    throw e;
  }
}

app.get('/', async (req, res) => {
  const cached = await redis.get('visits');
  const visits = cached ? parseInt(cached, 10) + 1 : 1;
  await redis.set('visits', visits);

  const [rows] = await pool.query('SELECT NOW() AS ts');

  res.json({ ok: true, visits, ts: rows[0].ts });
});

app.listen(port, async () => {
  await init();
  console.log(`Server listening on ${port}`);
});
```

---

## `app/healthcheck.sh`

```sh
#!/bin/sh
# simple healthcheck: probe http endpoint
if [ "$(curl -sS -o /dev/null -w '%{http_code}' http://localhost:3000/)" -eq 200 ]; then
  exit 0
fi
exit 1
```

Make it executable before building: `chmod +x app/healthcheck.sh`.

---

## `db/init.sql` (initial schema + user)

```sql
CREATE DATABASE IF NOT EXISTS appdb;
USE appdb;

CREATE TABLE IF NOT EXISTS metrics (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  value INT DEFAULT 0
);

-- create app user (for dev/demo only)
CREATE USER IF NOT EXISTS 'app'@'%' IDENTIFIED BY 'apppass';
GRANT ALL PRIVILEGES ON appdb.* TO 'app'@'%';
FLUSH PRIVILEGES;
```

---

## `docker-compose.yml` (compose v3.8, services for app, db, redis)

```yaml
version: "3.8"

services:
  app:
    build:
      context: ./app
      args:
        NODE_VERSION: 18
        APP_VERSION: 1.0.0
    image: demo-express:1.0.0
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - MYSQL_HOST=db
      - MYSQL_USER=app
      - MYSQL_PASSWORD=apppass
      - MYSQL_DATABASE=appdb
      - REDIS_HOST=redis
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    restart: unless-stopped

  db:
    image: mysql:8.0
    command: --default-authentication-plugin=mysql_native_password
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
    volumes:
      - db-data:/var/lib/mysql
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    volumes:
      - redis-data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

volumes:
  db-data:
  redis-data:
```

Notes: `depends_on` with `condition` is supported in Compose v2, but not in v3 for Docker Swarm—here it's fine for local dev using Docker Compose CLI. Healthchecks ensure services are ready.

---

## `README.md` (quick start)

```md
# Demo: Node + MySQL + Redis (Docker)

# Build & run (compose)
docker compose up --build

# Build only the app image
docker build -t demo-express:1.0.0 ./app

# Run app image directly (example)
docker run -p 3000:3000 --env MYSQL_HOST=<db-host> demo-express:1.0.0

# Useful commands
# List containers: docker ps
# Exec into app: docker exec -it <container> sh
# View logs: docker compose logs -f app
```

---

## Mapping to the important Dockerfile keywords

This example uses and demonstrates:

* `FROM` (base images in both stages)
* `ARG` (build-time variables: NODE_VERSION, APP_VERSION)
* `LABEL` (metadata)
* `WORKDIR` (sets working directory)
* `COPY` / `COPY --from=builder` (copy files / multi-stage)
* `RUN` (install steps, add user)
* `USER` (non-root process)
* `EXPOSE` (port documentation)
* `ENV` (runtime env vars)
* `CMD` / `ENTRYPOINT` (entrypoint + default args)
* `HEALTHCHECK` (container health)
* `SHELL` (explicit shell)
* `STOPSIGNAL` (graceful shutdown)
* `.dockerignore` (keeps context small)

---

## Security & production notes

* Do not keep secrets in `ENV` or Dockerfiles. Use secret managers or environment injection at runtime.
* Pin versions for base images and dependencies.
* Scan images with Trivy or similar before pushing to registries.
* Consider using `distroless` or smaller runtime images if you need minimal attack surface.

---

## Next steps (ideas)

* Add a CI workflow that builds, scans, and pushes `demo-express:1.0.0` to a container registry.
* Replace compose with Kubernetes manifests or a Helm chart for production.
* Add graceful shutdown handling in `server.js` to properly close DB/Redis connections on SIGTERM.

---

Happy hacking — open the files above, and run `docker compose up --build`. If you want, I can convert this into a downloadable ZIP or generate a Kubernetes manifest derived from the docker-compose file.


Here’s a tight, practical cheat-sheet on **port mapping**, **volume mapping**, and **inspect**—the everyday commands you keep using when working with containers. No fluff, just real-world notes that stick.

---

## **Port Mapping (container ↔ host)**

### Publish a port

Expose a container’s internal port to your machine:

```bash
docker run -p 3000:3000 myapp
```

Meaning:
**HOST:CONTAINER**
Left = your laptop
Right = inside the container

Useful note:
The app **always binds inside the container** (e.g., port 3000), but you can expose it on any host port:

```bash
docker run -p 8080:3000 myapp   # access via localhost:8080
```

### Publish UDP

```bash
docker run -p 5000:5000/udp myserver
```

### Publish multiple ports

```bash
docker run -p 80:80 -p 443:443 nginx
```

### Check published ports

```bash
docker ps
```

It shows PORTS like:
`0.0.0.0:8080->3000/tcp`

---

## **Volume Mapping (host ↔ container filesystem)**

### Bind mount (host directory → container)

Perfect for development:

```bash
docker run -v $(pwd):/app myapp
```

Notes:

* Live changes on host reflect inside container
* Use for Node/React development
* Be careful NOT to mount over system paths

### Named volume (managed by Docker)

Better for databases:

```bash
docker volume create mydata

docker run -v mydata:/var/lib/mysql mysql
```

Docker stores it in its own internal location.

### Create volume implicitly

```bash
docker run -v dbdata:/var/lib/postgresql/data postgres
```

### Check volumes

```bash
docker volume ls
```

### Inspect a volume

```bash
docker volume inspect mydata
```

Shows mount point, driver, etc.

### Remove a volume

```bash
docker volume rm mydata
```

(Can’t remove while a container is using it.)

### Remove unused volumes

```bash
docker volume prune
```

Housekeeping spell.

---

## **docker inspect — the X-ray machine for containers & images**

### Inspect a container

```bash
docker inspect mycontainer
```

Gives JSON with:

* IP address
* Ports
* Mounted volumes
* Entrypoint/CMD
* Env variables
* Network details
* Image layers used

Useful bits:

#### Get container IP

```bash
docker inspect -f '{{ .NetworkSettings.IPAddress }}' mycontainer
```

#### Get env variables

```bash
docker inspect -f '{{json .Config.Env}}' mycontainer | jq
```

#### Get mounted volumes

```bash
docker inspect -f '{{json .Mounts}}' mycontainer | jq
```

#### Get working directory

```bash
docker inspect -f '{{ .Config.WorkingDir }}' mycontainer
```

---

## **Useful Related Commands (handy in day-to-day debugging)**

### See container logs

```bash
docker logs -f mycontainer
```

### Jump into container terminal

```bash
docker exec -it mycontainer sh
```

### Show running containers

```bash
docker ps
```

### Show all containers (including stopped)

```bash
docker ps -a
```

### Stop / start

```bash
docker stop mycontainer
docker start mycontainer
```

### Remove container

```bash
docker rm mycontainer
```

---

## **Quick Summary (mental cheat sheet)**

**Port mapping** → `-p HOST:CONTAINER`
**Volume mapping** → `-v HOST:CONTAINER` or `-v NAME:CONTAINER`
**Inspect** → Full JSON deep-dive of container internals
**Logs** → Container output (super useful with Node/Express)
**Exec** → Open a shell inside a running container

---

If you want, I can turn this into a neat one-page printable PDF cheat-sheet.
