n = int(input("Nhập n: "))

print("Các số nguyên tố:")
for x in range(2, n + 1):
    la_snt = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            la_snt = False
            break
    if la_snt:
        print(x, end=" ")
print()

print("Các số hoàn hảo:")
for x in range(1, n + 1):
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    if tong == x:
        print(x, end=" ")