from flask import Flask
from flask import Blueprint
from flask import request

app = Flask(__name__)
route = Blueprint('index', __name__)


@route.route("/get", methods=['GET'])
def get_page():
    ret = dict(
        success=True,
        message='this is a get page.',
    )
    return ret


@route.route("/post", methods=['POST'])
def post_page():
    ret = dict(
        success=True,
        message='this is a post page.',
    )
    return ret


@route.route("/another", methods=['GET', 'POST'])
def another_page():
    ret = dict(
        success=True,
        message='this page allow get / post request',
        your_method=request.method,
    )
    return ret


def register_route():
    app.register_blueprint(route)


if __name__ == '__main__':
    register_route()
    app.run(debug=True)
