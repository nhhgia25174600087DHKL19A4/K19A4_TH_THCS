n = int(input("Nhap so phan tu: "))
a = [0] * n
for i in range(n):
    a[i] = int(input("Nhap phan tu thu " + str(i) + ": "))

#a, tim phan tu lon thu hai va vi tri cua no
max1 = a[0]
for i in range(1, n):
    if a[i] > max1:
        max1 = a[i]
max2 = None
for i in range(n):
    if a[i] != max1:
        if max2 is None or a[i] > max2:
            max2 = a[i]
vi_tri_max2 = -1
for i in range(n):
    if a[i] == max2:
        vi_tri_max2 = i
        break
print("So lon thu hai =", max2)
print("Vi tri =", vi_tri_max2)

#b,dem so duong lien tiep nhieu nhat
dem = 0
max_dem = 0
for i in range(n):
    if a[i] > 0:
        dem = dem + 1
        if dem > max_dem:
            max_dem = dem
    else:
        dem = 0
print("So duong lien tiep nhieu nhat =", max_dem)

#c,tong lon nhat cua day duong lien tiep
tong = 0
max_tong = 0
for i in range(n):
    if a[i] > 0:
        tong = tong + a[i]
        if tong > max_tong:
            max_tong = tong
    else:
        tong = 0
print("Tong lon nhat =", max_tong)