'''
只要能用循环遍历的对象都是可迭代(iterable)的对象
list()
str()
dict()

for i in iterable:
    pass

for i in  [1,2,3]:
    print(i)

1.可迭代的对象内部都有 _iter_()
2.会调用iterable数据类型当中的_iter_()，将它转为迭代器
3.迭代器可调用_next_()方法取值,直到抛出StopIteration异常，结束迭代
'''

# lis = [1,2,3]
# lis_iter = lis.__iter__()
# try:
#     while True:
#         print(lis_iter.__next__())
# except StopIteration:
#     pass

'''
range(start,stop,step) start默认为0，左闭右开
'''
# for i in range(1,11,2):
#     print(i)

'''
程序：当我输入11 --> 壹拾壹元整
壹壹 ch_num[1]
'''
ch_num = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
ch = ['园', '拾', '佰', '仟', '萬']
ipt = input("请输入多少钱：")
len_ipt = len(ipt)
for i in ipt:
    # print(i)
    len_ipt -= 1
    # nums = ch_num[int(i)]
    # print(nums)
    # res = ch[len_ipt]
    # print(res)
    # print("{}{}".format(ch_num[int(i)], ch[len_ipt]),end='')
    print(f"{ch_num[int(i)]}{ch[len_ipt]}",end='')
print("整")
