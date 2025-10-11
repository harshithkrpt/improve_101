# Use the official lightweight Redis image
FROM redis:7-alpine

# Optional: Copy custom redis.conf if you have one
# COPY redis.conf /usr/local/etc/redis/redis.conf

# Expose the default Redis port
EXPOSE 6379

# Start Redis with default configuration
# (If you have a custom config, use: CMD ["redis-server", "/usr/local/etc/redis/redis.conf"])
CMD ["redis-server"]
