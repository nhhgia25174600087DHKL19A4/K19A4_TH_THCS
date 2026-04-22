a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a += [x]
#a. 
b = []
for x in [1, 2, 3]:
    b += [x]
for x in a:
    b += [x]
for x in [1, 2, 3]:
    b += [x]
c = []
if len(b) >= 4:
    for i in range(len(b)):
        if i == 4:
            for x in [1, 2, 3]:
                c += [x]
        c += [b[i]]
else:
    c = b
print("a) Sau khi chèn:", c)
#b. 
k = int(input("Nhập k: "))
d = []
if 0 <= k < len(c):
    for i in range(len(c)):
        if i != k:
            d += [c[i]]
else:
    print("k không hợp lệ")
    d = c
print("b) Sau khi xóa:", d)
#c.Sắp xếp tăng dần
for i in range(len(d)):
    for j in range(i+1, len(d)):
        if d[i] > d[j]:
            d[i], d[j] = d[j], d[i]
print("c) Tăng dần:", d)
#Sắp xếp giảm dần
for i in range(len(d)):
    for j in range(i+1, len(d)):
        if d[i] < d[j]:
            d[i], d[j] = d[j], d[i]
print("   Giảm dần:", d)