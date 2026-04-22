def tinh_P_n():
    n = int(input("Nhập số nguyên n: "))
    if n < 0:
        return
    P = 1
    for i in range(n + 1):
        P *= (2 * i + 1)
    print(f"Kết quả P({n}) = {P}")
def tinh_S_b():
    n = int(input("Nhập số nguyên n: "))
    if n < 0:
        return
    S = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            S += i
        else:
            S -= i
    print(f"Kết quả S({n}) = {S}")
def tinh_S_c():
    n = int(input("Nhập số nguyên n: "))
    if n <= 0:
        return
    S_tong = 0
    for i in range(1, n + 1):
        tong_trong_ngoac = 0
        for j in range(1, i + 1):
            tong_trong_ngoac += j
        S_tong += tong_trong_ngoac
    print(f"Kết quả S({n}) = {S_tong}")
def tinh_P_xy():
    x = float(input("Nhập giá trị x: "))
    y = float(input("Nhập giá trị y: "))
    n = int(input("Nhập số nguyên n: "))
    if n <= 1:
        return
    phan_dau = x ** y 
    tong_sigma = 0
    for k in range(1, n + 1):
        tong_sigma += (x + 32 * y + (y ** k))
    P = phan_dau + tong_sigma
    print(f"Kết quả P(x={x}, y={y}, n={n}) = {P}")
tinh_P_n()
print("-" * 40)
tinh_S_b()
print("-" * 40)
tinh_S_c()
print("-" * 40)
tinh_P_xy()