n = int(input("Nhập số phần tử n: "))
a = []

for i in range(n):
    x = int(input(f"Nhập a[{i}]: "))
    a.append(x)
# a
max1 = a[0]
max2 = a[0]
vt = -1

# tìm max1
for i in range(n):
    if a[i] > max1:
        max1 = a[i]

# tìm max2 (khác max1)
for i in range(n):
    if a[i] < max1:
        max2 = a[i]
        break

for i in range(n):
    if a[i] < max1 and a[i] > max2:
        max2 = a[i]
for i in range(n):
    if a[i] == max2:
        vt = i

print("Giá trị lớn thứ hai:", max2)
print("Vị trí:", vt)
# b
dem = 0
max_dem = 0

for i in range(n):
    if a[i] > 0:
        dem = dem + 1
        if dem > max_dem:
            max_dem = dem
    else:
        dem = 0

print("Số lượng dương liên tiếp nhiều nhất:", max_dem)
# c
tong = 0
max_tong = 0

dem = 0
max_dem = 0

for i in range(n):
    if a[i] > 0:
        tong = tong + a[i]
        dem = dem + 1

        if tong > max_tong:
            max_tong = tong
            max_dem = dem
    else:
        tong = 0
        dem = 0

print("Số lượng phần tử của đoạn có tổng lớn nhất:", max_dem)