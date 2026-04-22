def nhan(a, b):
    if b == 0:
        return 0
    if b % 2 == 0:
        return 2 * nhan(a, b // 2)
    else:
        return 2 * nhan(a, b // 2) + a
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
sign = 1
if a * b < 0:
    sign = -1
print("Kết quả:", sign * nhan(abs(a), abs(b)))