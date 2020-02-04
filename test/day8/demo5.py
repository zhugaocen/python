"""
__str__()
1.return返回值一定要是字符串类型
2.有多个返回值时，注意使用字符串拼接
"""

class Students(object):
    def __init__(self, age, gender, addr):
        self.age = age
        self.gender = gender
        self.addr = addr

    def __str__(self):
        return str(self.age)
        # return f'{str(self.age)},{self.gender},{self.addr}'
        # return self.age

s = Students(18, 'female', 'kunming')
print(s)
# print(s.__str__())  #跟普通调用方法无区别，不会报错
