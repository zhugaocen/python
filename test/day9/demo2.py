"""
__init__() 在类的外部去访问的
不想被外部访问，怎么办？
私有属性 --> __属性名 -->不允许在类的外部去访问
"""

# class People(object):
#     def __init__(self):
#         self.name = 'oldamy'
#         self.__has_bf = 'no'
#
# amy = People()
# print(amy.name)
# print(amy.has_bf)   #报错
# print(amy.__has_bf)   #报错

'''
强硬的渴望访问到该私有属性
类的外部不能直接访问？类中的方法是否可以访问？
1.可以通过类的内部方法返回私有属性，在外部调用访问到
'''

# class People(object):
#     def __init__(self):
#         self.name = 'oldamy'
#         self.__has_bf = 'no'
#
#     def get_has_bf(self):
#         return self.__has_bf
#
#     def set_has_bf(self,yes_or_no):
#         self.__has_bf =yes_or_no
#
# amy = People()
# print(amy.name)
# # res = amy.get_has_bf()
# # print(res)
#
# # print(amy.__dir__())    #列出对象拥有的属性名与方法名 []
# # amy.__has_bf = 'emm...'
# # print(amy.__has_bf)
# # print(amy.get_has_bf())
# # print(amy.__dir__())
#
# amy.set_has_bf('yes')
# print(amy.get_has_bf())

'''
私有方法：__方法名 -->对象不希望公开的方法
'''
class Demo(object):
    def test1(self):
        print('---1---')

    def test2(self):
        print('---2---')

    def __test3(self):
        print('---3---')

    def _test4(self):
        print('---4---')

d = Demo()
d.test1()
d.test2()
# d.__test3()  #报错
d._test4()
d._Demo__test3()
