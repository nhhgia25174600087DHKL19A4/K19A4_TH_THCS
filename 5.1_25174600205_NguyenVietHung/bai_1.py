n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
lst = [0] * n
for i in range(n):
    lst[i] = (i + 1) * (i + 1)
if m >= n:
    for i in range(n):
        print(lst[i], end=" ")
else:
    for i in range(m):
        print(lst[i], end=" ")