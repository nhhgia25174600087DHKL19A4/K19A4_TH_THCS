
n = int(input("Nhập số phần tử: "))
A = []

for i in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = int(input("Nhập điểm: "))
    A.append((name, age, score))

for i in range(n - 1):
    for j in range(i + 1, n):

        if (A[i][0] > A[j][0]) or \
           (A[i][0] == A[j][0] and A[i][1] > A[j][1]) or \
           (A[i][0] == A[j][0] and A[i][1] == A[j][1] and A[i][2] > A[j][2]):
            
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

print("Danh sách sau khi sắp xếp:")
for i in range(n):
    print(A[i])