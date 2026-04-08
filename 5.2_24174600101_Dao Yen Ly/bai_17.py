m = int(input("nhap so hang: "))
n = int(input("nhap so cot: "))

# a. nhap ma tran
A = []

for i in range(m):
    hang = list(map(int, input("nhap hang: ").split()))
    A.append(hang)

# b. tinh tong
tong = 0

for i in range(m):
    for j in range(n):
        tong = tong + A[i][j]

print("tong ma tran:", tong)