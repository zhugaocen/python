"""
成员
类属性（静态属性） 保存在类中，是可以通过对象访问,还可以通过类名访问
实例属性：保存在对象中，只能通过对象访问
"""

class Province(object):
    country = '中国'  # 类属性

    def __init__(self, name):
        # self.country = '中国'
        self.name = name

    def print_info(self):
        # print(self.country, self.name)
        print(Province.country, self.name)

guangdong = Province('广东')
sichuan = Province('四川')
guangdong.print_info()
sichuan.print_info()
