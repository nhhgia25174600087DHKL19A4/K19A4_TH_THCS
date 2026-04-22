a = list(map(int, input("nhap list: ").split()))

# a. lay so chan (list)
b = [0] * len(a)
k1 = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        b[k1] = a[i]
        k1 = k1 + 1

print("so chan (list):")
for i in range(k1):
    print(b[i], end=" ")
print()

# b. binh phuong tung phan tu (tuple)
c = ()

for i in range(len(a)):
    c = c + (a[i] * a[i],)

print("binh phuong (tuple):")
print(c)

# c. lay so duong (list)
d = [0] * len(a)
k2 = 0

for i in range(len(a)):
    if a[i] > 0:
        d[k2] = a[i]
        k2 = k2 + 1

print("so duong (list):")
for i in range(k2):
    print(d[i], end=" ")