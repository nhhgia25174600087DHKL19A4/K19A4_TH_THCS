m = int(input())
n = int(input())

A = []

for i in range(m):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    A.append(row)

# tổng
tong = 0
for row in A:
    for x in row:
        tong += x

print("Tổng:", tong)