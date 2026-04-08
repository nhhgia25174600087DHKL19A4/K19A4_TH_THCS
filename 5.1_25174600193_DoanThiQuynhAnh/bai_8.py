ds = []

while True:
    x = input("Nhap so: ")
    if x == "0":
        break
    ds.append(int(x))

print(ds)
ds = []

n = int(input("Nhap so phan tu: "))
for i in range(n):
    x = int(input("Nhap phan tu: "))
    ds.append(x)

print("Danh sach ban dau:", ds)

x = int(input("Nhap gia tri can tim: "))

vitri = -1
for i in range(len(ds)):
    if ds[i] == x:
        vitri = i
        break

if vitri != -1:
    print("Tim thay tai vi tri:", vitri)
else:
    print("Khong tim thay")

if vitri != -1:
    moi = int(input("Nhap gia tri moi: "))
    ds[vitri] = moi

print("Danh sach sau khi sua:", ds)

y = int(input("Nhap y can them: "))

ds.insert(0, y)
ds.append(y)
giua = len(ds)//2
ds.insert(giua, y)

print("Danh sach sau khi them:", ds)

print("Truoc sap xep:", ds)

for i in range(len(ds)):
    for j in range(i+1, len(ds)):
        if ds[i] < ds[j]:
            temp = ds[i]
            ds[i] = ds[j]
            ds[j] = temp

print("Sau sap xep giam dan:", ds)

print("Danh sach truoc khi xoa:", ds)

xoa = int(input("Nhap gia tri can xoa: "))

if xoa in ds:
    ds.remove(xoa)

print("Danh sach sau khi xoa:", ds)