# i = 1
# while i <= 5:
#     print("hello amy")
#     i += 1  # 计数器

'''
 求1~100之间的和
'''

# n = 1
# num_sum = 0
# while n <= 100 :
#     # num_sum = num_sum + n
#     num_sum += n
#     print(n)
#     n += 1
#     if n == 8:
#         break  #退出循环
#         # continue  #退出当前循环，进入下次循环
# else:
#     #else是指条件为false的时候执行的语句
#     print("执行完毕")
# print(num_sum)


'''
*
**
***
****
....
'''

# row = 1
# while row <= 4:
#     print("*" * row)
#     row += 1

row = 1
while row <= 4:
    starts=1
    while starts <= row:
        print("*",end='')
        starts += 1
    print('')
    row += 1