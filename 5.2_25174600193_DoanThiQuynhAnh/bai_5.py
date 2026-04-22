import random

A = []

while len(A) < 1000:
    x = random.randint(1, 99999)
    if x % 7 != 0:
        A.append(x)

print(A)
