n = int(input("Nhập số nguyên dương n: "))
if n > 0:
    print(f"Các số từ {n} đến {n}^2 là:")
    for i in range(n, n**2 + 1):
        print(i, end=" ")
else:
    print("Vui lòng nhập một số nguyên dương.")