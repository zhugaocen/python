'''
封闭：已经实现的代码块，则尽量可能不做任何修改
开放：允许拓展新的功能
@  语法糖
@calcu_time 装饰器：在不改变源代码的情况下添加新的功能
'''

# import time
# '''
# 想要添加验证功能？一定要遵循封闭开发原则
# '''
# def calcu_time(func):
#     print('我在装饰')
#     def test_in():
#         start = time.time()
#         func()
#         end = time.time()
#         print('spend:{}'.format(end - start))
#     return test_in
#
# @calcu_time  #test1 = calcu_time(test2)  #test1 = test_in
# def test2():
#     print('-----test2-----')
#     time.sleep(2)
#
# @calcu_time
# def test3():
#     print('-----test3-----')
#     time.sleep(2)


# test1()
# test1 = calcu_time(test2)  #test1 = test_in
# test2()  #test_in()
# test3()


import time

'''
想要添加验证功能？一定要遵循封闭开发原则
'''
def outer(flag):
    def calcu_time(func):
        print('我在装饰')
        def test_in():
            start = time.time()
            func()
            end = time.time()
            print('spend:{}'.format(end - start))
            if flag == 'true':
                print("验证成功")
        return test_in
    return calcu_time

@outer(flag='true ')
def test2():
    print('-----test2-----')
    time.sleep(2)

test2()