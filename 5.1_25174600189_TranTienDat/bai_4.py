m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

lst = []
for i in range(m, n+1, 2):
    lst.append(i)

lst = lst[:100]

tong = 0
for i in lst:
    tong += i

print(lst)
print("Tổng:", tong)