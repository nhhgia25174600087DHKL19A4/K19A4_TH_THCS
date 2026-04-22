n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
lst = [i**2 for i in range(1, n + 1)]
if m >= n:
    print(lst)
else:
    print(lst[:m])