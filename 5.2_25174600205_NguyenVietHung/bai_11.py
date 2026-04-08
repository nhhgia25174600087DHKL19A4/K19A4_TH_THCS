n = int(input("Nhập số phần tử n: "))
A = [0]*n
for i in range(n):
    A[i] = int(input("Nhập phần tử thứ " + str(i) + ": "))

# a
B = [x for x in A if (x % 3 == 0 and x % 5 != 0)]
print("Danh sách B (chia hết 3, không chia hết 5):", B)

# b
C = [x*x for x in A]
print("Danh sách C (bình phương các phần tử A):", C)

# c
D = [A[i] for i in range(0, n, 2) if A[i] % 3 == 0] 
print("Danh sách D (các phần tử vị trí chẵn chia hết 3):", D)


tB = tuple(B)
tC = tuple(C)
tD = tuple(D)
print("Tuple B:", tB)
print("Tuple C:", tC)
print("Tuple D:", tD)