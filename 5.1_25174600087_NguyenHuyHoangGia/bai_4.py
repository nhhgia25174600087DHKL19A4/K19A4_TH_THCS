while True:
    m = int(input("Nhap m: "))
    n = int(input("Nhap n: "))
    if 0 < m < n:
        break
    else:
        print("Hay nhap lai")
ds_so = []
for i in range(m, n + 1, 2):
    ds_so.append(i)
    if len(ds_so) == 100:
        break
tong = 0
for so in ds_so:
    tong = tong + so
print("Danh sach cac so lay đuoc la:", ds_so)
print("Tong cua cac so đo la:", tong)