# nhập n
while True:
    n = int(input("Nhập n (>0): "))
    if n > 0:
        break
# a. S1
S1 = 0
i = 1
while i <= n:
    S1 = S1 + i * i
    i = i + 1
# b. S2
S2 = 0
i = 0
while i <= n:
    x = 2 * i + 1
    S2 = S2 + x * x * x
    i = i + 1
# c. S3
S3 = 0
i = 1
while i <= n:
    x = 2 * i
    S3 = S3 + x**4
    i = i + 1
# d. S4
S4 = 0
i = 1
while i <= n:
    if i % 2 == 0:
        S4 -= 1 / i
    else:
        S4 += 1 / i
    i += 1
# e. S5
S5 = 0
i = 1
while i <= n:
    S5 += 1 / (i * (i + 1))
    i += 1
# f. S6
S6 = 0
i = 2
while i <= n:
    S6 += 1 / (i ** 0.5)
    i += 1
print(S1, S2, S3, round(S4,2), round(S5,2), round(S6,2))