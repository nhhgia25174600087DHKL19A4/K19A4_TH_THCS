a = [0] * 1000
k = 0
i = 1

while k < 1000:
    if i % 7 != 0:
        a[k] = i
        k = k + 1
    i = i + 1

for i in range(1000):
    print(a[i], end=" ")


