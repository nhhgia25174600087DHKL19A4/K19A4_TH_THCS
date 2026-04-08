n = int(input("Nhập số lượng người: "))

danh_sach = []
for i in range(n):
    name = input(f"Nhập tên người thứ {i+1}: ").strip()
    age = int(input(f"Nhập tuổi người thứ {i+1}: "))
    score = float(input(f"Nhập điểm người thứ {i+1}: "))
    danh_sach.append((name, age, score))

print("\nDanh sách ban đầu:")
for t in danh_sach:
    print(t)

danh_sach_sap_xep = sorted(danh_sach, key=lambda x: (x[0], x[1], x[2]))

print("\nDanh sách sau khi sắp xếp (Name > Age > Score):")
for t in danh_sach_sap_xep:
    print(t)