n = int(input("Nhập n: "))
a = [int(input(f"a[{i}] = ")) for i in range(n)]

# a
print("Tổng các phần tử:", sum(a))

# b
duong = [x for x in a if x > 0]
print("Số lượng số dương:", len(duong))
print("Tổng số dương:", sum(duong))

# c
vi_tri_am = next((i for i, x in enumerate(a) if x < 0), -1)
print("Vị trí âm đầu tiên:", vi_tri_am)

# d
vi_tri_duong = next((i for i in range(len(a)-1, -1, -1) if a[i] > 0), -1)
print("Vị trí dương cuối:", vi_tri_duong)

# e
max_val = max(a)
vi_tri_max = len(a) - 1 - a[::-1].index(max_val)
print("Max:", max_val)
print("Vị trí cuối của max:", vi_tri_max)

t = tuple(a)
print("Tuple:", t)