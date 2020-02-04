# def test():
#     print(11111)
#
# te = test()
# print(id(te))
# print(id(test()))

'''
闭包
1.在一个外函数中定义一个内函数
2.内函数里运用了外函数的临时变量
3.外函数的返回值是内函数的引用
'''

def test(number):
    print('-----1-----')
    def test_in(number_in):  #内函数
        print(number_in)
        print('----2------')
        return  number + number_in  #内函数运用了外函数的临时变量
    print('-----3-----')
    return test_in   #外函数的返回值是内函数的引用

res = test(20)  #res = test_in
in_res = res(25)
print(in_res)
