Message in a Flask!
================================================================

Message in a Flask is a docker image which show environment information and environment variables.

### Current features
- It can show you the local Hostname and local IP address of the container.

### Planned features
- Show SQL connection, hostname, port, identity and simple query
- Show SaaS and PaaS services available


## Docker CI/CD commands



### MIA

##### MIA with Terminal:
```
git clone https://github.com/oscillate123/message-in-a-flask.git
docker build --rm -t mia:latest ./message-in-a-flask
docker image prune -f
docker run --name mia -d --rm -it -p 5000:5000 thlab/mia:latest
```
or in a bash script:
```
cat >> build_and_run.sh
#!/bin/bash
docker kill mia #kill existing container if any
docker build --rm -t thlab/mia:latest /path/to/message-in-a-flask #
docker image prune -f
docker run --name mia -d --rm -it -p 5000:5000 thlab/mia:latest
```
then run `bash /path/to/build_and_run.sh` everytime you change the code for automatic removal of previous container, build and start of new container



### MySQL

##### Connect to sql server:
```
mysql -u mia -h '0.0.0.0' -P 3306 -p
-u = user
-h = host
-P = port
-p = enter password after command run
```

##### Start MySQL with docker:
```
docker run --name mysql -d --rm -it -p 3306:3306 mysql:latest
```

##### Start MySQL with docker-compose:
```
version: '3.3'

services:
  db:
    image: mysql:8.0
    restart: always
    environment:
      MYSQL_DATABASE: 'db'
      MYSQL_USER: 'mia'
      MYSQL_PASSWORD: 'Howdy1234'
      MYSQL_ROOT_PASSWORD: 'r00tp455w0rd'
    ports:
      - '3306:3306'
    expose:
      - '3306'
    volumes:
      - mysql-db:/var/lib/mysql

volumes:
  mysql-db:

networks: # if you have vpn active, adding this part will specify that the default docker network will be used
  default:
    driver: bridge
    ipam:
      config:
        - subnet: 172.16.57.0/24
```



### Flask variables and commands

- `export FLASK_APP=flask-app`
- `export FLASK_ENV=development`
- `export FLASK_DEBUG=1`
- `flask run --host=0.0.0.0`

--------------------------------------

#### Sources:


##### Python documentation 
- https://docs.python-guide.org/writing/structure/
- https://stackoverflow.com/questions/4906977/how-to-access-environment-variable-values
- Python mysql class - https://github.com/nestordeharo/mysql-python-class/blob/master/mysql_python.py
- Python Mysql connector - https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html


##### Flask documentation
- https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/
- https://flask.palletsprojects.com/en/1.1.x/quickstart/
- Flask example project - https://github.com/pallets/flask/blob/1.1.2/examples/tutorial/flaskr/templates/blog/index.html
- https://stackoverflow.com/questions/32677167/in-a-flask-app-how-to-print-each-item-of-a-list-in-the-new-paragraphs-inside-my


##### Docker documentation
- Mysql docker-compose https://medium.com/@chrischuck35/how-to-create-a-mysql-instance-with-docker-compose-1598f3cc1bee
- Docker network error - https://stackoverflow.com/questions/43720339/docker-error-could-not-find-an-available-non-overlapping-ipv4-address-pool-am
- Flask - https://runnable.com/docker/python/dockerize-your-flask-application
- Tags - https://docs.docker.com/engine/reference/commandline/tag/
- Docker linting (size optimization) - https://www.fromlatest.io/#/


##### MySQL related links
- https://stackoverflow.com/questions/8283248/show-mysql-host-via-sql-command