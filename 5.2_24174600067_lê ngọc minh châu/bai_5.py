A = []
i = 1
while len(A) < 1000:
    if i % 7 != 0:
        A = A + [i]
    i = i + 1
print(A)