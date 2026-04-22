n = int(input("Nhập số lượng người: "))
students = []
for _ in range(n):
    inp = input("Nhập name, age, score cách nhau bởi dấu phẩy: ").split(',')
    name = inp[0].strip()
    age = int(inp[1].strip())
    score = float(inp[2].strip())
    students.append((name, age, score))
students.sort(key=lambda x: (x[0], x[1], x[2]))
print("Danh sách sau khi sắp xếp:", students)