m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
temp_list = []
for i in range(m, n + 1):
    temp_list.append(i)
tup = tuple(temp_list)
print("Tuple ban dau:", tup)
mid = len(tup) // 2
tp1 = tup[:mid]
tp2 = tup[mid:]
print("tp1 =", tp1)
print("tp2 =", tp2)