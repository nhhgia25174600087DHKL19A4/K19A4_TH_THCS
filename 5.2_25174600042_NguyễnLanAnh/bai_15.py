X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))

A = []

for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i * j)
    A.append(hang)

print(A)