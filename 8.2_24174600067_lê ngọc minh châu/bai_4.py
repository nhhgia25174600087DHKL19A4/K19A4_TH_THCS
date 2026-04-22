def dao_nguoc(ds):
    i = 0
    j = len(ds) - 1
    
    while i < j:
        ds[i], ds[j] = ds[j], ds[i]
        i = i + 1
        j = j - 1
    
    return ds

n = int(input("Nhap so luong: "))
ds = []
i = 0
while i < n:
    x = int(input("Nhap so: "))
    ds.append(x)
    i = i + 1
print("Danh sach ban dau:", ds)
print("Dao nguoc:", dao_nguoc(ds))