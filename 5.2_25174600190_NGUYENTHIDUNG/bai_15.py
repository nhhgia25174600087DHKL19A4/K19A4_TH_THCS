X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))
mang_2_chieu = [[i * j for j in range(Y)] for i in range(X)]
print("Mảng 2 chiều tạo ra:")
print(mang_2_chieu)