def in_fibonacci():
    a = 0
    b = 1
    dem = 0

    while dem < 20:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        dem = dem + 1

in_fibonacci()