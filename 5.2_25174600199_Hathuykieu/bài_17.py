m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
A = []
for i in range(m):
    row = []
    for j in range(n):
        x = int(input(f"A[{i}][{j}] = "))
        row.append(x)
    A.append(row)
tong = 0
for i in range(m):
    for j in range(n):
        tong += A[i][j]
print("Ma trận A:")
for row in A:
    print(row)
print("Tổng các phần tử:", tong)