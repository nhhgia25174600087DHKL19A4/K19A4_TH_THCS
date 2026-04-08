so = 987654321
A = []
for i in range(1000):
    so = (1103515245 * so + 12345) % (2**31)
    A.append((so % 99999) + 1)
A_cach1 = sorted(A)
A_cach2 = A[:]
n = len(A_cach2)
for i in range(n):
    for j in range(0, n - i - 1):
        if A_cach2[j] > A_cach2[j+1]:
            A_cach2[j], A_cach2[j+1] = A_cach2[j+1], A_cach2[j]
print("Cách 1 ", A_cach1[:5])
print("Cách 2 ", A_cach2[:5])