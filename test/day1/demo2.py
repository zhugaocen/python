# print(3*3)
# print(3**3)  #3*3^2

#print(10/3) #二进制的有穷性

# print(9/3) #float 3.0

# print(10//3) #取整
# print(10.0//3)

#print(-10//3) #向下取整

# print(10%3)  #1  10//3   3   10-9=1
# print(-10%3)  #2  -10//3  -4  -10-(-12)=2

# print(0.1+0.1+0.1-0.3) #科学及算法 转为二进制

# from decimal import Decimal
# import decimal
# decimal.Decimal()
#print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')) #保留十进制的数据格式

# print(2.0==2) #比较数值
# print('2'==2) #int 和str不能直接比较

# a=1
# b=2
# print(a!=b)
# print(a<>b) #python3中不支持

# print(2.5>2)   #true

# print('abc'<'xyz')  #字符串与字符串之间的比较，ASCII值，对应位相比
# print(3<'a')  #报错，不能比较

# print(3>2>1)   #3>2 and 2>1 只有两者都为true的时候才返回true
# print(3>2>2)  #3>2 and 2>2 返回false

# print((3>2)>1)  #返回false 先计算3>2，结果为true,true=1,所以true>1返回false

# a=60
# b=13
# print(a or b)

# a=[1,2,3]
# b=[1,2,3]
# print(a is b) #false 比较的是内存地址
# print(id(a))
# print(id(b))
# print(a==b)  #true 比较数值

# a=1
# b=2
# if a+b>3:
#     print(a+b)
# else:
#     print(b-a)
#
# print(a+b if a+b>3 else b-a) #三目运算符

# print(id(1))
# print(id(2))  #python 的整数长度为32，并且是连续分配内存空间的。相邻两个整数内存地址之间相差32

# print(id(-5))
# print(id(-4))
# print(id(-6))


'''
整数缓冲区域
'''

a=10000
print(id(a)) #2146431468656

del a
b=10000
print(id(b)) #2146431468656


