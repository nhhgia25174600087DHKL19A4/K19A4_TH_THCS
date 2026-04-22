def kiem_tra_nt(x):
    if x < 2:
        return False

    dem = 0
    for i in range(1, x + 1):
        if x % i == 0:
            dem = dem + 1

    if dem == 2:
        return True
    else:
        return False


def tao_danh_sach():
    n = int(input("Nhập số phần tử n: "))
    ds = []

    for i in range(n):
        x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
        ds = ds + [x]

    return ds

a = tao_danh_sach()

print("Danh sách:", a)
print("Các số nguyên tố:")

for so in a:
    if kiem_tra_nt(so):
        print(so, end=" ")