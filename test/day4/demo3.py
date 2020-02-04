'''
九九乘法表
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
...
'''

flag = False
for i in range(1,10):
    if flag == True:
        break
    for j in range(1,i+1):
        # print(i,j)
        if j == 3:
            flag = True
        print("{}*{}={}".format(j,i,(i*j)),end=' ')
    print('')