def uoc_so():
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("Số không hợp lệ!")
        return
    print("Các ước số của", n, "là:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
uoc_so()