X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))
matrix = [[0] * Y for _ in range(X)]
for i in range(X):
    for j in range(Y):
        matrix[i][j] = i * j
print("Ma trận:")
for i in range(X):
    row_tuple = tuple(matrix[i]) 
    print(row_tuple)