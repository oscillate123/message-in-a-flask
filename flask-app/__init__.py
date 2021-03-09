import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def root():
        return "Welcome to message in a flask!"

    @app.route('/hello')
    def hello():
        return 'Howdy!'

    @app.route('/sql-database')
    def sqldb():
        return 'Hello, sqldb!'

    @app.route('/container')
    def container():
        return 'Hello, Container!' 

    @app.route('/<random_url>')
    def random_url(random_url):
        return f"Page: \" {random_url} \" does not exist."

    return app