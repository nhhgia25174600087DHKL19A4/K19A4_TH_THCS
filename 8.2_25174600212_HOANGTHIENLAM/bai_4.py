def dao_nguoc(ds):
    return ds[::-1]

n = int(input("Nhap so phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input()))
print("Ban dau:", ds)
print("Dao nguoc:", dao_nguoc(ds))