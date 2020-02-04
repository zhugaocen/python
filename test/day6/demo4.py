'''
实现计算函数运行时间的功能
'''

import time
def calcu_time(func):
    start = time.time()
    func()
    end = time.time()
    print('spend:{}'.format(end-start))

def test1():
    print('-----test-----')
    time.sleep(2)

# test1()
calcu_time(test1)

