while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))

    if 0 < m < n:
        break
    else:
        print("Lỗi, nhập lại!")
size = n - m + 1
lst = [0] * size
for i in range(size):
    lst[i] = m + i
even_lst = [0] * size
count = 0
for i in range(size):
    if lst[i] % 2 == 0:
        even_lst[count] = lst[i]
        count += 1
print("Số chẵn:")
for i in range(count):
    print(even_lst[i], end=" ")