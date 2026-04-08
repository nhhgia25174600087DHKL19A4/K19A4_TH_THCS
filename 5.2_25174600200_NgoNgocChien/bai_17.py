m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = []
for i in range(m):
    row = []
    for j in range(n):
        x = int(input("Nhập phần tử a[" + str(i) + "][" + str(j) + "]: "))
        row.append(x)
    A.append(row)
print("Ma trận A:")
for i in A:
    print(i)
tong = 0
for i in range(m):
    for j in range(n):
        tong += A[i][j]
print("Tổng các phần tử:", tong)