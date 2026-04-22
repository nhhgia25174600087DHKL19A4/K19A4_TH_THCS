n = int(input("Nhập n: "))

print("Số nguyên tố:")
for x in range(2, n + 1):
    la_so_nguyen_to = True
    for i in range(2, x):
        if x % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(x, end=" ")

print("\nSố hoàn hảo:")
for x in range(2, n + 1):
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    if tong == x:
        print(x, end=" ")