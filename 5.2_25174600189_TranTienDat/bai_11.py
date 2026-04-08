import random

n = int(input())
A = [int(input()) for _ in range(n)]

B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print(B)

C = [x*x for x in A]
print(C)

D = [x for x in A if x % 3 == 0]
if len(D) > 0:
    print(random.choice(D))