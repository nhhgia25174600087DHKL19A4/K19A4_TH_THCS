n = int(input("Nhập số phần tử: "))

ds = []

for i in range(n):
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    score = int(input("Điểm: "))
    ds.append((name, age, score))

for i in range(len(ds)):
    for j in range(i + 1, len(ds)):
        if ds[i][0] > ds[j][0] or \
           (ds[i][0] == ds[j][0] and ds[i][1] > ds[j][1]) or 3(ds[i][0] == ds[j][0] and ds[i][1] == ds[j][1] and ds[i][2] > ds[j][2]):
            ds[i], ds[j] = ds[j], ds[i]

print(ds)