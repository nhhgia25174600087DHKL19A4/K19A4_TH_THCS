def dao_nguoc(ds):
    ds_moi = []
    i = len(ds) - 1

    print("Dang dao nguoc danh sach...")

    while i >= 0:
        ds_moi.append(ds[i])
        i = i - 1

    return ds_moi


n = int(input("Nhap n: "))
ds = []

for i in range(n):
    x = int(input("Nhap so: "))
    ds.append(x)

print("Danh sach ban dau:", ds)

kq = dao_nguoc(ds)

print("Danh sach sau khi dao:", kq)