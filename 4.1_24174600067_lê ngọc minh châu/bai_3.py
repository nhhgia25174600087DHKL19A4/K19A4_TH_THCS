a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
kq = 0
while b > 0:
    if b % 2 != 0:
        kq = kq + a
    a = a * 2
    b = b // 2
print("Ket qua:", kq)