while True:
    m = int(input("nhap m tu ban phim "))
    n = int(input("nhap n tu ban phim "))
    if 0 < m and m < n:
        break
    print("loi")

lst100 = []
count = 0
curr = m
while curr <= n and count < 100:
    lst100 += [curr]
    curr += 2
    count += 1
total = 0
for x in lst100:
    total += x

print("danh sach tao ra", lst100)
print("tong danh sach", total)