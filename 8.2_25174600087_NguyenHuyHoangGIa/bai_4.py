def dao_nguoc_danh_sach(ds):
    ds_dao_nguoc = []
    do_dai = 0
    for _ in ds:
        do_dai += 1
    for i in range(do_dai - 1, -1, -1):
        ds_dao_nguoc.append(ds[i])
    return ds_dao_nguoc
if __name__ == "__main__":
    nhap = input("Nhập danh sách: ")
    danh_sach_ban_dau = nhap.split() 
    print("Danh sách ban đầu:", danh_sach_ban_dau)
    print("Danh sách đảo ngược:", dao_nguoc_danh_sach(danh_sach_ban_dau))