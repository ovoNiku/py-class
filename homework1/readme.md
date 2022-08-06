作业1
查询网络资料，写一个sqlite_demo.py文件
实现下面三个函数

db_create => 用来创建数据，创建数据表，建表语句

```
create table todo(id integer, message text);
```

db_insert => 用来写入一些数据

db_query => 查询数据并打印	


========= 写代码的过程描述

    14:41
    创建好文件写好函数声明, 尝试搜索sqlite的api使用方法
    搜索关键字 sqlite python
    搜到了这篇文章
    https://www.cnblogs.com/desireyang/p/12102143.html

抄了一下代码完成了1、2、3步

尝试运行，发现有自带的数据库管理软件, 如图

![图片](src/1.png '')

然后替换成题目中给的sql语句

```
create table todo(id integer, message text);
```

重新运行，刷新后结构也更新了

在刚才的教程中，搜一下insert的语句怎么写

发现也是用cur来操作,后面提到了要提交用commit

报错 1

sqlite3.OperationalError: table todo already exists

    数据表重复创建，这里参考教程把sql语句改成
    create table if not exists todo(id integer, message text);
    看意思是，当表不存在的时候创建

报错2

SyntaxError: Non-ASCII character '\xe6' in file main.py on line 16, but no encoding declared;

    看起来像是编码有问题，先用非中文的字符串，重新运行后成功
    通过如下方式可以查看数据

![图片](src/2.png '')

第二个函数看起来也ok了，然后写个循环多加几个数据

第三个函数就是写一个select语句

照着之前的写，发现直接打印cur.execute()的结果是

<sqlite3.Cursor object at 0x10b7642d0>

看了下教程里面的例子是这么写的

```
cur.execute("select * from Test")
print(cur.fetchall())
```

试了下ok了

了解了基本的sqlite的语句和api的使用

15:00 完成, 耗时20分钟