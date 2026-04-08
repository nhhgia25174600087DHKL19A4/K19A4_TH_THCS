a = []
i = 1
while len(a) < 1000:
    x = (i * 37) % 99999 + 1
    if x % 7 != 0:
        a.append(x)
    i = i + 1
print("Day A:")
print(a)