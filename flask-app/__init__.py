import os
import socket

from flask import Flask
from flask import render_template, abort, redirect, url_for

from .sql.sql import MysqlInstance


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def start():
        return redirect(url_for('home'))

    @app.route('/home')
    def home():
        return render_template('home_view.html', 
            home_info="Welcome to Message in a Flask!", 
            route="Home")

    @app.route('/sql')
    def sql():


        mysql = MysqlInstance(
                host=os.environ["MYSQL_IP"],
                port=os.environ["MYSQL_PORT"],
                user=os.environ["MYSQL_USER"],
                password=os.environ["MYSQL_PASSWORD"],
                database=os.environ["MYSQL_DATABASE"]
            )

        return render_template('sql_view.html', 
            sql_instance=mysql, 
            route="SQL")

    @app.route('/environment')
    def environment():
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        try:
            dev_mysql_ip = socket.gethostbyname("database") # change this to your local db dns
        except socket.gaierror as err:
            dev_mysql_ip = False

        try:
            oc_mysql_ip = socket.gethostbyname("mysql-v8-mia-dev") # change this to your cluster db dns
        except socket.gaierror as err:
            oc_mysql_ip = False



        if oc_mysql_ip:
            env_info = {
                "Hostname": hostname,
                "IPv4": ip_address,
                "cluster database found": oc_mysql_ip # for openshift runs
            }
        elif dev_mysql_ip:
            env_info = {
                "Hostname": hostname,
                "IPv4": ip_address,
                "docker database found": dev_mysql_ip # for local docker-compose runs
            }
        else:
            env_info = {
                "Hostname": hostname,
                "IPv4": ip_address,
                "no specified database found": None # for local docker-compose runs
            }

        return render_template('environment_view.html', 
            env_info=env_info, 
            route="Environment")

    @app.route('/variables')
    def variables():
        env_info = os.environ
        return render_template('variables_view.html',
            env_info=env_info,
            route="Variables")

    @app.route('/<random_url>')
    def random_url(random_url):
        return f"404: Page \" {random_url} \" does not exist."

    return app