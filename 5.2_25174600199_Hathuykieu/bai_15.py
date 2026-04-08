X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))
A = []
for i in range(X):
    A.append([])          
    for j in range(Y):
        A[i].append(i * j)
print(A)