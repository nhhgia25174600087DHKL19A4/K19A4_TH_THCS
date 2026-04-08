a = []
for i in range(1,1001):
    x = (i * 53) % 99999 + 1
    a.append(x)
print("Danh sách ban đầu:")
print(a)
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print("Danh sách sau khi sắp xếp:")
print(a)