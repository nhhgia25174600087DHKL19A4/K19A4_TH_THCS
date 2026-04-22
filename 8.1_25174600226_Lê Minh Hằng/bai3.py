def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập n: "))
if so_nguyen_to(n):
    print("Là số nguyên tố")
else:
    print("Không phải số nguyên tố")
def so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
n = int(input("Nhập n: "))
if so_hoan_hao(n):
    print("Là số hoàn hảo")
else:
    print("Không phải số hoàn hảo")
