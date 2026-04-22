while True:
    m = int(input("nhap m tu ban phim "))
    n = int(input("nhap n tu ban phim "))
    if 0 < m and m < n:
        break
    print("loi")

danh_sach = []
for i in range(m, n + 1):
    danh_sach += [i]

def is_even(x):
    return x % 2 == 0

filtered_list = list(filter(is_even, danh_sach))
print("so chan la", filtered_list)