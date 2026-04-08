m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
size = n - m + 1
lst = [0] * size
for i in range(size):
    lst[i] = m + i
tp = tuple(lst)
mid = size // 2
tp1 = tp[:mid]
tp2 = tp[mid:]
print("tp1:", tp1)
print("tp2:", tp2)