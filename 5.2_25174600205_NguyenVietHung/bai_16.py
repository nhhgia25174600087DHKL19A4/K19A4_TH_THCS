n = int(input("Nhập n: "))
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = 1
print("Ma trận đơn vị:")
for i in range(n):
    row_tuple = tuple(matrix[i])
    print(row_tuple)