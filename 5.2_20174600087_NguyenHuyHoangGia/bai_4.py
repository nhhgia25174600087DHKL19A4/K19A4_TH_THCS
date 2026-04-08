a = []
while True:
    n = int(input("Nhập số : "))
    if n == 0:
        break
    a.append(n)
# a.
sub = [1, 2, 3]
a = sub + a
a = a + sub
if len(a) >= 5:
    a[4:4] = sub 
print("Danh sách sau khi chèn [1,2,3]:", a)
# b.
k = int(input("Nhập vị trí k cần xóa: "))
if 0 <= k < len(a):
    del a[k]
print(f"Danh sách sau khi xóa vị trí {k}:", a)
# c.
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print("Danh sách tăng dần:", a)
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
print("Danh sách giảm dần:", a)