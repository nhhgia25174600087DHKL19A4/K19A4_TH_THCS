def mu(a, b):
    kq = 1
    i = 0
    while i < b:
        kq = kq * a
        i = i + 1
    return kq
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
n = int(input("Nhap n: "))
print("Cong:", a + b)
print("Tru:", a - b)
print("Nhan:", a * b)
if b != 0:
    print("Chia:", a / b)
print("a^(b+n):", mu(a, b + n))
print("b^(n+2):", mu(b, n + 2))