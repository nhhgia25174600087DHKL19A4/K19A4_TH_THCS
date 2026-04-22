import random

A = []
for i in range(1000):
    A.append(random.randint(1, 99999))
for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

print("Sắp xếp không dùng sorted():")
print(A)