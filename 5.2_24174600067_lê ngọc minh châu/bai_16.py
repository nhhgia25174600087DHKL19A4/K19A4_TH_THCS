n = int(input("Nhap n: "))
A = []
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang = hang + [1]
        else:
            hang = hang + [0]
    A = A + [hang]
print(A)