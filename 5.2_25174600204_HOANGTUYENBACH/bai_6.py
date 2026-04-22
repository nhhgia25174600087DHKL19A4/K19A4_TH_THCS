
A = []
seed = 12345

for i in range(1000):
    seed = (seed * 1103515245 + 12345) % 99999 + 1
    A.append(seed)

A_sorted = sorted(A)
print("20 phần tử đầu (sorted):")
for i in range(20):
    print(A_sorted[i], end=" ")

print()

B = []
for i in range(1000):
    B.append(A[i])
for i in range(999):
    for j in range(i + 1, 1000):
        if B[i] > B[j]:
            temp = B[i]
            B[i] = B[j]
            B[j] = temp

print("\n20 phần tử đầu (tự sắp xếp):")
for i in range(20):
    print(B[i], end=" ")