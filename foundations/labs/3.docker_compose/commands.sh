# Bring up docker-compose.yml
docker-compose up

# check containers running
#CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS         PORTS                                         NAMES
#a9886f7d3c1f   python:3.12   "sh -c 'pip install …"   5 minutes ago   Up 5 minutes   0.0.0.0:8000->5000/tcp, [::]:8000->5000/tcp   flask-app
#4ed4c4addbee   mysql:8.0     "docker-entrypoint.s…"   5 minutes ago   Up 5 minutes   0.0.0.0:3306->3306/tcp, [::]:3306->3306/tcp   mysql-db
docker-ps

# Open interative terminal inside terminal
# Similar to SSH into a box, now can run linux commands
docker exec -it flask-app bash
# Run 
python
print("hello inside docker container")
exit()
# Return to host terminal
exit

# access mysql container
docker exec -it mysql-db bash
# login to database
mysql -u user -p password   #password
show databases;
show tables;
use testdb;
show tables;
select * from messages;
exit
# Return to host terminal
exit

# Check flask-app logs
docker logs flask-app

# Follow logs of service in real time
# docker logs -f <service-name>
docker logs -f flask-app
docker logs -f mysql-db
