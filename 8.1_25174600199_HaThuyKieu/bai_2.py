def fibonacci():
    a, b = 0, 1
    dem = 0
    while dem < 20:
        print(a, end=" ")
        a, b = b, a + b
        dem += 1
fibonacci()