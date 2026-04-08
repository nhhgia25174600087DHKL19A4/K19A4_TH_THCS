n = int(input("Nhap so phan tu: "))
a = []
for i in range(n):
    x = int(input("Nhap phan tu thu " + str(i) + ": "))
    a.append(x)

#a, Tinh tong cac phan tu 
tong = 0
for i in range(n):
    tong = tong + a[i]
print("Tong =", tong)

#b, Dem so luong so duong va tinh tong so duong
dem_duong = 0
tong_duong = 0
for i in range(n):
    if a[i] > 0:
        dem_duong = dem_duong + 1
        tong_duong = tong_duong + a[i]
print("So luong so duong =", dem_duong)
print("Tong so duong =", tong_duong)

#c, Tim vi tri phan tu am dau tien
vi_tri_am = -1
for i in range(n):
    if a[i] < 0:
        vi_tri_am = i
        break
print("Vi tri am dau tien =", vi_tri_am)

#d,Tim vi tri phan tu duong cuoi cung
vi_tri_duong = -1
for i in range(n-1, -1, -1):
    if a[i] > 0:
        vi_tri_duong = i
        break
print("Vi tri duong cuoi =", vi_tri_duong)

#e, Tim phan tu lon nhat va vi tri cuoi cua no
max_val = a[0]

for i in range(1, n):
    if a[i] > max_val:
        max_val = a[i]
vi_tri_max = -1
for i in range(n):
    if a[i] == max_val:
        vi_tri_max = i
print("Gia tri lon nhat =", max_val)
print("Vi tri cuoi cua max =", vi_tri_max)