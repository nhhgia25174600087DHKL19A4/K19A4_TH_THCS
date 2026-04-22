def P(n):
    tich = 1
    for i in range(n + 1):
        tich *= (2 * i + 1)
    return tich
def S1(n):
    tong = 0
    for i in range(1, n + 1):
        tong += (-1) ** (i + 1) * i
    return tong
def S2(n):
    tong = 0
    for i in range(1, n + 1):
        tong_con = 0
        for j in range(1, i + 1):
            tong_con += j
        tong += tong_con
    return tong
n = int(input("Nhập n: "))
print("P(n) =", P(n))
print("S1(n) =", S1(n))
print("S2(n) =", S2(n))