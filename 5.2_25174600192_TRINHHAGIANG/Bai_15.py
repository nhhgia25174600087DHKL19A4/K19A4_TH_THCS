X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))

mang_2_chieu = [[i * j for j in range(Y)] for i in range(X)]
print("\nMảng 2 chiều (i*j):")
for hang in mang_2_chieu:
    print(hang)