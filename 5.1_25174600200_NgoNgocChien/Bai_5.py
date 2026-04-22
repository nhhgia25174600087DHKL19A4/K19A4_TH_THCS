n = int(input("Nhập n: "))
a = []
for i in range(1, n + 1):
    a.append(i)
nguyen_to = []
hoan_hao = []
for x in a:
    dem = 0
    for i in range(1, x + 1):
        if x % i == 0:
            dem += 1
    if dem == 2:
        nguyen_to.append(x)
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    if tong == x:
        hoan_hao.append(x)
print("Số nguyên tố:", nguyen_to)
print("Số hoàn hảo:", hoan_hao)                    
                