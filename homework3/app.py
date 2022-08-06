from flask import Flask
from route.index import route as index_routes
from route.todo import route as todo_routes

app = Flask(__name__)


def register_route():
    app.register_blueprint(index_routes)
    app.register_blueprint(todo_routes, url_prefix='/todo')


if __name__ == '__main__':
    register_route()
    app.run(debug=True)
