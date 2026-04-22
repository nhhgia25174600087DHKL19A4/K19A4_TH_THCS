n = int(input("Nhập số phần tử: "))
A = []
i = 1
while len(A) < n:
    A.append((i * 3 + 7) % 99999 + 1)
    i = i + 1
print("Danh sách ban đầu:", A)

B = sorted(A)
print("Sorted:", B)
C = A.copy()
for i in range(len(C)):
    for j in range(len(C)):
        if C[i] < C[j]:
            C[i], C[j] = C[j], C[i]

print("Không dùng sorted:", C)