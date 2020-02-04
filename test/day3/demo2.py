dic1={'name':'jack','age':'19'}
print(dic1)
# print(dic1.get('name'))
# print(dic1.items())
# for k,v in dic1.items():
#     print(k,v)

# print(dic1.keys())
# print(dic1.values())

dic2 = {'Qian':90,'sige':85,'FS':88}
print(sorted(dic2))  #以key的ASCII值来排序
print(sorted(dic2.values()))
# print(list(zip(dic2.values(),dic2.keys())))

print(sorted(zip(dic2.values(),dic2.keys())))