n = int(input("Nhập số nguyên dương n: "))

if n > 0:
    for i in range(n, n**2 + 1):
        print(i, end=" ")