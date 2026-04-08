n = int(input("Nhập n: "))
fibo = [0, 1]
for i in range(2, n + 1):
    so_moi = fibo[i-1] + fibo[i-2]
    fibo.append(so_moi)
chuoi_ket_qua = ""
for i in range(len(fibo)):
    if i == len(fibo) - 1:
        chuoi_ket_qua = chuoi_ket_qua + str(fibo[i])
    else:
        chuoi_ket_qua = chuoi_ket_qua + str(fibo[i]) + ", "
print(chuoi_ket_qua)