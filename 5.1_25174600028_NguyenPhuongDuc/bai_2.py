n = int(input("nhap tu ban phim"))
m = int(input("nhap tu ban phim "))
lst = []
for i in range(1, n + 1):
    lst = lst + [i * i]
if m >= n:
    print("danh sach rong ", [])
else:
    res = []
    for i in range(m, n):
        res = res + [lst[i]]
    print(f"danh sach bo m :", res)