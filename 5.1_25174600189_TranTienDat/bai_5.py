n = int(input("Nhập n: "))

lst = []
for i in range(1, n+1):
    lst.append(i)

# danh sách chứa số nguyên tố
so_nguyen_to = []
for x in lst:
    if x < 2:
        continue
    check = True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            check = False
            break
    if check:
        so_nguyen_to.append(x)

# danh sách chứa số hoàn hảo
so_hoan_hao = []
for x in lst:
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    if s == x:
        so_hoan_hao.append(x)

print("Nguyên tố:", so_nguyen_to)
print("Hoàn hảo:", so_hoan_hao)