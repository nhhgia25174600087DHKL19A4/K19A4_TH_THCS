
X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))

A = []


for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    A.append(row)

for i in range(X):
    print(A[i])