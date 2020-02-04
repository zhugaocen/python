"""
for循环 iterable
__iter__()将对象转为了迭代器
迭代器才会调用__next__()方法读取数据
"""

from collections.abc import Iterable, Iterator

# isinstance()
# print(isinstance('abc', Iterable))
# print(isinstance([1, 2, 3, 4], Iterable))
# print(isinstance((1, 2, 3, 4, 5, 6), Iterable))

'''
__next__()只能顺延调用，不能往前
'''

# for i in range(5):
#     print(i)


'''
可迭代的对象不一定是迭代器
'''
li = [1, 2, 3]
# print(isinstance(li, Iterator))  # False  Iterable

# li_iter = li.__iter__()
# print(li)

li_res1 = iter(li)
# print(li_res1)
# print(li_res1.__next__())
# print(next(li_res1))
# print(li_res1[1])  #报错，因为迭代器不支持索引取值


