# Dockerfile (local-dev friendly)
FROM postgres:17-alpine

# Build-time defaults; runtime env from compose will override if present
ENV POSTGRES_USER=collabadmin \
    POSTGRES_PASSWORD=collabadminsecretpassword \
    POSTGRES_DB=collabdb

# No COPY of docker-init: we'll bind-mount ./docker-init at runtime (easier for dev)
# If you need custom postgres.conf, add it here (or mount it via volumes).
HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=5 \
  CMD pg_isready -U "$POSTGRES_USER" || exit 1
