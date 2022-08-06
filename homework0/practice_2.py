def bubble_sort():
    array = [2, 1, 9, 7, 6, 4, 3, 5]
    """
    将数组进行排序, 使用冒泡排序即可
    冒泡排序的方式: 两次循环, 将数字两两比较进行排序    
    """


def args_from_url():
    url = 'https://baidu.com?search=test'
    """
    处理字符串, 可以获取参数的dict
    例如这里的case需要输出
    dict(search=test)
    """


def meta_from_url():
    url = 'http://www.google.com:8000/doc?doc_id=1'
    """
    处理字符串, 可以得到字符串的 
        协议 (http/https)
        host (www.google.com)
        端口号 (8000, 如果没有, http默认是80, https是443)
        访问路径 (doc)
        参数dict (doc_id=1)
    请注意检查url的合法性
    """
