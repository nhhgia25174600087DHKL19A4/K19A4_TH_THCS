def is_perfect(n):
    if n <= 1:
        return False
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

n = int(input("Nhập số cần kiểm tra: "))
print(f"{n} là số hoàn hảo" if is_perfect(n) else f"{n} không là số hoàn hảo")