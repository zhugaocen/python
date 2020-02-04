"""
[0.5,1.0,1.5,2.0,2.5....10.0]
"""

# li = []
# for i in range(1,21):
#     li.append(i/2)
# print(li)

'''
列表推导式
'''
# li1 =[i/2 for i in range(1,21)]
# print(li1)

'''
随机生成一个列表 <0的数进行平方  生成新的列表
'''
import random
# print(random.randint(-10,10))
# li = [random.randint(-10,10) for i in range(10)]
# print(li)

# li = [-7,2,-2,-3, -5,10,5,-1,10,-8]
# li1 = []
# for i in li:
#     if i < 0:
#         i = i**2
#         li1.append(i)
#
# print(li1)

# print(list(filter(lambda x:x<0,li)))
# print(list(map(lambda x:x**2,filter(lambda x:x<0,li))))

# li2 = [i**2 for i in li if i<0]
# print(li2)

'''
列表推导式嵌套循环
'''
# for i in "123":
#     for j in "abc":
#         print(i+j)
#
# li3 = [i+j for i in "123" for j in "abc"]
# print(li3)

# dic ={'name':'amy','age':'18'}
#[key:value,key:value]
# li4 = [k+':'+str(v) for k,v in dic.items()]
# print(li4)

# li5 = ['age','name','gender']
#{'age':0,'name':1,'gender':2}
'''
字典推导式
'''
# dic1 = {i:li5.index(i) for i in li5}
# print(dic1)

'''
随机生成1~100之间的元素 并且去重
'''
# import random
# s1 = {random.randint(1,100) for i in range(1,100)}
# print(type(s1))

'''
没有元组推导式的说法
'''
# tup = (i for i in range(3))
# print(type(tup))     #不是元组推导式，而是generator生成器
# print(tuple(tup))

'''
函数调用时才执行
'''
res = [lambda x:x+i for i in range(10)]   #10+9
print(res[1](10))  #不论res[]取几，结果都为19
print(res)