for n in range(2, 1001):
    kt = True
    for i in range(2, n):
        if n % i == 0:
            kt = False
            break
    print(n * kt, end=" ")