n = int(input("Nhập số phần tử: "))
m = []
for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    m.append(x)
y = list(map(lambda x: x * x, m))
print("Danh sách ban đầu:", m)
print("Danh sách bình phương:", y)