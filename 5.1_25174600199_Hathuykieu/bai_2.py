n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
lst = [i**2 for i in range(1, n + 1)]
ket_qua = []
for i in range(m, n):
    ket_qua.append(lst[i])
print(ket_qua)