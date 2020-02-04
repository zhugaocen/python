"""
函数的调用
函数执行完毕后会返回到函数调用处
"""


# def test():
#     print(5)
#
#
# def test2():
#     print(3)
#     test()
#     print(4)
#
#
# def test3():
#     print(1)
#     test2()
#     print(2)
#
#
# test3()

def mutil_table():
    print("九九乘法表")

def print_tables():
    i = 0
    while i <10:
        mutil_table()
        i += 1
    # for i in range(10):
    #     mutil_table()

print_tables()
