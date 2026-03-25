n = int(input("Nhập n: "))
print(f"Các số nguyên tố từ 1 đến {n}:")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print(f"\nCác số hoàn hảo từ 1 đến {n}:")
for num in range(1, n + 1):
    tong_uoc = 0
    for i in range(1, num):
        if num % i == 0:
            tong_uoc += i
    if tong_uoc == num:
        print(num, end=" ")