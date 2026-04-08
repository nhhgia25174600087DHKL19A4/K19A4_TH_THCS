a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a += [x]
# a.
b = []
for x in a:
    if x > 0:
        b += [x]
for x in a:
    if x <= 0:
        b += [x]
print("a) Danh sách sau khi đưa số dương lên đầu:")
print(b)
# b. 
m = int(input("Nhập m: "))
c = []
c += [m]
for x in b:
    c += [x]
c += [m]
d = []
if len(c) >= 4:
    for i in range(len(c)):
        if i == 4:
            d += [m]
        d += [c[i]]
else:
    print("Không đủ phần tử để chèn vào vị trí thứ 5")
    d = c

print("b) Danh sách sau khi chèn:")
print(d)