n = int(input("Nhập n: "))
a = []
for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)
# a.
max1 = -10**9
max2 = -10**9

for i in range(n):
    if a[i] > max1:
        max2 = max1
        max1 = a[i]
    elif a[i] > max2 and a[i] != max1:
        max2 = a[i]

if max2 == -10**9:
    print("a) Không tồn tại số lớn thứ hai")
else:
    print("a) Số lớn thứ hai:", max2)
    print("   Vị trí:", end=" ")
    for i in range(n):
        if a[i] == max2:
            print(i, end=" ")
    print()

# b. 
max_len = 0
do_dai = 0

for i in range(n):
    if a[i] > 0:
        do_dai += 1
        if do_dai > max_len:
            max_len = do_dai
    else:
        do_dai = 0

print("b) Dãy dương liên tiếp dài nhất:", max_len)

# c. 
max_sum = 0
tong = 0

for i in range(n):
    if a[i] > 0:
        tong += a[i]
        if tong > max_sum:
            max_sum = tong
    else:
        tong = 0

print("c) Tổng dãy dương liên tiếp lớn nhất:", max_sum)