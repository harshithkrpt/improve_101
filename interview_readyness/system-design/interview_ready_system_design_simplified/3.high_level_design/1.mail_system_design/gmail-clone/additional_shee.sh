docker cp services/auth-service/migrations/01_create_users_table.sql $(docker-compose ps -q mysql):/tmp/

docker-compose exec mysql bash
mysql -u root -p password < /tmp/01_create_users_table.sql