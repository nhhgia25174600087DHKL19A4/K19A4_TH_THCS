#a
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

A = []

for i in range(m):
    hang = []
    for j in range(n):
        x = int(input(f"A[{i}][{j}] = "))
        hang.append(x)
    A.append(hang)

print(A)
#b
tong = 0

for i in range(len(A)):
    for j in range(len(A[i])):
        tong += A[i][j]

print("Tổng =", tong)