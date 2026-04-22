n = int(input("Nhập số phần tử: "))
lst = []

for i in range(n):
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    score = int(input("Điểm: "))
    lst.append((name, age, score))

# sắp xếp: name -> age -> score
lst.sort()

print("Kết quả:")
for item in lst:
    print(item)