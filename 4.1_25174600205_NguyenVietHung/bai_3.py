a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
tong = 0
while b > 0:
    if b % 2 != 0:
        tong = tong + a
    a = a * 2
    b = b // 2
print(tong)