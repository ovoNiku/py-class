def odd_even_loop():
    number = 10
    """
    输入一个数字, 例如 10
    打印从0到这个数字的 奇数 和 偶数
    输出格式如下:
    奇数 1, 3, 5, 7...
    偶数 0, 2, 4, 6, 8, 10...
    自行完成测试
    """
    list_odd = []
    list_even = []
    """
    先在下面写好 assert 测试方法, 如果不符合预期会报错, 写代码前先运行一下, 保证方法是被调用到的
    然后写一个循环, 打印出来0~10的数字
    使用 % 计算判断奇数和偶数
    """
    for i in range(number + 1):
        # print(i)
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)

    # 先使用 assert 这种比较简单的测试方法
    assert list_odd == [1, 3, 5, 7, 9], "奇数生成错误, {}".format(list_odd)
    assert list_even == [0, 2, 4, 6, 8, 10], "偶数生成错误, {}".format(list_even)
    """
    完成
    """


def str_reverse():
    s = 'dlrow,olleh'
    """
    将字符串翻转打印出来
    例如上述字符串应该输出: 
    hello,world
    """
    #
    """
    1、先写测试
    2、文档中查看到可以用数组访问的方式翻转
    """
    result = s[::-1]
    assert result == 'hello,world', "字符串翻转错误, {}".format(result)
    # 完成


def pick_up_number_str():
    s = "123,abc,a21kd,42,9aj"
    """
    将字符串 s 按照逗号分割
    打印出来里面是数字的 子串
    例如上述字符串应该输出:
    123, 42
    """
    result = []
    """
    惯例先写测试
    然后需要使用 split 方法切割字符串
    然后需要一个判断是否是数字的方法 isdigit
    """
    for sub_str in s.split(','):
        if sub_str.isdigit():
            result.append(sub_str)

    assert result == ['123', '42'], "提取数字字符串异常, {}".format(result)


def reverse_word():
    s = 'tom and jack'
    """
    将整个字符串的里面的单词顺序进行翻转
    思路: 先翻转字符串, 根据空格切成list, 每一个单词再做一次翻转, 重新拼成字符串
    输出: jack and tom
    """
    reverse_list = []
    """
    先写assert测试
    思路是: 
    先翻转一次, 先用split切割, 然后逐个翻转, 然后使用join合并拼接
    每一步做完可以都打印看下中间结果
    """
    s = s[::-1]
    split_list = s.split(' ')
    # print(split_list)
    for i in split_list:
        reverse_list.append(i[::-1])
    # print(reverse_list)
    result = ' '.join(reverse_list)

    assert result == 'jack and tom', "翻转单词失败, {}".format(result)
    # 注释掉多余的print, 完成


if __name__ == '__main__':
    # 添加运行的方法
    odd_even_loop()
    str_reverse()
    pick_up_number_str()
    reverse_word()
