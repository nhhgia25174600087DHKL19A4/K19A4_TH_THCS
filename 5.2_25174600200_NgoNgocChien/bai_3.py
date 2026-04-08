a = []
while True:
    x = int(input("Nhập số: "))
    if x == 0:
        break
    a.append(x)
#a
b = []
c = []
for i in range(len(a)):
    if a[i] > 0:
        b.append(a[i])
    else:
        c.append(a[i])
a = b + c
print("Danh sách sau khi đưa số dương lên đầu:")
print(a)
#b
m = int(input("Nhập m: "))
a.insert(0, m)
a.append(m)
if len(a) >= 5:
    a.insert(4, m)
print("Danh sách sau khi chèn:")
print(a)