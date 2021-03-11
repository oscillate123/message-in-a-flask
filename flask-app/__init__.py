import os
import socket

from flask import Flask
from flask import render_template

from sql.sql import MysqlInstance


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def home():
        return render_template('home_view.html', 
            home_info="Welcome to Message in a Flask!", 
            route="Home")

    @app.route('/sql')
    def sql():
        return render_template('sql_view.html', 
            sql_info="In development", 
            route="SQL")

    @app.route('/environment')
    def environment():
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        env_info = {
            "Hostname": hostname,
            "IPv4": ip_address
        }

        return render_template('environment_view.html', 
            env_info=env_info, 
            route="Environment")

    @app.route('/<random_url>')
    def random_url(random_url):
        return f"404: Page \" {random_url} \" does not exist."

    return app