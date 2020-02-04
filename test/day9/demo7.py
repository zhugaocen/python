"""
成员
属性
    实例属性
    静态属性(类属性)
            obj.name
方法
    实例方法
    静态方法
    类方法
            obj.test()

obj.test 去调用test()方法

@property 负责将一个方法变为属性
"""

# class Demo(object):
#     @property
#     def test(self):
#         print("test")
#         return 1
#
#     @test.setter  #d.test = 123
#     def test(self,para):
#         print(para)
#
#     @test.deleter   #del d.test
#     def test(self):
#         print("i am delete")
#
# d = Demo()
# # d.test()
# res = d.test  #当访问时，需要返回值
# print(res)
#
# d.test = '123'
#
# del d.test

'''
分页
用户输入：1
[0,1,2,3,3...9]
2
[10,11,12....19]
...
100页
'''
# li = [i for i in range(1000)]
# while True:
#     p = int(input("请输入页码："))  # 1 -->li[0:10]  #li[start :end]
#     start = (p - 1) * 10
#     end = p * 10
#     print(li[start:end])

'''
面向对象实现方式
'''
# li = [i for i in range(1000)]
#
# class Page(object):
#     def __init__(self,cur_page):
#         try:
#             p = int(cur_page)
#         except Exception as e:
#             p = 1
#         self.page = p
#
#     @property
#     def start(self):
#         val = (self.page - 1)*10
#         return  val
#
#     @property
#     def end(self):
#         val = self.page*10
#         return val
#
# while True:
#     p = int(input("请输入页码："))
#     page = Page(p)
#     # print(li[page.start():page.end()])
#     print(li[page.start:page.end])

'''
@property
'''

class Test():
    def __init__(self):
        self.__age = 18

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def del_age(self):
        del self.__age

    age = property(fget=get_age,fset=set_age,fdel=del_age)

t =Test
res = t.age
print(res )