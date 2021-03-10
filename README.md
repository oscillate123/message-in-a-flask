Message in a Flask!
================================================================

Message in a Flask is a docker image which show environment information and environment variables.

### Current features
- It can show you the local Hostname and local IP address of the container.

### Planned features
- Show SQL connection, hostname, port, identity and simple query
- Show SaaS and PaaS services available


### Docker CI/CD commands

Terminal:
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
then run `bash /path/to/build_and_run.sh` everytime you change the code


### Flask variables and commands

`export FLASK_APP=flask-app`
`export FLASK_ENV=development`
`export FLASK_DEBUG=1`
`flask run --host=0.0.0.0`

--------------------------------------

### Sources:


#### Flask documentation
- https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/
- https://flask.palletsprojects.com/en/1.1.x/quickstart/


#### Python documentation 
- https://docs.python-guide.org/writing/structure/


#### Flask example project
- https://github.com/pallets/flask/blob/1.1.2/examples/tutorial/flaskr/templates/blog/index.html


#### Flask usefull links
- https://stackoverflow.com/questions/32677167/in-a-flask-app-how-to-print-each-item-of-a-list-in-the-new-paragraphs-inside-my
- https://runnable.com/docker/python/dockerize-your-flask-application
- https://docs.docker.com/engine/reference/commandline/tag/


#### Docker related links
- https://docs.google.com/document/d/1EJa3VbtJSbRMWcpsm9xfZJMUBjHed2c8xS0sJQ919_g