s = input("nhap day so: ")
a = s.split()

b = [0] * len(a)
k = 0

for i in range(len(a)):
    if int(a[i]) > 0:
        b[k] = int(a[i])
        k = k + 1

print("list:", end=" ")
for i in range(k):
    print(b[i], end=" ")
print()

t = ()

for i in range(len(a)):
    if int(a[i]) > 0:
        t = t + (int(a[i]),)

print("tuple:", t)