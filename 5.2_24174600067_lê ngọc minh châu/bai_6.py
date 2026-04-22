A = []
for i in range(1, 1001):
    A = A + [i]

# -- CACH 1: DUNG SORTED() --
B = sorted(A)
print("Sap xep tang (sorted) =", B)

# --CACH 2: KHONG dung sorted() --
C = []
for i in range(len(A)):
    C = C + [A[i]]

for i in range(len(C)):
    for j in range(len(C)-1):
        if C[j] > C[j+1]:
            C[j], C[j+1] = C[j+1], C[j]
print("Sap xep tang (thu cong) =", C)