m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
a = list(range(m, n + 1))
ket_qua = []
for i in a:
    if i % 2 == 0:
        ket_qua.append(i)
print("Danh sách:", a)
print("Số chẵn:", ket_qua)                