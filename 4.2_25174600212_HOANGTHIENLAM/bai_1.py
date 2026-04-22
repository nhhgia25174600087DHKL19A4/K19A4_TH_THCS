
while True:
    n = int(input("Nhập n (n > 0): "))
    if n > 0:
        break
    print("Sai! Nhập lại.")
S1 = 0
for i in range(1, n + 1):
    S1 += i * i
S2 = 0
for i in range(0, n + 1):
    x = 2 * i + 1
    S2 += x * x * x
S3 = 0
for i in range(1, n + 1):
    x = 2 * i
    S3 += x * x * x * x
S4 = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        S4 += 1 / i
    else:
        S4 -= 1 / i
S5 = 0
for i in range(1, n + 1):
    S5 += 1 / (i * (i + 1))
def sqrt_newton(x):
    guess = x
    for _ in range(20):  
        guess = (guess + x / guess) / 2
    return guess
S6 = 0
for i in range(2, n + 1):
    S6 += 1 / sqrt_newton(i)
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", round(S4, 4))
print("S5 =", round(S5, 4))
print("S6 =", round(S6, 4))