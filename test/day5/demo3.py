'''
函数作用域
LEGB
1.先从自己所在层级找，如果没有就向外层找
2.只要在某个层内找到了，就停止寻找，即使外面有同名的
'''

# def test():
#     b = 6  #局部变量
#
# # print(b)
# test()

a = 100  # 全局变量

# def test1():
#     print(f'a = {a}')  # 当局部没有变量时，去全局中找该变量
#
#
# def test2():
#     a = 200
#     print(f'a={a}')  # 当局部存在改变量时，则优先局部的
#
#
# test1()
# test2()

'''
局部变量 -->全局变量
global 局部变量名
'''

# count = 10
# def test3():
#     global count
#     print(count)
#     count = 5
#
# test3()
# print(count)

'''
LEGB
local -->局部作用域
enclosing -->夹在函数中间的作用域
global--> 全局作用域
built-in-->内建作用域
'''

# a = int(2.14)  # built-in  int()
# b = 11  # global
#
#
# def outer():
#     d = 5  # enclosing
#
#     def inner():
#         f = 6  # local
