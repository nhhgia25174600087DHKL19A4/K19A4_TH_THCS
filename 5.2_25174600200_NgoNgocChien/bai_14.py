n = int(input("Nhập số lượng: "))
a = []
for i in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm: "))
    a.append((name, age, score))
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i][0] > a[j][0] or \
           (a[i][0] == a[j][0] and a[i][1] > a[j][1]) or \
           (a[i][0] == a[j][0] and a[i][1] == a[j][1] and a[i][2] > a[j][2]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("Danh sách sau khi sắp xếp:")
for i in a:
    print(i)