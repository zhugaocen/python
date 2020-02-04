"""
#类的创建/定义
class 类名：
    def 方法名(self,参数):
        pass

#执行
s = 类名()  #s为对象（实例化）
s.方法名(参数)
"""

class Students(object):
    def stu_info(self, name):
        print(name, self.age, self.gender, self.addr)

s = Students()
s.age = "18"
s.gender = 'male'
s.addr = 'chengdu'
s.stu_info('F.S')
s.stu_info('amy')
s.stu_info('jack')
