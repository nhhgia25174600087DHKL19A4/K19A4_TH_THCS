n = int(input("Nhập số lượng người: "))
ds = []

for i in range(n):
    ten = input(f"Người {i+1} - Tên: ")
    tuoi = int(input(f"Người {i+1} - Tuổi: "))
    diem = int(input(f"Người {i+1} - Điểm: "))
    ds = ds + [(ten, tuoi, diem)]


for i in range(len(ds)):
    for j in range(len(ds) - 1):
        
        if ds[j] > ds[j+1]:
           
            tam = ds[j]
            ds[j] = ds[j+1]
            ds[j+1] = tam

print("\nDanh sách sau khi sắp xếp:")
for item in ds:
    print(item)