n = int(input("Nhập n: "))
z  = []
print("Nhập test_list:")
for i in range(n):
    a = int(input())
    b = int(input())
    z.append((a, b))
y = []
print("Nhập search_tup:")
for i in range(n):
    a = int(input())
    b = int(input())
    y.append((a, b))
for x in y:
    if x in z:
        print(x, "ở vị trí", z.index(x))
    else:
        print(x, "không có")