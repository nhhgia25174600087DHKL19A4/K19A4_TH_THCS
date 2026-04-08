n = int(input("Nhập n: "))
ds = []
for i in range(n):
    s = input(f"Nhập phần tử {i+1}: ")
    ten, tuoi, diem = s.split()
    ds.append([ten, int(tuoi), int(diem)])
for i in range(n):
    for j in range(i + 1, n):
        if (ds[i][0] > ds[j][0] or
           (ds[i][0] == ds[j][0] and ds[i][1] > ds[j][1]) or
           (ds[i][0] == ds[j][0] and ds[i][1] == ds[j][1] and ds[i][2] > ds[j][2])):
            ds[i], ds[j] = ds[j], ds[i]
print("Kết quả sau khi sắp xếp:")
print(ds)