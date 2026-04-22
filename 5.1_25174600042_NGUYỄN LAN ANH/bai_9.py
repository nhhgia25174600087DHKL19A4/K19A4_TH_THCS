m = int(input("Nhap m: "))
n = int(input("Nhap n: "))

t = ()
for i in range(m, n + 1):
    t = t + (i,)

print("Tuple ban dau:", t)

mid = len(t) // 2

tp1 = t[:mid]
tp2 = t[mid:]

print("tp1:", tp1)
print("tp2:", tp2)