n = int(input("nhap tu ban phim "))
m = int(input("nhap tu ban phim "))
binh_phuong = [i**2 for i in range(1, n + 1)]

if m >= n:
    print("list ket qua", binh_phuong)
