n = int(input("Nhập số phần tử: "))

a = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    a.append(x)

# a.
max1 = a[0]
for x in a:
    if x > max1:
        max1 = x

max2 = None
vi_tri = -1

for i in range(len(a)):
    if a[i] != max1:
        if max2 is None or a[i] > max2:
            max2 = a[i]
            vi_tri = i

print("Số lớn thứ hai:", max2)
print("Vị trí:", vi_tri)

# b
dem = 0
max_dem = 0
for x in a:
    if x > 0:
        dem += 1
        if dem > max_dem:
            max_dem = dem
    else:
        dem = 0
print("Số dương liên tiếp nhiều nhất:", max_dem)

# c
tong = 0
max_tong = 0
for x in a:
    if x > 0:
        tong += x
        if tong > max_tong:
            max_tong = tong
    else:
        tong = 0

print("Tổng dãy dương lớn nhất:", max_tong)