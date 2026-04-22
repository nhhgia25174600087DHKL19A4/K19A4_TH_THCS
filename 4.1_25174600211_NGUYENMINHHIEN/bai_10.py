n = int(input("Nhập số nguyên dương n: "))
print(f"\nCác số nguyên tố từ 1 đến {n} là:")
for i in range(2, n + 1):
    la_so_nguyen_to = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(i, end=" ")

print(f"\n\nCác số hoàn hảo từ 1 đến {n} là:")
for i in range(1, n + 1):
    tong_uoc = 0
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            tong_uoc += j
    if tong_uoc == i and i != 0:
        print(i, end=" ")