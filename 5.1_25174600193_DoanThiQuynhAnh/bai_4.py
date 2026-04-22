m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
ds = []
dem = 0
i = m
while i <= n and dem < 100:
    ds.append(i)
    i = i + 2
    dem = dem + 1
tong = 0
for x in ds:
    tong = tong + x
print("Danh sach:", ds)
print("Tong :", tong)