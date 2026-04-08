seed = 987654321 
A = []
while len(A) < 1000:
    seed = (1103515245 * seed + 12345) % (2**31)
    so_ngau_nhien = (seed % 99999) + 1
    if so_ngau_nhien % 7 != 0:
        A.append(so_ngau_nhien)
n = len(A)
for i in range(n - 1):
    for j in range(i + 1, n):
        if A[i] > A[j]:
            tam = A[i]
            A[i] = A[j]
            A[j] = tam
print("Đã tự sinh và sắp xếp xong 1000 số không dùng thư viện!")
print("10 số nhỏ nhất sau khi xếp là:", A[:10])
print("10 số lớn nhất sau khi xếp là:", A[-10:])