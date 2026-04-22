m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
A = []
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input("Nhap phan tu: "))
        hang = hang + [x]
    A = A + [hang]
tong = 0
for i in range(m):
    for j in range(n):
        tong = tong + A[i][j]
print("Tong =", tong)