m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

A = []
tong_matran = 0

for i in range(m):
    hang = []
    for j in range(n):
        val = int(input(f"Nhập A[{i}][{j}]: "))
        hang = hang + [val]
        tong_matran = tong_matran + val
    A = A + [hang]

print("Ma trận A:")
for row in A:
    print(row)
print("Tổng các phần tử:", tong_matran)