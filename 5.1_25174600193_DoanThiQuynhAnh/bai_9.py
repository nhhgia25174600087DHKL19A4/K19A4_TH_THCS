m = int(input("Nhap m: "))
n = int(input("Nhap n: "))

tp = tuple(range(m, n+1))

print("Tuple ban dau:", tp)

mid = len(tp)//2

tp1 = tp[:mid]
tp2 = tp[mid:]

print("tp1 =", tp1)
print("tp2 =", tp2)