# 什么是正则表达式：记录文本规则的代码
# 是一个特殊的字符序列
# 普通字符和元字符组成的，其实就是对元字符的学习

import re

# reg_String = 'hellopython@wanhellog.@！：xiaowang'
# reg = 'hello'
#
# result =re.findall(reg,reg_String)
# print(result)

'''
元字符
.匹配除换行符以外的任意字符
\w 匹配字母或数字或下划线或汉字
\s 匹配任意的空白符
\d 匹配数字
\b 匹配单词的开始或结束
^ 匹配字符串的开始
$ 匹配字符串的结束
'''

# reg_String = 'hellopython1234@旺财wanhellog.@！：xiaowang'
# # reg = '\d'
#
# # s = re.findall(reg,reg_String)
# # print(s)
#
# reg = '^hello'
# s = re.findall(reg,reg_String)
# print(s)
#
# reg = '\w'
# s = re.findall(reg,reg_String)
# print(s)

'''
反义代码
\W 匹配任意不是字母、数字、下划线、汉字的字符
\S 匹配任意不是空白符的字符
\D 非数字
\B 匹配不是单词开头或结束的字符
[^a]匹配除了a以外的任意字符
[^abcd]
'''

'''
限定符
* 重复零次或多次
+ 重复一次或多次
？重复零次或一次
{n} 重复n次
{n,} 重复n次或更多次
{n,m} 重复n到m次 {1,3}
'''

# reg_String = 'hellopython3333@旺财wanhellog.@！：xiaowang'
# reg = '\d{4}'
# result = re.findall(reg,reg_String)
# print(result)
#
# reg = '[0-9a-z]{4}'
# result = re.findall(reg,reg_String)
# print(result)

# ip = 'this is ip:192.168.1.123 : 172.138.2.15'
# reg = '\d{3}.\d+.\d+.\d+'
# result = re.findall(reg,ip)
# print(result)

# serach
# ip = 'this is ip:192.168.1.123 : 172.138.2.15'
# reg = '(\d{1,3}.){3}\d{1,3}'
# result = re.search(reg, ip)[0]
# print(result)

'''
search 和 findall
search 只匹配第一个
findall 匹配所有
'''

'''
组匹配
'''
# s = 'this is phone:13888888888 and this is my postcode:012345'
# reg ='this is phone:(\d{11}) and this is my postcode:(\d{6})'
# result =re.search(reg,s)
# print(result)
# result =re.search(reg,s).group(0)
# print(result)
# result =re.search(reg,s).group(1)
# print(result)
# result =re.search(reg,s).group(2)
# print(result)

# reg_String = 'HelloPythonHelloString'
# reg = 'hello'
# result = re.match(reg,reg_String,re.I).group()
# print(result)

#match 只匹配开头的


#贪婪 与非贪婪  贪婪与懒惰

'''
什么是贪婪：尽可能多的匹配
非贪婪：尽可能少的匹配
非贪婪操作符：？
这个操作符是用在* + ？后边的，要求正则匹配的越少越好
* 重复零次或更多次 ？
+ 重复一次或更多次 ？
？重复零次或一次 ？
'''
reg_String = 'pythonnnnnpythonHelloPython'
#贪婪
reg = 'python*'
result = re.findall(reg,reg_String)
print(result)
