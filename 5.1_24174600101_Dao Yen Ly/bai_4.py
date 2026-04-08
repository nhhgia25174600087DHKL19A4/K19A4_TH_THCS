while True:
    m = int(input("Nhap m: "))
    n = int(input("Nhap n: "))
    
    if m > 0 and m < n:
        break

a = []

for i in range(m, n+1, 2):
    a.append(i)

a = a[0:100]

tong = 0
for i in a:
    tong = tong + i

print(a)
print("Tong =", tong)