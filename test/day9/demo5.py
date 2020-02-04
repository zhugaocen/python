"""
静态方法
@staticmethod
保存在类中，不需要创建对象，直接访问，不需要用到self

"""
import time
class TimeTest(object):
    @staticmethod
    def show_time():
        print(time.strftime('%Y年%m月%d日 %H:%M:%S',time.localtime()))

# nowtime = TimeTest()
TimeTest.show_time()
# nowtime.show_time()