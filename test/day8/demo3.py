"""
self是什么？
self其实就是对象本身，也就是说，当实例化的对象是谁，self就是谁
self形参
"""

# class Students(object):
#     def test(self):
#         print(self)
#
# Jc = Students()
# print(Jc)
# Jc.test()

# li = [1,2,3]
# li.append()

'''
对象是否可以将自己的属性（name,age）带给类？

'''
class Student(object):
    def info(self):
        print(jack.name,jack.age)

jack = Student()
jack.name = 'jack'
jack.age = 18
jack.info()
