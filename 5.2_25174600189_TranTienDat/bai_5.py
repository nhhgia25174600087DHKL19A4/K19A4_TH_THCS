a = []
i = 1
while len(a) < 1000:
    if i % 7 != 0:
        a.append(i)
    i += 1

print(len(a))