n = int(input("Nhập số lượng phần tử: "))
A = []
i = 1
while len(A) < n:
    if i % 7 != 0:
        A.append(i)
    i = i + 1

print(A)