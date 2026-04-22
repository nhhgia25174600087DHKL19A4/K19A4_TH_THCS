n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

ds = []
for i in range(m, n + 1, 2):
    if len(ds) < 100:
        ds.append(i)
ket_qua = tuple(ds)

print("Kết quả là: ", ket_qua)
print("Tổng các số là: ", sum(ket_qua))