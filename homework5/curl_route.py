import os
import subprocess


def method_curl():
    print("请求1================")
    cmd = " curl --request POST 'http://127.0.0.1:5000/another' "
    os.system(cmd)
    print("请求1结束================")

    """
          会发现程序会额外打印一些信息
          % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                         Dload  Upload   Total   Spent    Left  Speed
          100    99  100    99    0     0  24750      0 --:--:-- --:--:-- --:--:-- 24750
    """


def method_subprocess_curl():
    cmd = " curl --request POST 'http://127.0.0.1:5000/another' "
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    rs = stdout.decode("UTF-8")
    print('subprocess_curl 请求执行结果\n {}'.format(rs))


if __name__ == '__main__':
    method_curl()
    # method_subprocess_curl()
