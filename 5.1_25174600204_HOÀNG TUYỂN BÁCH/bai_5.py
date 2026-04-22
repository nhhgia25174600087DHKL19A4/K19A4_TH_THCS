n = int(input("Nhập n: "))

a = []
for i in range(1, n + 1):
    a.append(i)

primes = []
perfects = []

for x in a:
    if x >= 2:
        isPrime = True
        for i in range(2, x):
            if x % i == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(x)
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    if tong == x:
        perfects.append(x)
print("Số nguyên tố:", primes)
print("Số hoàn hảo:", perfects)