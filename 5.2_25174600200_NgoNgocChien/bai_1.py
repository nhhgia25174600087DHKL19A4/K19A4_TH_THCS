n = int(input("Nhập n: "))
a = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    a.append(x)
#a
tong = 0
for i in range(n):
    tong = tong + a[i]
print("Tổng các phần tử:", tong)
#b
dem_duong = 0
tong_duong = 0
for i in range(n):
    if a[i] > 0:
        dem_duong = dem_duong + 1
        tong_duong = tong_duong + a[i]
print("Số lượng số dương:", dem_duong)
print("Tổng số dương:", tong_duong)
#c
vitri_am = -1
for i in range(n):
    if a[i] < 0:
        vitri_am = i
        break
print("Vị trí số âm đầu tiên:", vitri_am)
#d
vitri_duong = -1
for i in range(n):
    if a[i] > 0:
        vitri_duong = i
print("Vị trí số dương cuối cùng:", vitri_duong)
#e
max_value = a[0]
vitri_max = 0
for i in range(n):
    if a[i] >= max_value:
        max_value = a[i]
        vitri_max = i
print("Giá trị lớn nhất:", max_value)
print("Vị trí cuối của max:", vitri_max)