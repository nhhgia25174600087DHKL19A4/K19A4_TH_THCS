for n in range(2, 1001):
    la_so_nguyen_to = True
    for i in range(2, n):
        if n % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(n, end=" ")    