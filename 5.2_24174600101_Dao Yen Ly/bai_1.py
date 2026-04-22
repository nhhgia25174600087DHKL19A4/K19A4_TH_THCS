a = list(map(int, input("nhap danh sach: ").split()))

# a. tong
tong = 0
for i in range(len(a)):
    tong = tong + a[i]
print("tong:", tong)

# b. dem so duong va tong duong
dem = 0
tong_duong = 0

for i in range(len(a)):
    if a[i] > 0:
        dem = dem + 1
        tong_duong = tong_duong + a[i]

print("so duong:", dem)
print("tong duong:", tong_duong)

# c. vi tri so am dau tien
vt_am = -1
for i in range(len(a)):
    if a[i] < 0:
        vt_am = i
        break

print("vi tri am dau:", vt_am)

# d. vi tri so duong cuoi
vt_duong = -1
for i in range(len(a)):
    if a[i] > 0:
        vt_duong = i

print("vi tri duong cuoi:", vt_duong)

# e. max va vi tri cuoi cua max
maxx = a[0]
for i in range(len(a)):
    if a[i] > maxx:
        maxx = a[i]

vt_max = -1
for i in range(len(a)):
    if a[i] == maxx:
        vt_max = i

print("max:", maxx)
print("vi tri max cuoi:", vt_max)