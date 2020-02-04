"""
方法
实例方法
1.保存在类中，一般由self对象去访问
2.应用场景：如果对象中需要保存一些值（属性），方法中需要访问到该属性，执行实例方法
"""

class Demo(object):
    def __init__(self):
        self.name = 'amy'

    # 实例方法
    def test(self):
        print(self.name)

    def test1(self):
        print(self.name)

d = Demo()
d.test1()


# def test1():
#     name = 'amy'
#     return name
#
# def test2(name):
#     name1 = name
#
# res = test1()
# test2(res)
