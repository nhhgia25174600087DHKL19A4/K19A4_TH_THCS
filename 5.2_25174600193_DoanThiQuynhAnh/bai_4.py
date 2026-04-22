a = []

while True:
    x = int(input("Nhap phan tu (0 de dung): "))
    if x == 0:
        break
    a.append(x)

b = [1, 2, 3]

a = b + a
a = a + b

if len(a) >= 5:
    for i in range(len(b)):
        a.insert(4 + i, b[i])

print(a)

k = int(input("Nhap vi tri k can xoa: "))
if 0 <= k < len(a):
    a.pop(k)

print(a)

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t

print(a)

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] < a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t

print(a)
