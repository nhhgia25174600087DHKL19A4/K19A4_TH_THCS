n = int(input("Nhập n: "))
for num in range(1, n + 1):
    tong = 0
    for i in range(1, num):
        if num % i == 0:
            tong += i
    if tong == num:
        print(num, end=" ")        