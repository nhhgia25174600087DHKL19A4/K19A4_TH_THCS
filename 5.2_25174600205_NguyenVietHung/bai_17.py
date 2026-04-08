m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        A[i][j] = int(input(f"A[{i}][{j}] = "))

print("Ma trận A:")
for i in range(m):
    row_tuple = tuple(A[i])
    print(row_tuple)

tong = 0
for i in range(m):
    for j in range(n):
        tong += A[i][j]

print("Tổng các phần tử:", tong)