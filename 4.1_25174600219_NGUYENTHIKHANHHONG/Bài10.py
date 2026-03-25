n = int(input("Nhập n: "))
for x in range(2, n + 1):
    m = 0
    for i in range(1, x + 1):
        if x % i == 0:
            m += 1
    if m == 2:
        print(x, end=" ")