def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập số nguyên dương: "))
print(f"{n} là số nguyên tố" if is_prime(n) else f"{n} không là số nguyên tố")