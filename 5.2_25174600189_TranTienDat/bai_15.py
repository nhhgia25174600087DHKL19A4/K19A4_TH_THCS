X = int(input())
Y = int(input())

a = []
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i*j)
    a.append(row)

print(a)