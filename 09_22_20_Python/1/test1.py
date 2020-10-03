# s = "BeijingJiaoTongUniversity"
# print(s[0:-1])
# print('1'+s[:len(s)]) # 1BeijingJiaoTongUniversity
# print('2'+s[:len(s)-1]) # 1BeijingJiaoTongUniversit
# print('3'+s[:]) # 1BeijingJiaoTongUniversity
# print('4'+s[:-1]) # 1BeijingJiaoTongUniversit

#
# print("hello"*2)
#
# str="4"+"5"
# print(str)

# str=r"5\5=1"
# print(str)
#
# str="5\\5=1"
# print(str)

# print("BBJJTTUU"[::2])
#
# str=","
#
# print(str.join("123"))

# str="123abc"
#
# print(str.isnumeric())

# str="ABCDEF"
#
# print(str.lower())

# str="abcdef"
#
# print(str[:2])
#
# print(str[1:])
#
# print(len(str))

#1 检测 str 是否包含在 string 中
# 如果是返回开始的索引值，否则返回-1
str1 = "sfjnn\bbbhnnbkj"
print(str1)
print(str1.find("nb", 0, len(str1))) # 10
print(str1.find("123",0,len(str1))) # -1