def dao_nguoc_danh_sach():
    print("=== BÀI 4 ===")
    chuoi_nhap = input("Nhập các phần tử (cách nhau bằng dấu cách): ")
    ds_ban_dau = chuoi_nhap.split()
    
    ds_dao_nguoc = []
    for i in range(len(ds_ban_dau) - 1, -1, -1):
        ds_dao_nguoc.append(ds_ban_dau[i])
        
    print("Danh sách ban đầu:", ds_ban_dau)
    print("Danh sách đảo ngược:", ds_dao_nguoc)
    print()
dao_nguoc_danh_sach()