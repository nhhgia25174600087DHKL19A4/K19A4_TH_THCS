a = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)
for i in range(len(a)):
    assert a[i] % 2 == 0
print("Tất cả số trong list đều chẵn")