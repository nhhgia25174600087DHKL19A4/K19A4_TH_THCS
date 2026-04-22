a = []
while True:
    x = int(input("Nhap so (0 dung): "))
    if x == 0:
        break
    a = a + [x]

#a,chen [1,2,3]
a = [1,2,3] + a + [1,2,3]
if len(a) >= 5:
    a = a[:4] + [1,2,3] + a[4:]
print(a)

#b,xoa phan tu k
k = int(input("Nhap k: "))
if 0 <= k < len(a):
    for i in range(k, len(a)-1):
        a[i] = a[i+1]
    a = a[:-1]
print(a)

#c,sap xep tang 
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print("Tang =", a)

# giam
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] < a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print("Giam =", a)