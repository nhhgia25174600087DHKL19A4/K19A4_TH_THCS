def dao_nguoc_danh_sach():
    chuoi_nhap = input("Nhập các phần tử của danh sách: ")
    danh_sach = chuoi_nhap.split()
    
    danh_sach_dao = []
    for i in range(len(danh_sach) - 1, -1, -1):
        danh_sach_dao.append(danh_sach[i])
        
    print("Danh sách sau khi đảo ngược:", danh_sach_dao)

dao_nguoc_danh_sach()