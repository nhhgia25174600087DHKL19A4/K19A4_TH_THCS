n = int(input("Nhap n: "))
a = []

for i in range(n):
    a.append(int(input("Nhap phan tu: ")))

max1 = a[0]
for i in range(len(a)):
    if a[i] > max1:
        max1 = a[i]

max2 = None
vitri = -1

for i in range(len(a)):
    if a[i] != max1:
        if max2 == None or a[i] > max2:
            max2 = a[i]
            vitri = i

print("Gia tri lon thu hai:", max2)
print("Vi tri:", vitri)

dem = 0
max_dem = 0

for i in range(len(a)):
    if a[i] > 0:
        dem += 1
        if dem > max_dem:
            max_dem = dem
    else:
        dem = 0

print("So duong lien tiep nhieu nhat:", max_dem)

tong = 0
max_tong = 0

for i in range(len(a)):
    if a[i] > 0:
        tong += a[i]
        if tong > max_tong:
            max_tong = tong
    else:
        tong = 0

print("Tong day so duong lien tiep lon nhat:", max_tong)
