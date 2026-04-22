def in_uoc_so(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()

n = int(input("Nhập n: "))
in_uoc_so(n)