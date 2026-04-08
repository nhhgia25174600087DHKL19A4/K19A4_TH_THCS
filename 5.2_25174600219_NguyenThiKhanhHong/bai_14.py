n = int(input("Nhập số người: "))
danh_sach = []
for _ in range(n):
    t = input("Nhập Tên: ")
    u = int(input("Nhập Tuổi: "))
    d = int(input("Nhập Điểm: "))
    danh_sach.append((t, u, d))
danh_sach.sort()
print("Kết quả:", danh_sach)