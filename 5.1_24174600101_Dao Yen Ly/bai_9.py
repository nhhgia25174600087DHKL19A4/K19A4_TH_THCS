m = int(input("Nhap m: "))
n = int(input("Nhap n: "))

a = []
i = m

while i <= n:
    a.append(i)
    i = i + 1

t = tuple(a)

print("Tuple ban dau:", t)

d = len(t)//2

tp1 = t[:d]
tp2 = t[d:]

print("tp1:", tp1)
print("tp2:", tp2)