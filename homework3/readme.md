## flask route

### 如何启动这个程序

首先启动 app.py

如果看到 如下信息则说明启动成功

```text
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```

### 这个程序有什么功能

这个程序是为了模拟一个 todo 记事本的功能, 有三个功能

1、展示所有的记录 (已完成)

2、添加记录 (需要添加程序实现)

3、删除某个记录 (需要添加程序实现)

### 如何使用这个程序

直接访问 http://127.0.0.1:5000/todo/list

会在浏览器中看到如下信息

```json
{
  "data_list": [
    "默认待办事项1",
    "默认待办事项2",
    "默认待办事项3"
  ]
}
```

对应的程序函数是 route/todo.py 里面的 data_list 方法

```python
data = dict(data_list=[])
route = Blueprint('todo', __name__)
@route.route("/list")
def data_list():
    return data
```

这几行的代码的意思 通过 /todo/list 可以访问到这个方法 (为什么不用管, 先当成标准的套路)

`return data` 的意思是, 直接把这个数据作为 response 返回 (也就是访问这个地址你看到的东西) 

### 需要做什么

尝试修改 add 方法, 即在方法 add 中实现修改 data

本质就是对 list 进行操作

通过访问 http://127.0.0.1:5000/todo/add?message=hello,world

可以访问到 add 方法

通过

```json
message = request.args.get('message')
```

这个方法可以获取 message 的内容

### 其他

尝试实现 delete 方法