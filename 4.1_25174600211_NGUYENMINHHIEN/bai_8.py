print("Các số nguyên tố từ 1 đến 1000:")
for n in range(2, 1001):
    la_so_nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(n, end=" ")