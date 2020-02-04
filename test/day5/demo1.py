"""
函数 ：封装一个特定功能的代码块
避免重复造轮子，提高代码的复用性
函数如果不进行调用，只会载入内存
只有当函数调用时，才会执行函数体内的代码
"""


# def multi_table():
#     print("九九乘法表")
#
# multi_table()

"""
函数参数
"""

# def test(b):   #形参
#     print(b)
#
# a = 1
# test(a)  #实参

# def test(a):#形参
#     a = 100  #不可变对象参数，相当于重新赋值
#     print('111',a)
#
# a = 1
# test(a)  #实参
# print('222',a)

# def test1(li):
#     li.extend([1,11])  #可变的对象参数传入，改变原有的值
#     print('1',li)
#     # pass
#
# li = [1,2,3]
# test1(li)
# print('2',li)

'''
利用函数完成两个数值相加
'''
# def sum_nums(num1,num2):
#     result = num1 + num2
#     print("{}+{}={}".format(num1,num2,result))
#     pass
# num1 = int(input("请输入num1:"))
# num2 = int(input("请输入num2:"))
# sum_nums(num1,num2)   #位置参数 一一对应的
# sum_nums(num1=num1,num2=num2)     #关键字参数，不受位置影响，只与形参对应有关

# def test2(a, b=3):   #默认参数值,不传为默认值，传了则覆盖
#     a = a + b
#     print(a,b)

# a = 1
# test2(a)  #4  3
# test2(a,10)  # 11  10

# range(1,10).index()

# import requests
# requests.get()

'''
*args-->可传可不传，但要传 -->元组
**kwargs -->可传可不传，但要传 -->dict字典
'''
# def test4(*args):  #打包成元组
#      print(args)
#
# test4(1,2,3)

# def test5(**kwargs):   #打包成字典
#     print(kwargs)

# test5(a=1,b=2,c=3)   #{'a': 1, 'b': 2, 'c': 3}

def test6(a,b,c):    #解包
    print(a,b,c)

tu = (1,2,3)
test6(*tu)

a,b,c =(1,2,3)