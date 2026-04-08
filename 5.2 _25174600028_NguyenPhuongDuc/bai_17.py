m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"Nhập a[{i+1}][{j+1}]: ")))
    A.append(row)
total_sum = 0
for row in A:
    for val in row:
        total_sum += val
print(f"Tổng các phần tử của ma trận A là: {total_sum}")