g = (x for x in range(5))  # generator
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# 超出会抛出异常   StopIteration
# print(next(g))

# for i in g:
#     print(i)

'''
生成自定义长度的列表
当函数遇到yield关键字时，函数会暂停，并将对象返回出去，下次会继续上次暂停的地方执行
当函数遇到return关键字，函数会直接返回该对象 
'''

# def yield_test(number):
#     # li = []
#     n = 0
#     while n < number:
#         # li.append(n)
#         yield n  #return
#         n += 1
#     # print(li)
#
# res = yield_test(20)
# # print(res)
# # for i in res:
# #     print(i)
# print(next(res))

'''
send() 获取下一个值
只是在获取下一个值得时候，给上一个yield得位置传递一个数据
1.send()不能是第一个，也不能是最后一个
'''
def test():
    a1 = yield "hello"  #a1 = 'world'
    print('---1---')
    yield  a1
res = test()
print(next(res))
print(res.send("world"))