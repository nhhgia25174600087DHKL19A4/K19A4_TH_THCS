while True:
    n = int(input("Nhập n > 0: "))
    if n > 0:
        break
    print("Nhập lại!")

#a, for
S1 = 0
for i in range(1, n+1):
    S1 += i*i
print("S1 =", S1)

#while
S1 = 0
i = 1
while i <= n:
    S1 += i*i
    i += 1
print("S1 =", S1)