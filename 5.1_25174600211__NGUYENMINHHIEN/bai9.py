m = int(input("nhap m: "))
n = int(input("nhap n: "))
tam = []
for i in range(m, n + 1):
    tam.append(i)
t = tuple(tam)
print("Tuple ban dau:", t)
nua = len(t) // 2
tp1 = t[:nua]
tp2 = t[nua:]
print("tp1 la:", tp1)
print("tp2 la:", tp2)