a = []
print("Nhập các số nguyên (Nhập 0 để dừng lại):")
while True:
    so = int(input("Nhập số: "))
    if so == 0:
        break
    a.append(so)
b = [1, 2, 3]
a = b + a 
a = a + b 
if len(a) >= 5:
    a = a[:4] + b + a[4:]
k = int(input("\nNhập vị trí k cần xóa (từ 1): "))
if 1 <= k <= len(a):
    a = a[:k-1] + a[k:]
    print("Danh sách sau khi xóa:", a)
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            tam = a[i]
            a[i] = a[j]
            a[j] = tam
print("\nDanh sách tăng dần:", a)
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] < a[j]:
            tam = a[i]
            a[i] = a[j]
            a[j] = tam
print("Danh sách giảm dần:", a)