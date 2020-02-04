"""
匿名函数
匿名函数关键字  参数：表达式返回值
lambda x:x*x
"""

# f = lambda x: x * x
# print(f(5))

# print(reduce(lambda x,y:x*y,range(1,7)))

'''
匿名函数可以直接作为函数返回值
'''

# def fx(i,j):
#     return lambda:i*j

# print(fx(6,6))  #<function fx.<locals>.<lambda> at 0x000002150B96B0D0>  内存地址
# res = fx(6,6)     #lambda : i*j = fx(6,6),还未调用匿名函数，用res()来调用
# print(res)       #<function fx.<locals>.<lambda> at 0x000002150B96B0D0>  内存地址
# print(res())     #36

'''
匿名函数当作参数
'''

# def test(a, b, func):
#     res = func(a, b)
#     # res = a + b
#     return res
#
# res = test(11, 33, lambda x, y: x + y)
# print(res)


'''
高阶函数
1、函数名可以作为参数输入
2、函数名可以作为返回值
只要满足条件之一-->高阶函数
map()
filter()
reduce()
'''

'''
不改变原有的符号，但是以绝对值来排序
'''
# lis = [4,-2,3,-1]
# lis.sort(key=abs)
# print(lis)

infor = [{'name':'Qian','age':28},{'name':'amy','age':18},{'name':'jack','age':20}]
infor.sort(key= lambda x:x['age'])
print(infor)