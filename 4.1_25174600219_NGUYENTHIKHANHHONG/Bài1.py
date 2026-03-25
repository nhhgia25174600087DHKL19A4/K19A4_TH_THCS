n = int(input("Nhập n (n > 0): "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))
for i in range(n, n*n + 1):
    print(i, end=" ")