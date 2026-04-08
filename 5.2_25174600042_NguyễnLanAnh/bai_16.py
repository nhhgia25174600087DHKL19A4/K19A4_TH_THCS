n = int(input())

A = []

for i in range(n):
    dong = []
    for j in range(n):
        if i == j:
            dong.append(1)
        else:
            dong.append(0)
    A.append(dong)

for i in range(n):
    print(A[i])