print("Các số nguyên tố từ 1 đến 1000:")
for n in range(2, 1001):
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")