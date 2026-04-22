def in_uoc(n):
    print("Các ước của", n, "là:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập n > 0")
else:
    in_uoc(n)