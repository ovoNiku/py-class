## 学习使用 pycharm

首先需要认识的一个点: pycharm只是工具, 运行python不是一定要用pycharm, 两者并没有什么关系

其次使用这个工具需要解决的一些问题: 

    1、如何新建工程
    2、如何安装依赖(例如flask/fastapi等库)

事实上只要做好一个模板工程, 以后都不需要重复做这个事情, 只需要把工程复制一下就可以用

### 生成项目

![图片](src/1.png '')

生成后先运行一下, 这里会有一个 venv 的概念

![图片](src/2.png '')

### 安装依赖的三方库

python 自带一个叫做 pip3 的管理工具包, 可以用来下载依赖

sqlite这种是 python 自带的, 所以不需要下载

比如你需要使用 flask 框架, 则 

```
pip3 install Flask --trusted-host pypi.douban.com -i https://pypi.douban.com/simple
```

就可以了

比如 flask 的文档中也会提到 [flask-python](https://dormousehole.readthedocs.io/en/latest/installation.html#id2 '')

然后运行这个程序 ![图片](src/3.png '')

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True)
```

如果你看教程的话, 他会让你用这样的方式启动, 实际上这并不是一个好的方式

你需要有额外的成本, 先设置一个变量

```bash
export FLASK_APP=hello
flask run
```

那么有一个新的问题, 每次下载的项目都需要自己把所有的依赖找出来下来么

所以需要一个地方记录所有的依赖, 在python中约定了使用 requirements.txt 来做这个事情

```bash
pip3 freeze > requirements.txt
```

记录所有的依赖信息, 如果下载的项目有 requirements.txt 

```bash
pip3 install -r requirements.txt  --trusted-host pypi.douban.com -i https://pypi.douban.com/simple 
```

```text
click==8.0.3
Flask==2.0.2
itsdangerous==2.0.1
Jinja2==3.0.3
MarkupSafe==2.0.1
Werkzeug==2.0.2
```

虽然安装了 flask, 同时也装了一些其他软件, 因为flask也是基础其他的一些库实现的
