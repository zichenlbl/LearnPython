num = 2**100
print(num)
count = 0
while num > 0:
    if num % 10 == 6:
        count += 1
    num //= 10
print(count)
