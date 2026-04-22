A = []

seed = 12345

for i in range(1000):
    seed = (seed * 1103515245 + 12345) % 99999 + 1
    if seed % 7 == 0:
        seed = seed + 1
        if seed > 99999:
            seed = seed - 7

    A.append(seed)

for i in range(20):
    print(A[i], end=" ")