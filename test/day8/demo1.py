"""
输出多个同学的信息
"""

def stu_info(nsme, age, gender, addr):
    print(nsme, age, gender, addr)

stu_info('F.S', '18', 'male', 'chenddu')
stu_info('amy', '18', 'male', 'chenddu')
stu_info('jack', '18', 'male', 'chenddu')

class Student(object):
    def stu_info(self, name, age, gender, addr):
        print(name, age, gender, addr)

s = Student()
s.stu_info('F.S', '18', 'male', 'chenddu')
s.stu_info('amy', '18', 'male', 'chenddu')
s.stu_info('jack', '18', 'male', 'chenddu')
