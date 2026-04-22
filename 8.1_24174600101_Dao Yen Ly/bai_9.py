a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

print("Cong:", a + b)
print("Tru:", a - b)
print("Nhan:", a * b)

if b != 0:
    print("Chia:", a / b)
else:
    print("Khong chia duoc")

# luy thua
n = int(input("Nhap mu: "))
kq = 1
for i in range(n):
    kq = kq * a

print("a^n =", kq)