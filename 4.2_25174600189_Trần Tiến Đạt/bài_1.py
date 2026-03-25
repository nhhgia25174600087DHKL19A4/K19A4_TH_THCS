import math

while True:
    n = int(input("Nhập n > 0: "))
    if n > 0:
        break
    else:
        print("Nhập lại!")

# a
S1 = 0
for i in range(1, n+1):
    S1 += i*i

# b
S2 = 0
i = 0
while i <= n:
    x = 2*i + 1
    S2 += x**3
    i += 1

# c
S3 = 0
for i in range(1, n+1):
    S3 += (2*i)**4

# d
S4 = 0
i = 1
while i <= n:
    if i % 2 == 1:
        S4 += 1/i
    else:
        S4 -= 1/i
    i += 1

# e
S5 = 0
for i in range(1, n+1):
    S5 += 1/(i*(i+1))

# f
S6 = 0
i = 2
while i <= n:
    S6 += 1/math.sqrt(i)
    i += 1
    
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)