#a
def tinh_P_a(n):
    P = 1
    for i in range(n + 1):
        P = P * (2 * i + 1)
    return P
print("P(3) =", tinh_P_a(3))
#b
def tinh_S_b(n):
    S = 0
    for i in range(1, n + 1):
        S += (-1)**(i + 1) * i
    return S
print("S(5) =", tinh_S_b(5))
#c
def tinh_S_c(n):
    S = 0
    tong_phu = 0
    
    for i in range(1, n + 1):
        tong_phu += i 
        S += tong_phu
    return S
print("S(3) =", tinh_S_c(3))
#d
def tinh_P_d(x, y, n):
    P = x**y
    for k in range(1, n + 1):
        P += (x + 32*y + y**k)
    return P
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
n = int(input("Nhập n (>1): "))
print("Kết quả P =", tinh_P_d(x, y, n))
