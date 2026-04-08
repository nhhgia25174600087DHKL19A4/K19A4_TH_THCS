n = int(input("Nhập n: "))
a = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    a.append(x)
#a
max1 = a[0]
max2 = -999999
for i in range(n):
    if a[i] > max1:
        max2 = max1
        max1 = a[i]
    elif a[i] > max2 and a[i] != max1:
        max2 = a[i]
vitri = -1
for i in range(n):
    if a[i] == max2:
        vitri = i
print("Số lớn thứ hai:", max2)
print("Vị trí:", vitri)
#b
dem = 0
max_dem = 0

for i in range(n):
    if a[i] > 0:
        dem = dem + 1
        if dem > max_dem:
            max_dem = dem
    else:
        dem = 0

print("Số dương liên tiếp nhiều nhất:", max_dem)
#c
tong = 0
max_tong = 0
for i in range(n):
    if a[i] > 0:
        tong = tong + a[i]
        if tong > max_tong:
            max_tong = tong
    else:
        tong = 0
print("Tổng dương liên tiếp lớn nhất:", max_tong)