import random
n = int(input("Nhập n: "))
A = []
for i in range(n):
    x = random.randint(1, 99999)
    A += [x]
print("Danh sách ban đầu:")
print(A)
#CÁCH 1: DÙNG sorted() 
B = sorted(A)
print("Tăng dần (dùng sorted):")
print(B)
#CÁCH 2 KHÔNG DÙNG sorted 
C = []
for x in A:
    C += [x]
# sắp xếp tăng dần bằng for
for i in range(len(C)):
    for j in range(i+1, len(C)):
        if C[i] > C[j]:
            C[i], C[j] = C[j], C[i]
print("Tăng dần (không dùng sorted):")
print(C)