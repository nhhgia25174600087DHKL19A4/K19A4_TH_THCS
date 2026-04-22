a = []
while True:
    x = int(input("Nhap so (0 de dung): "))
    if x == 0:
        break
    a = a + [x]

#a,dua so duong len dau
duong = []
am = []
for i in range(len(a)):
    if a[i] > 0:
        duong = duong + [a[i]]
    else:
        am = am + [a[i]]
a = duong + am
print("Danh sach moi =", a)

#b,chen m vao dau, cuoi, vi tri 5
m = int(input("Nhap m: "))
a = [m] + a + [m]
if len(a) >= 5:
    a = a[:4] + [m] + a[4:]
print("Sau khi chen =", a)