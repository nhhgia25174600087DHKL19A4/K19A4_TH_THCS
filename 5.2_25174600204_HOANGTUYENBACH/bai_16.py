
n = int(input("Nhập n: "))

A = []

for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    A.append(row)

for i in range(n):
    print(A[i])