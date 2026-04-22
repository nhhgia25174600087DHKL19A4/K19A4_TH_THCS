def nhap_list():
    n = int(input("Nhập số phần tử: "))
    ds = []

    for i in range(n):
        x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
        ds = ds + [x]

    return ds

def binh_phuong(ds):
    return list(map(lambda x: x * x, ds))

a = nhap_list()
b = binh_phuong(a)

print("List ban đầu:", a)
print("List bình phương:", b)