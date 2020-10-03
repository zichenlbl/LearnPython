# # 1 + 2 + 3 + ... + 99 + 100 = ？
# count = 0
# a = 1
# while a <= 100:
#     if a % 2 != 0:  # 1 + 3 + ... + 99 = ？
#         count += a
#     a += 1
# print(count)  # 5050 # 2500

# # for语句
# count = 0
# for i in range(1, 101, 1):  # range() 函数可创建一个整数列表，
#     count += i
# print(count)  # 5050
# # range(start, stop[, step])
# count2 = 0
# for j in range(1, 101, 2):
#     count2 += j
# print(count2)  # 2500

i = 2
while i < 20:
    j = 2
    while j <= (i / j):  # 1.0,1.5,2.0
        if not (i % j):  # 不是素数
            break
        j = j + 1
    if j > i / j:
        print(i, " 是素数")
    i = i + 1

