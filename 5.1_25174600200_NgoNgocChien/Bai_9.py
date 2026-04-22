m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
a = []
for i in range(m, n+1):
    a.append(i)
t = tuple(a)
mid = len(t)//2
tp1 = t[:mid]
tp2 = t[mid:]
print("Tuple ban dau:", t)
print("tp1:", tp1)
print("tp2:", tp2)