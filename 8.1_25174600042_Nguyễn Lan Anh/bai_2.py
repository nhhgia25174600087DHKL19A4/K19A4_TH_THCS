def fibonacci(n):
    a = 0
    b = 1
    dem = 0
    while dem < n:
        print(a, end=" ")
        a = b
        b = a + b
        dem = dem + 1
n = int(input("Nhập số phần tử nhỏ hơn hoặc bằng 20: "))
if n > 20:
    n = 20
fibonacci(n)