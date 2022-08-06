from flask import Blueprint


route = Blueprint('index', __name__)


@route.route("/")
def index():
    ret = dict(
        success=True,
        message='hello,world.',
    )
    return ret
