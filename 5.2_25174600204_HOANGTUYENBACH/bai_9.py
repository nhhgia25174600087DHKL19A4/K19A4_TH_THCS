
a = []
n = int(input("Nhập số phần tử: "))

for i in range(n):
    x = int(input(f"Nhập a[{i}]: "))
    a.append(x)

for i in range(n):
    assert a[i] % 2 == 0, "Danh sách có phần tử không phải số chẵn!"

print("Tất cả các phần tử đều là số chẵn.")