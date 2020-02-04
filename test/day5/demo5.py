"""
递归
5！ --> 5*4*3*2*1
4! --> 4*3*2*1
"""

# i = 1
# res = 1
# while i <= 4:
#     res =res * i
#     i += 1
# print(res)

"""
1.调用自身函数
2.还没有自带的结束条件（使用递归时，设置结束条件）
3.凡是递归可以做到的，循环也可以做
4.递归效率低于循环
"""


def get_nums(num):
    if num > 1:
        return num * get_nums(num - 1)  # 6*5*4*3*2*1
    else:
        return 1


res = get_nums(6)
print(res)
