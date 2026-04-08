X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))

matrix = []
for i in range(X):
    hang = []
    for j in range(Y):
        hang = hang + [i * j]
    matrix = matrix + [hang]

for row in matrix:
    print(row)