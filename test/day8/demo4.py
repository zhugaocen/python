"""
魔法方法命名：__魔法__()  --> 有特殊功能的方法
构造方法__init__():创建对象时，同时通过对象执行这个方法
注意：
1.构造方法 底层封装返回None
2.构造方法当中声明的属性是允许外部调用的
"""

# class Student(object):
#     def __init__(self):
#         print('---1---')
#
#     def test(self):
#         pass
#
# qian = Student()

class Students(object):
    def __init__(self):
        self.age = "18"
        self.gender = 'male'
        self.addr = 'chengdu'
    def stu_info(self, name):
        print(name, self.age, self.gender, self.addr)
    def test(self):
        self.weight = '120'


s = Students()
print(s)   #输出对象的内存地址
# print(s.age)
# # print(s.weight)   #报错  调用方法后才能使用该属性
# s.test()
# print(s.weight)
# s.stu_info('F.S')
# s.stu_info('amy')
# s.stu_info('jack')
