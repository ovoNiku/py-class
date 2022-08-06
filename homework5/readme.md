## 使用 curl 实现 web 服务的测试  

### 

在 homework4 中, 通过启动 web 服务可以在浏览器中访问到对应的程序函数

通过访问不同的路径可以对列表进行 查询 / 新增 / 删除

但是这个过程比较手动, 这里介绍一个自动化访问网页的方法

并结合 curl 指令, 介绍不同参数的传递方式

### web 相关知识

之前提到的关于网页请求, 分为 `GET` 请求 和 `POST` 请求

通常我们通过网页直接访问的就是 GET 请求, 但是无法直接通过网站地址访问 POST 请求

启动本目录下的 app.py , 看一下里面的代码, 里面定义了 3个 方法, 尝试直接用浏览器访问他们

http://127.0.0.1:5000/get

访问这个地址可以正确返回

http://127.0.0.1:5000/post

访问这个地址会返回如下信息

```text
Method Not Allowed
The method is not allowed for the requested URL.
```

http://127.0.0.1:5000/another

访问这个地址会返回

```text
{
    message: "this page allow get / post request",
    success: true,
    your_method: "GET",
}
```

### 如何使用 post 方法访问

在控制台使用如下指令

```shell
curl --request POST 'http://127.0.0.1:5000/post'
```

这次能看到返回信息是 

```json
{
  "message": "this is a post page.",
  "success": true
}
```

尝试自己编写 shell 访问 http://127.0.0.1:5000/another 试一下

尝试用 post 方法访问 http://127.0.0.1:5000/get 查看结果

尝试通过 get 方法的命令访问 http://127.0.0.1:5000/get 查看结果

### 如何在 python 中使用控制台命令?

查看并运行 curl_route.py

里面提供了两个方法 method_curl 和 method_subprocess_curl 

分别运行对比一下差异, 并自行理解代码