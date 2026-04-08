X = int(input("Nhap X: "))
Y = int(input("Nhap Y: "))
A = []
for i in range(X):
    hang = []
    for j in range(Y):
        hang = hang + [i*j]
    A = A + [hang]
print(A)