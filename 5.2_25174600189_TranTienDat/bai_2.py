n = int(input("Nhập n: "))
a = [int(input()) for _ in range(n)]

# a
max1 = max2 = -10**9
for x in a:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x

for i in range(len(a)):
    if a[i] == max2:
        print("Max2:", max2, "vị trí:", i)
        break

# b
max_len = cur = 0
for x in a:
    if x > 0:
        cur += 1
        if cur > max_len:
            max_len = cur
    else:
        cur = 0
print("Dãy dương dài nhất:", max_len)

# c
max_sum = cur_sum = 0
for x in a:
    if x > 0:
        cur_sum += x
        if cur_sum > max_sum:
            max_sum = cur_sum
    else:
        cur_sum = 0
print("Tổng lớn nhất:", max_sum)