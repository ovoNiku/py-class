import json
import subprocess
from urllib.parse import urlencode

log = print


def method_subprocess_curl(url, **params):
    param_str = urlencode(params)
    cmd = f"curl --request GET '{url}?{param_str}' "
    log('cmd: ', cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    rs = stdout.decode("UTF-8")
    return rs


def test_todo_add(message):
    rs = method_subprocess_curl('http://127.0.0.1:5000/todo/add', message=message)
    rs_json = json.loads(rs)
    assert rs_json['success'], "add 返回异常"


def test_todo_all_num():
    rs = method_subprocess_curl('http://127.0.0.1:5000/todo/all')
    data = json.loads(rs)
    return len(data['data'])


def test_todo_delete(todo_id):
    rs = method_subprocess_curl(f'http://127.0.0.1:5000/todo/delete/{todo_id}')
    data = json.loads(rs)
    return data


def test_reset_file():
    with open('database.json', 'w') as f:
        data_list = [
            {
                "id": 0,
                "message": "初始化的todo",
                "create_time": "2021-01-05 00:00:00",
                "update_time": "2021-01-05 00:00:00",
                "status": "未完成"
            },
        ]
        f.write(json.dumps(data_list, ensure_ascii=False, default=lambda o: o.__dict__, indent=4))


if __name__ == '__main__':
    test_reset_file()
    # 获取当前数据的长度
    num = test_todo_all_num()

    test_todo_add("测试message")

    num_after = test_todo_all_num()
    assert num + 1 == num_after, f"操作add后数据长度不匹配, {num}, {num_after}"

    test_todo_delete(1)
    num_delete_after = test_todo_all_num()
    assert num == num_delete_after, f'操作delete后数据长度不匹配, {num}, {num_delete_after}'

    # 重置数据, 保证每次测试可以重复运行
    test_reset_file()
