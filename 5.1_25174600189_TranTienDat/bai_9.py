m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

t = ()
for i in range(m, n+1):
    t = t + (i,)

mid = len(t)//2

tp1 = t[:mid]
tp2 = t[mid:]

print(tp1)
print(tp2)