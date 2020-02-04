'''
1.
'''
# a = 'amy'
# b =['鲜橙多','Qian','FS','自由']
# if a in b :
#     print(a+'在逻辑大家庭')
# else:
#     print(a+'不在。。好难过')
'''
2.
'''
# print('ax'<'xa') #比较ASCII值，a的ASCII值小于x的ASCII值，所以结果为True

'''
3.输入666执行哪个语句？
'''
# temp = input("请输入：")
# if temp == "YES" or "yes":
#     print("if被执行了")
# else:
#     print("else被执行了")

'''
4 is 与==的区别？
Python中对象包含的三个基本要素，分别是：id(身份标识)、type(数据类型)和value(值)。
is和==都是对对象进行比较判断作用的，但对对象比较判断的内容并不相同。
==是python标准操作符中的比较操作符，用来比较判断两个对象的value(值)是否相等，
is也被叫做同一性运算符，这个运算符比较判断的是对象间的唯一身份标识，也就是id是否相同
'''

'''
5.用户输入a,b，当a与b都不为0时则输出a与b的商，否则输出a与b的乘积。
'''
# a = input("a=")
# b = input("b=")
# if int(a) !=0 and int(b) !=0:
#     print(int(a)/int(b))
# else:
#     print(int(a)*int(b))

'''
6.基于5做三目运算
'''
# a = input("a=")
# b = input("b=")
# print(int(a)/int(b) if int(a) !=0 and int(b) !=0 else int(a)*int(b))

'''
7.小整数对象池的取值范围？以及其作用
-5~256  Python为了优化速度，使用了小整数对象池， 避免为整数频繁申请和销毁内存空间
'''
'''
8.用代码演练整数缓冲区
在命令行中看不出效果，得到的结果会不同
'''

# a=10000
# print(id(a))
#
# del a
# b=10000
# print(id(b))

