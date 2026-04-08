n = int(input("Nhập n: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
s = ""
for i in range(n):
    s += str(fib[i])
    if i != n - 1:
        s += ","
print(s)