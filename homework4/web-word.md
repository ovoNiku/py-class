## web名词解释

### 认识 url

url 可以简单理解成网址, 它是有几部分组成的

如果尝试搜索 http url 的话可以看到类似的文章介绍

https://blog.csdn.net/vikeyyyy/article/details/80596988

简单来说, 以 http://127.0.0.1:5000/todo/list 为例

http 是协议, 除了 http 以外还有 https ssh 等协议

127.0.0.1 是 host, 域名, 就是网站的名字, 可以是网址也可以是一个 ip

5000 是端口号

/todo/list 是路径, 也会叫 `路由`, 在程序角度看, 一个路由对应了一个处理程序

如果后面还有类似 ?k1=v1&k2=v2 之类的就是参数

### request(请求) & response(响应/返回)

请求, 如果在web的上下文讨论的话, 就是发送 http 的请求

以 homework4 为例, 启动 flask 显示的信息

```text
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 634-954-104
```

这里访问 http://127.0.0.1:5000/ 就是一次发送的 request

网页返回了如下信息 

```text
{
message: "hello,world.",
success: true,
}
```

这个就是 response, 返回的内容

### get && post

是访问网站的不同请求方式, 直接通过浏览器输入网址访问就是 get

一般在网页上填写信息然后点击提交的请求大多数是 post

除了 get 和 post 还有很多其他的请求类型, 可以用到了再关注, 90% 的情况是用不到的

