# 1 列表数据类型
# list1 = [1,2,3,4,5,6,7]
# print(list1) # [1, 2, 3, 4, 5, 6, 7]

# 2 列表元素类型多样 支持数字，字符串，列表嵌套
# 3 列表元素访问 -1表示倒数第一个
# list1 = [1,2,3,"abc",[4,5,6]]
# print(list1) # [1, 2, 3, 'abc', [4, 5, 6]]
# print(list1[2]) # 3
# print(list1[3]) # abc
# print(list1[-2]) # abc
# print(list1[-1][0]) # 4
# print(list1[-1][-2:-1]) # [5]

# 3 列表拼接
# str1 = [1,2,3]
# str2 = [4,5,6]
# print(str1 + str2) # [1, 2, 3, 4, 5, 6]

# 4 重复拼接
# str1 = "abd" * 3
# print(str1) # abdabdabd

# 5 删除列表元素
# list = ["hello", 'world', 566]
# print(list) # ['hello', 'world', 566]
# del list[1]
# print(list) # ['hello', 566]

# 6  列表脚本操作符
# list = [1, 2, 3]
# print(len(list)) # 3
# print(list + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
# print(list * 4) # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(3 in list) # True
# for x in list:
#     print(x, end= " ") # 1 2 3
