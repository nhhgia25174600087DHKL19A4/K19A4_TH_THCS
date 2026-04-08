while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    print("Sai điều kiện, nhập lại!")
lst = []
i = m
while i <= n and len(lst) < 100:
    lst.append(i)
    i += 2
print("Danh sách:", lst)
print("Tổng:", sum(lst))