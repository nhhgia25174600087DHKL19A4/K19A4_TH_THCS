n = int(input("Nhap n: "))

fibo = [0, 1]

[fibo.append(fibo[i-1] + fibo[i-2]) for i in range(2, n)]

print(", ".join(str(x) for x in fibo[:n]))