n = int(input("Nhập n: "))
so_nguyen_to = []

for x in range(1, n + 1):
    if x < 2:
        continue
    
    dem = 0
    for i in range(1, x + 1):
        if x % i == 0:
            dem += 1
    
    if dem == 2:
        so_nguyen_to.append(x)
so_hoan_hao = []

for x in range(1, n + 1):
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    
    if tong == x:
        so_hoan_hao.append(x)
print("Số nguyên tố:", so_nguyen_to)
print("Số hoàn hảo:", so_hoan_hao)