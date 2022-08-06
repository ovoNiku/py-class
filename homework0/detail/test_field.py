class Test:

    static_field = 'static'

    def __init__(self):
        # 这个叫做类的构造方法
        self.instance_field = 'instance'

    def get_instance_field(self):
        # 这个叫做类的实例方法
        return self.instance_field

    # 这个带@的叫做注解
    @classmethod
    def get_static_filed(cls):
        # 这个叫做类方法
        return cls.static_field


if __name__ == '__main__':
    # 这个过程叫做实例化
    t = Test()

    # 类方法可以直接通过类名调用
    s = Test.get_static_filed()
    print(s)
    # 实例方法必须通过实例化之后的变量调用
    f = t.get_instance_field()
    print(f)