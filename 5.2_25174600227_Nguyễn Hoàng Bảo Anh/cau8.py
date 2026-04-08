n = int(input("Nhập n: "))
fib = [0, 1]

for i in range(2, n + 1):
    fib = fib + [fib[i-1] + fib[i-2]]

res = [str(x) for x in fib[:n+1]]
print(", ".join(res))