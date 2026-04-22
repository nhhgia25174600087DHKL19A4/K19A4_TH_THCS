# tao list rong san
a = [0] * 50
k = 0

# tim cac so chia het cho 5 va 7
for i in range(201):
    if i % 5 == 0 and i % 7 == 0:
        a[k] = i
        k = k + 1

# in cac phan tu trong list
print("cac so tim duoc la:")
for i in range(k):
    print(a[i], end=" ")
    