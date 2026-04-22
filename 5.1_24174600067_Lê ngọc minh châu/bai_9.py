m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
t = tuple(range(m, n+1))
mid = len(t) // 2
tp1 = t[:mid]
tp2 = t[mid:]
print(tp1)
print(tp2)