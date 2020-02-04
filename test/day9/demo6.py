"""
类方法
@classmethod
保存在类中，由类直接调用 cls--> 当前类
"""
import time
class TimeTest(object):
    @classmethod
    def clsmd(cls):
        print(cls)
        print('classmethod')

    @staticmethod
    def show_time():
        print(time.strftime('%Y年%m月%d日 %H:%M:%S',time.localtime()))

# nowtime = TimeTest()
TimeTest.show_time()
# nowtime.show_time()

TimeTest.clsmd()