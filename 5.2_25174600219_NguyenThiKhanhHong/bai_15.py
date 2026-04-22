X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))
mang_2d = [[i * j for j in range(Y)] for i in range(X)]
print("Mảng 2 chiều tạo ra:")
for hang in mang_2d:
    print(hang)