n = int(input("Nhập số phần tử: "))
m = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    m.append(x)
a = tuple(m)
b = tuple(x for x in a if x % 2 != 0)
print("Tuple ban đầu:", a)
print("Tuple số lẻ:", b)