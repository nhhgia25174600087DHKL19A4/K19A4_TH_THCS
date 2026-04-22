while True:
    m = int(input("Nhap m: "))
    n = int(input("Nhap n: "))   
    if m > 0 and m < n:
        break
    else:
        print("Nhap sai, nhap lai!")
ds = []
i = m
dem = 0
while i <= n and dem < 100:
    ds.append(i)
    i = i + 2
    dem = dem + 1
tong = 0
for x in ds:
    tong = tong + x
print("Danh sach la:")
print(ds)
print("Tong la:", tong)