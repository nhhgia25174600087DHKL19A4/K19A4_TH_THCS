tp = tuple(map(int, input("Nhập các số: ").split()))
n = int(input("Nhập n: "))
ket_qua = ()
for x in tp:
    if x % 2 != 0:
        ket_qua += (x,)
        if len(ket_qua) == n:
            break
print("Tuple kết quả:", ket_qua)