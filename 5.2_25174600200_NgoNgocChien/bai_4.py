a = []
while True:
    x = int(input("Nhập số: "))
    if x == 0:
        break
    a.append(x)
#a
b = [1,2,3]
a = b + a
a = a + b
if len(a) >= 5:
    a = a[:4] + b + a[4:]
print("Danh sách sau khi chèn:", a)
#b
k = int(input("Nhập vị trí k: "))
if 0 <= k < len(a):
    for i in range(k, len(a)-1):
        a[i] = a[i+1]
    a.pop()
print("Danh sách sau khi xóa:", a)
#c
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("Tang dan:", a)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("Giảm dần:", a)