import random
A = []
for i in range(1000):
    so = random.randint(1, 99999)
    A.append(so)

# CÁCH 1: 
B = sorted(A)
print("Đã sắp xếp xong bằng hàm sorted().")

# CÁCH 2:
B= A[:] 
n = len(B)
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if B[i] > B[j]:
            tam =B[i]
            B[i] =B[j]
            B[j] = tam
print("Đã sắp xếp xong bằng thuật toán tự viết (vòng lặp for).")
print("10 số đầu tiên của Cách 2:", B[:10])