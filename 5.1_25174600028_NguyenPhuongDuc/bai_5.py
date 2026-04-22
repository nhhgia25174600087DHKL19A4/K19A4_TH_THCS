n = int(input("nhap so n "))
so_nguyen_to = []
so_hoan_hao = []
for i in range(1, n + 1):
    if i > 1:
        is_prime = True
        for j in range(2, i):
            if j * j > i:
                break
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            so_nguyen_to += [i]
    if i > 1:
        div_sum = 0
        for j in range(1, i):
            if i % j == 0:
                div_sum += j
        if div_sum == i:
            so_hoan_hao += [i]
print("so nguyen to:", so_nguyen_to)
print("so hoan hao", so_hoan_hao)