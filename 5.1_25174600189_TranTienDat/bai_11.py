n = int(input("Nhập n: "))

test_list = []
search_tup = []

print("Nhập test_list:")
for i in range(n):
    a = int(input())
    b = int(input())
    test_list.append((a, b))

print("Nhập search_tup:")
for i in range(n):
    a = int(input())
    b = int(input())
    search_tup.append((a, b))

for t in search_tup:
    found = False
    for i in range(len(test_list)):
        if t == test_list[i]:
            print(t, "ở vị trí", i)
            found = True
            break
    if not found:
        print(t, "không có")