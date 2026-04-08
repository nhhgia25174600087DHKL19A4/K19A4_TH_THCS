n = int(input("Nhap n: "))
A = [0]*n
for i in range(n):
    A[i] = int(input("Nhap phan tu: "))
# a
B = []
for i in range(n):
    if A[i] % 3 == 0 and A[i] % 5 != 0:
        B = B + [A[i]]
print("B =", B)
# b
C = []
for i in range(n):
    C = C + [A[i]*A[i]]
print("C =", C)
# c
D = []
for i in range(n):
    if A[i] % 3 == 0:
        D = D + [A[i]]
if len(D) > 0:
    print("Phan tu chia het cho 3 =", D[0])
else:
    print("Khong co")