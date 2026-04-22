import random

n = int(input("Nhap n: "))
A = [int(input("Nhap phan tu: ")) for _ in range(n)]

B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print(B)

C = [x**2 for x in A]
print(C)

D = [random.choice([x for x in A if x % 3 == 0]) for _ in range(len(A)) if any(y % 3 == 0 for y in A)]
print(D)