#!/bin/bash

MODE=$1

if [[ "$MODE" == "dev" ]]; then
  echo "Starting in DEVELOPMENT mode (hot reload for frontend, 1 Eureka replicas)"
  docker compose -f docker-compose.dev.yml up --build --scale eureka=1
elif [[ "$MODE" == "prod" ]]; then
  echo "Starting in PRODUCTION mode (nginx static frontend)"
  docker compose -f docker-compose.yml up --build
else
  echo "Usage: $0 [dev|prod]"
  exit 1
fi
