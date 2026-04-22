n = int(input("Nhập số phần tử: "))
data = [0] * n

for i in range(n):
    name = input("Name: ")
    age = int(input("Age: "))
    score = float(input("Score: "))
    
    
    t = (name, age, score)
    data[i] = t


for i in range(n):
    for j in range(n - 1):
        a = data[j]
        b = data[j + 1]

        
        if a[0] > b[0]:
            data[j], data[j + 1] = data[j + 1], data[j]

        elif a[0] == b[0]:
            if a[1] > b[1]:
                data[j], data[j + 1] = data[j + 1], data[j]

            elif a[1] == b[1]:
                if a[2] > b[2]:
                    data[j], data[j + 1] = data[j + 1], data[j]


print("Sau khi sắp xếp:")
for i in range(n):
    print(data[i])