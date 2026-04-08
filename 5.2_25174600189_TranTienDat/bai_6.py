a = []
for i in range(1000):
    a.append(i)

# dùng hàm sorted
b = sorted(a)
print(b[:10])

# không dùng hàm sorted
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a[:10])