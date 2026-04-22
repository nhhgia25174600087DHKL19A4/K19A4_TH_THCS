n = int(input("Nhap n: "))
print("Cac uoc la:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")