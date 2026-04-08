n = int(input("Nhập số lượng n: "))
ds_le = []
so = 1
while len(ds_le) < n:
    if so % 2 != 0:
        ds_le.append(so)
    so += 1

ket_qua = tuple(ds_le)
print("Tuple số lẻ:", ket_qua)