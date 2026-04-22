a = []

while True:
    x = int(input("Nhap phan tu (0 de dung): "))
    if x == 0:
        break
    a.append(x)

duong = []
khac = []

for i in range(len(a)):
    if a[i] > 0:
        duong.append(a[i])
    else:
        khac.append(a[i])

a = duong + khac
print(a)

m = int(input("Nhap m: "))

a.insert(0, m)
a.append(m)

if len(a) >= 5:
    a.insert(4, m)

print(a)
