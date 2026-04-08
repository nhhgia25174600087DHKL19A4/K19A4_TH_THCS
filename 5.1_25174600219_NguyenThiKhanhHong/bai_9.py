m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
x = tuple(range(m, n + 1))
y = len(x) // 2
x1 = x[:y]
x2 = x[y:]
print("Tuple ban đầu:", x)
print("Nửa đầu (tp1):", x1)
print("Nửa cuối (tp2):", x2)