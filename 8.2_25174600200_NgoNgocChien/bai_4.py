def dao_nguoc(ds):
    ds_moi = []
    for i in range(len(ds) - 1, -1, -1):
        ds_moi.append(ds[i])
    return ds_moi
n = int(input("Nhập số phần tử n: "))
ds = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    ds.append(x)
print("Danh sách ban đầu:", ds)
ds_dao = dao_nguoc(ds)
print("Danh sách sau khi đảo:", ds_dao)