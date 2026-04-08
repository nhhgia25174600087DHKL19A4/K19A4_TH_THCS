n = int(input("Nhập n: "))
A = []
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
    A.append(hang)
for hang in A:
    print(hang)