n = int(input("Nhập n: "))
a = []

for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)

b = list(map(lambda x: x*x, a))

print("List ban đầu:", a)
print("List bình phương:", b)