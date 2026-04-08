X, Y = map(int, input("Nhập X và Y cách nhau bởi dấu cách: ").split())
matrix_15 = [[i * j for j in range(Y)] for i in range(X)]
print("bai 15", matrix_15)