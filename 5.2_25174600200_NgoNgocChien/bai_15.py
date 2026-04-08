X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))
a = []
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    a.append(row)
print("Ma trận:")
for i in a:
    print(i)