docker run --name mysql-container \
  -e MYSQL_ROOT_PASSWORD=root \
  -v /home/harshith/Documents/LEARNING_101/MYSQL:/sql-scripts \
  -p 3306:3306 \
  -d mysql:latest

docker exec -it mysql-container mysql -uroot -proot
