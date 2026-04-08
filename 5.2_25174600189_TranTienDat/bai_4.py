a = []
while True:
    x = int(input())
    if x == 0:
        break
    a.append(x)

# a
a = [1,2,3] + a
a = a + [1,2,3]
if len(a) >= 5:
    a = a[:4] + [1,2,3] + a[4:]
print(a)

# b
k = int(input("Nhập k: "))
if 0 <= k < len(a):
    del a[k]

# c tăng dần
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print("Tăng:", a)

# giảm dần
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
print("Giảm:", a)