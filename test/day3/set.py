s = {1,2,3}
print(type(s))

s1 = {1,2,2,2,3,4,5}
print(s1)
s1.add((1,2,3))     #可以添加不可变的数据类型。
# s1.add(([1,2,3])) #报错，添加可变的数据类型，不可以进行哈西加密

s1.update("hello")
print(s1)
print(s1)
s1.remove(3)
print(s1)
print(id(s1))
s1.pop()
print(s1)
print(id(s1))

