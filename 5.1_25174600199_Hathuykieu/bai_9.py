m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
tp = tuple(range(m, n + 1))
tp1 = ()
tp2 = ()
for i in range(len(tp)):
    if i < len(tp) // 2:
        tp1 += (tp[i],)
    else:
        tp2 += (tp[i],)
print("Tuple ban đầu:", tp)
print("tp1:", tp1)
print("tp2:", tp2)