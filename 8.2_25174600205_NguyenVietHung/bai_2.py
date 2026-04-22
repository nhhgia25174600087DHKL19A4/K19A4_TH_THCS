def tao_danh_sach():
    n = int(input("Nhập số phần tử n: "))
    ds = []

    for i in range(n):
        x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
        ds = ds + [x]

    bp = list(map(lambda t: t * t, ds))

    return ds, bp


a, b = tao_danh_sach()

print("Danh sách ban đầu:", a)
print("Danh sách bình phương:", b)