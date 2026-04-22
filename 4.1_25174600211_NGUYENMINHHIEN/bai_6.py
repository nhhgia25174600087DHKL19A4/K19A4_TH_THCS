n = int(input("Nhập số n: "))
la_so_nguyen_to = True
if n < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_so_nguyen_to = False
            break
if la_so_nguyen_to:
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")