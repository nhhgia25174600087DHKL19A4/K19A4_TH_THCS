X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))
mang_2_chieu = []
for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i * j)
    mang_2_chieu.append(hang)
print("Mảng 2 chiều tạo được là:")
print(mang_2_chieu)