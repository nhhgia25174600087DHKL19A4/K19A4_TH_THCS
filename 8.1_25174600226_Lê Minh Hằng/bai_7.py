#UCLN
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
ucln = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        ucln = i
print("UCLN:", ucln)
#BCNN
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
i = max(a, b)
while True:
    if i % a == 0 and i % b == 0:
        print("BCNN:", i)
        break
    i += 1
#Rút gọn
tu = int(input("Nhập tử: "))
mau = int(input("Nhập mẫu: "))
ucln = 1
for i in range(1, min(tu, mau) + 1):
    if tu % i == 0 and mau % i == 0:
        ucln = i
print("Phân số rút gọn:", tu//ucln, "/", mau//ucln)