from flask import (Blueprint, request)

route = Blueprint('todo', __name__)

data_list = [
                "默认待办事项1",
                "默认待办事项2",
                "默认待办事项3",
            ]


@route.route("/list")
def data_all():
    return dict(
        data=data_list
    )


@route.route("/add")
def add():
    # get url encode params
    message = request.args.get('message')
    data_list.append(message)

    return dict(
        data=data_list
    )


@route.route("/delete/<int:todo_id>")
def delete(todo_id):
    # todo 实现删除功能

    return dict(
        data=data_list
    )
