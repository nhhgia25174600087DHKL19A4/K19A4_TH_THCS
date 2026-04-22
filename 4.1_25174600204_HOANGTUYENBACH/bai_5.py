n = int(input("Nhập số nguyên: "))
sign = -1 if n < 0 else 1
n = abs(n)
reverse = 0
for i in range(len(str(n))):
    reverse = reverse * 10 + (n % 10)
    n = n // 10
print("Số đảo ngược là:", sign * reverse)