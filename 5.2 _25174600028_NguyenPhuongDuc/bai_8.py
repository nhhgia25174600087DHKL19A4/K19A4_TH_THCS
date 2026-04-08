n = int(input("Nhập n cho Fibonacci: "))
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n - 1)]
print(", ".join(map(str, fib[:n+1])))