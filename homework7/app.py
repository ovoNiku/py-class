import json

from flask import (Blueprint, request)
from flask import Flask

from model import TodoModel

app = Flask(__name__)

route = Blueprint('todo', __name__)


@route.route("/all")
def todo_all():
    data_list = TodoModel.all()
    ret = dict(
        data=data_list,
    )
    return json.dumps(ret, default=lambda o: o.__dict__)


@route.route("/add")
def todo_add():
    # get url encode params
    message = request.args.get('message')
    todo = dict(
        message=message,
    )
    TodoModel.add(todo)
    return dict(
        success=True,
    )


@route.route("/delete/<int:todo_id>")
def todo_delete(todo_id):
    # todo 自行实现删除功能
    # 一个删除的实现参考
    TodoModel.delete(todo_id)
    data_list = TodoModel.all()
    ret = dict(
        data=data_list,
    )
    return json.dumps(ret, default=lambda o: o.__dict__)


def register_route():
    app.register_blueprint(route, url_prefix='/todo')


if __name__ == '__main__':
    register_route()
    app.run(debug=True)
