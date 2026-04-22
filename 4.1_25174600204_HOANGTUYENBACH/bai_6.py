n = int(input("Nhập số nguyên n: "))
if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")