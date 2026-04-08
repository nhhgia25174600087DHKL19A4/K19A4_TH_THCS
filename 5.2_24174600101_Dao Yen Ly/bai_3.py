n = int(input("nhap so luong: "))

a = [0] * n

for i in range(n):
    a[i] = int(input())

# a. dua so duong len dau
b = [0] * n
k = 0

for i in range(n):
    if a[i] > 0:
        b[k] = a[i]
        k = k + 1

for i in range(n):
    if a[i] <= 0:
        b[k] = a[i]
        k = k + 1

print("sau khi doi:")
for i in range(n):
    print(b[i], end=" ")
print()

# b. chen so m
m = int(input("nhap m: "))

c = [0] * (n + 3)
k2 = 0

c[k2] = m
k2 = k2 + 1

for i in range(n):
    c[k2] = b[i]
    k2 = k2 + 1

c[k2] = m
k2 = k2 + 1

if n >= 5:
    
    for i in range(k2, 4, -1):
        c[i] = c[i-1]
    c[4] = m
    k2 = k2 + 1

print("sau khi chen:")
for i in range(k2):
    print(c[i], end=" ")