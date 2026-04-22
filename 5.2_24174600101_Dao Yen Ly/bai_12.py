s = input("nhap day so: ")
a = s.split()

# a. binh phuong 
b = [0] * len(a)

for i in range(len(a)):
    b[i] = int(a[i]) * int(a[i])

print("a:", end=" ")
for i in range(len(b)):
    print(b[i], end=" ")
print()

# b. lap doi 
c = ()

for i in range(len(a)):
    x = int(a[i])
    c = c + (x,)
    c = c + (x,)

print("b:", c)

# c. vi tri chan 
d = [0] * len(a)
k1 = 0

for i in range(len(a)):
    if i % 2 == 0:
        d[k1] = int(a[i])
        k1 = k1 + 1

print("c:", end=" ")
for i in range(k1):
    print(d[i], end=" ")
print()

# d. vi tri le 
e = ()

for i in range(len(a)):
    if i % 2 != 0:
        e = e + (int(a[i]),)

print("d:", e)

# e. dao nguoc 
f = [0] * len(a)

for i in range(len(a)):
    f[i] = int(a[len(a) - 1 - i])

print("e:", end=" ")
for i in range(len(f)):
    print(f[i], end=" ")
print()

# f. so duong 
g = ()

for i in range(len(a)):
    if int(a[i]) > 0:
        g = g + (int(a[i]),)

print("f:", g)
