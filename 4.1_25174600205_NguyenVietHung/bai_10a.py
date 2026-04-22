n = int(input())
for x in range(2, n+1):
    kt = True
    for i in range(2, x):
        if x % i == 0:
            kt = False
            break
    print(x * kt, end=" ")