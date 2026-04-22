n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương")
else:
    i = n
    while i <= n * n:
        print(i, end=" ")
        i += 1