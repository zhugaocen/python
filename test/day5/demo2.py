"""
函数的返回值
return 返回值
当有多个return时，执行不会报错，但只执行第一个
因为程序在遇到函数体内第一个return时，就返回出去了
今天距离20号还有13天
20号距离春节还有 5天
"""


# def holiday():
#     dis_holiday = 13
#     print("距离放假还有：{}".format(dis_holiday))
#     return dis_holiday
#
# def spring_fes(dis_holiday):
#     dis_spr_fes = dis_holiday + 5
#     print("距离春节还有：{}".format(dis_spr_fes))
#
# res = holiday()
# # print(res)
# spring_fes(res)

def test6():
    a, b, c = 1, 2, 3
    return a, b, c


a, b, c = test6()
print(a, b, c)
