
while True:
    m = int(input("Nhập m (0 < m < n): "))
    n = int(input("Nhập n (m < n): "))
    if 0 < m < n:
        break
    else:
        print("Giá trị không hợp lệ, nhập lại.")
tp = ()
for i in range(m, n+1):
    tp = tp + (i,)
print("Tuple gốc:", tp)
lst1 = []
lst2 = []
mid = len(tp) // 2
for i in range(len(tp)):
    if i < mid:
        lst1.append(tp[i])
    else:
        lst2.append(tp[i])
tp1 = tuple(lst1)
tp2 = tuple(lst2)
print("Nửa đầu (tp1):", tp1)
print("Nửa cuối (tp2):", tp2)