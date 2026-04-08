import random

A = []

for i in range(1000):
    A.append(random.randint(1, 99999))

B = sorted(A)
print(B)

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            t = A[i]
            A[i] = A[j]
            A[j] = t

print(A)
