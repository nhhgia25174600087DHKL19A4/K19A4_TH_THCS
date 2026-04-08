#C1
A = [(i * 23 + 7) % 99999 + 1 for i in range(1000)]
B = sorted(A)
print(B)
#C2
A = [(i * 23 + 7) % 99999 + 1 for i in range(1000)]

for i in range(len(A)):
    for j in range(len(A) - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

print(A)