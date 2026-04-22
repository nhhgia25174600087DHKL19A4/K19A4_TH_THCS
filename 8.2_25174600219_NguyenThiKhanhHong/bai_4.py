def dao_ds(ds):
    kq = []
    for i in range(len(ds) - 1, -1, -1):
        kq.append(ds[i])
    return kq
n = int(input("Nhập số phần tử: "))
ds = []
for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    ds.append(x)
ds_dao = dao_ds(ds)
print("Danh sách ban đầu:", ds)
print("Danh sách đảo ngược:", ds_dao)