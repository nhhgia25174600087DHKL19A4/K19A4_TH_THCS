n = int(input("Nhap n: "))
a = list(map(int, input("Nhap list: ").split()))

# a. tim so lon thu 2
max1 = max(a)
max2 = None

for x in a:
    if x != max1:
        if max2 == None or x > max2:
            max2 = x

print("So lon thu 2:", max2)

# b. day duong lien tiep dai nhat
dem = 0
max_dem = 0

for x in a:
    if x > 0:
        dem = dem + 1
        if dem > max_dem:
            max_dem = dem
    else:
        dem = 0

print("Do dai duong max:", max_dem)

# c. day duong co tong lon nhat
tong = 0
max_tong = 0

for x in a:
    if x > 0:
        tong = tong + x
        if tong > max_tong:
            max_tong = tong
    else:
        tong = 0

print("Tong duong max:", max_tong)