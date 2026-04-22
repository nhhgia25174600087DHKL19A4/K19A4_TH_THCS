import math
while True:
    n = int(input("Nhập n (>0): "))
    if n > 0:
        break
S1 = S2 = S3 = 0
S4 = S5 = S6 = 0.0
for i in range(1, n + 1):
    # a. S1
    S1 += i**2
    # b. S2 (số lẻ)
    S2 += (2*i - 1)**3
    # c. S3 (số chẵn)
    S3 += (2*i)**4
    # d. S4 (đổi dấu)
    if i % 2 == 1:
        S4 += 1/i
    else:
        S4 -= 1/i
    # e. S5
    S5 += 1/(i*(i+1))
    # f. S6
    if i >= 2:
        S6 += 1/math.sqrt(i)
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)