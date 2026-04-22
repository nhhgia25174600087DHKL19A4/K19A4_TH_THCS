
n = int(input("Nhập số phần tử: "))
ds = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    ds.append(x)

tp = tuple(ds)
ket_qua = []
for x in tp:
    if x > 0 and x % 2 != 0:
        ket_qua.append(x)

tp_moi = tuple(ket_qua)

print("Tuple ban đầu:", tp)
print("Tuple số lẻ dương:", tp_moi)