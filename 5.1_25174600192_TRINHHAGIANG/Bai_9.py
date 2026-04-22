m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

while m <= 0 or m >= n:
    print("Sai điều kiện.Nhập lại")
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))

tp = tuple(range(m, n + 1))
mid = len(tp) // 2
tp1 = tp[:mid]
tp2 = tp[mid:]

print("Tuple ban đầu:", tp)
print("Nửa đầu (tp1):", tp1)
print("Nửa cuối (tp2):", tp2)