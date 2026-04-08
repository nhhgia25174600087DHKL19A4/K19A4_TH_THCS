while True:
    m = int(input("Nhap m: "))
    n = int(input("Nhap n: "))
    if 0 < m < n:
        break
    else:
        print("Hay nhap lai")
ds_so = list(range(m, n + 1))
ket_qua = list(lambda x: x % 2 == 0, ds_so)
print("Danh sach cac so chan la:")
print(ket_qua)