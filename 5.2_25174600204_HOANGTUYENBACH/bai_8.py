n = int(input("Nhập n: "))

fib = [0, 1]

for i in range(2, n + 1):
    fib.append(fib[i-1] + fib[i-2])

kq = [str(fib[i]) for i in range(n + 1)]

print(", ".join(kq))