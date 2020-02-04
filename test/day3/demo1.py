# fs={"addr":"gd","age":"15"}
# print(fs)

# fs1={("addr"):"yn"}
# print(fs1)

# dic={}
# print(type(dic))
# dict()
# dic1 = {"name":"amy","age":"19","hobby":"sleep"}
# print(dic1)

# dic2=dict(name="amy",age=18)
# print(dic2)

# dic3 = dict([('name','amy'),('age',18)])
# print(dic3)

'''
[1,2,3,4]-->['1','2','3','4']
map()  #根据提供的函数对指定序列做映射
zip()  #将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，返回由这写元素组成的列表。
'''

# li = [1,2,3,4]
# li[:] = ['1','2','3','4']
# print(li)
# print(list(map(str,li)))

'''
lik与liv里面一一对应的元素-->('name','amy')
'''
lik = ['name','age']
liv = ['amy',18]
def fmap(a,b):
    return (a,b)

# print(dict(map(fmap,lik,liv)))

print(dict(zip(lik,liv)))