n = 2
while n <= 1000:
    kt = True
    i = 2
    while i < n:
        if n % i == 0:
            kt = False
            break
        i = i + 1
    if kt == True:
        print(n, end=" ")
    n = n + 1