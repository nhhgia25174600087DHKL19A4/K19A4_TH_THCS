def dao_nguoc():
    n = int(input("Nhập số phần tử: "))
    ds = []

    for i in range(n):
        x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
        ds = ds + [x]

    dao = []

    for i in range(n - 1, -1, -1):
        dao = dao + [ds[i]]

    return ds, dao

a, b = dao_nguoc()

print("Danh sách ban đầu:", a)
print("Danh sách đảo ngược:", b)