# ipt = input("今天发工资了吗？Y/N：")
# if ipt.upper() == 'Y':
#     print("发工资了")
# elif ipt.upper() == 'N':
#     print("吃泡面")
# else:
#     print("输入错误")


ipt = input("今天发工资了吗？Y/N：")
if ipt.upper() == 'Y':
    salary = input("工资多少：")
    debt = input("要还多少花呗：")
    remain = float(salary) - float(debt)
    if remain >1000:
        print("可以吃大餐")
    else:
        print("还花呗,继续吃泡面")
elif ipt.upper() == 'N':
    print("吃泡面")
else:
    print("输入错误")