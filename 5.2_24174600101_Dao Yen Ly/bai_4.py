n = int(input("nhap n: "))

a = [0] * n

for i in range(n):
    a[i] = int(input())

# a. them [1,2,3] vao dau va cuoi
b = [0] * (n + 6)
k = 0

b[k] = 1; k += 1
b[k] = 2; k += 1
b[k] = 3; k += 1

for i in range(n):
    b[k] = a[i]
    k += 1

b[k] = 1; k += 1
b[k] = 2; k += 1
b[k] = 3; k += 1

print("sau khi them:")
for i in range(k):
    print(b[i], end=" ")
print()

# b. xoa phan tu thu k
k_del = int(input("nhap vi tri can xoa: "))

c = [0] * (k - 1)
k2 = 0

for i in range(k):
    if i != k_del:
        c[k2] = b[i]
        k2 += 1

print("sau khi xoa:")
for i in range(k2):
    print(c[i], end=" ")
print()

# c. sap xep tang dan 

for i in range(k2):
    for j in range(i+1, k2):
        if c[i] > c[j]:
            temp = c[i]
            c[i] = c[j]
            c[j] = temp

print("tang dan:")
for i in range(k2):
    print(c[i], end=" ")
print()

# sap xep giam dan

for i in range(k2):
    for j in range(i+1, k2):
        if c[i] < c[j]:
            temp = c[i]
            c[i] = c[j]
            c[j] = temp

print("giam dan:")
for i in range(k2):
    print(c[i], end=" ")