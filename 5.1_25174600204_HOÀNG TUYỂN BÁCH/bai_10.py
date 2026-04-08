
n = int(input("Nhập số lượng phần tử n của tuple: "))
tp = ()
print("Nhập các số nguyên cho tuple:")
for i in range(n):
    so = int(input(f"Phần tử {i+1}: "))
    tp = tp + (so,)

print("Tuple ban đầu:", tp)
lst_le = []
for num in tp:
    if num > 0 and num % 2 != 0:
        lst_le.append(num)
tp_le = tuple(lst_le)
print("Tuple chỉ chứa số nguyên dương lẻ:", tp_le)