def in_fibonacci():
    n = int(input("Nhập số lượng số Fibonacci (<=20): "))
    if n <= 0:
        return
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

in_fibonacci()