def la_snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(1, 1001):
    if la_snt(i):
        print(i, end=" ")