def luy_thua(a, n):
    ket_qua = 1
    for i in range(n):
        ket_qua *= a
    return ket_qua
# Nhập dữ liệu
a = int(input("Nhập số a: "))
n = int(input("Nhập số n: "))
print("Kết quả:", luy_thua(a, n))