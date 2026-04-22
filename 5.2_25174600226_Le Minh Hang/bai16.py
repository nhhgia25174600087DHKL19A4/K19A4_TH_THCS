n = int(input("Nhập n: "))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

print("Ma trận đơn vị:")
for row in matrix:
    print(row)