a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

kq = 0

while b > 0:
    if b % 2 == 1:
        kq += a
    a = a*2
    b = b // 2

print("Kết quả: ", kq)