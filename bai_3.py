a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

result = 0

while b > 0:
    if b % 2 == 1:
        result += a
    a *= 2
    b //= 2

print("Kết quả:", result)