"""
内置函數
map()
int()
zip()
"""

"""
返回1~10的奇數列表
"""
# li = []
# for i in range(1, 10):
#     if i % 2 == 1:
#         li.append(i)
# print(li)

"""
filter 過濾
"""

# def is_odd(n):
#     return n % 2 == 1
#
#
# print(list(filter(is_odd, range(1, 10))))


"""
阶乘 -->累积 循环 递归
reduce() 函数会对参数序列中的元素进行累积
"""

from functools import reduce

def multi(x, y):
    return x * y

print(reduce(multi, range(1, 7)))

print(reduce(lambda x,y:x*y,range(1,7)))