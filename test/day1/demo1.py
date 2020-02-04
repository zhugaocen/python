age=input("请输入年龄：")
# if(int(age)>18):
#     print("你好啊，小靓仔")
# else:
#     print("你好呀，小朋友")
if age.isdigit():
    if int(age)>18:
        print("你好啊，小靓仔")
    else:
        print("你好呀，小朋友")
else:
    print("您输入的非数字")
    age = input("请重新输入年龄：")