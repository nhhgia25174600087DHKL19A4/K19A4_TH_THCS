# a
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

A = []

for i in range(m):
    row = []
    for j in range(n):
        x = int(input(f"Nhập A[{i}][{j}]: "))
        row.append(x)
    A.append(row)


print("Ma trận A:")
for i in range(m):
    print(A[i])
# b
tong = 0

for i in range(m):
    for j in range(n):
        tong = tong + A[i][j]

print("Tổng các phần tử:", tong)