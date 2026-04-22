a = [0]*100
n = 0
while True:
    x = int(input())
    if x == 0:
        break
    a[n] = x
    n = n + 1

# a
b = [0]*n
k = 0
for i in range(n):
    if a[i] > 0:
        b[k] = a[i]
        k = k + 1
for i in range(n):
    if a[i] <= 0:
        b[k] = a[i]
        k = k + 1

print("Sau khi sắp xếp:", end=" ")
for i in range(n):
    print(b[i], end=" ")
print()

# b
x = int(input("Nhap so chen: "))

for i in range(n, 0, -1):
    b[i] = b[i-1]
b[0] = x
n = n + 1

b[n] = x
n = n + 1
if n >= 5:
    for i in range(n, 4, -1):
        b[i] = b[i-1]
    b[4] = x
    n = n + 1
print("Danh sach:", end=" ")
for i in range(n):
    print(b[i], end=" ")
print()


t = tuple(b[:n])
print("Tuple:", t)