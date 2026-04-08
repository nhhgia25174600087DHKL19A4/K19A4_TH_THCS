input_mat_khau = input("Nhập các mật khẩu, cách nhau bằng dấu phẩy: ")
danh_sach_mat_khau = [mk.strip() for mk in input_mat_khau.split(",")] 
#kiểm tra mật khẩu
def kiem_tra_mat_khau(mat_khau):
    if not (6 <= len(mat_khau) <= 12):
        return False
    co_chu_thuong = any(c.islower() for c in mat_khau)
    co_chu_hoa = any(c.isupper() for c in mat_khau)
    co_so = any(c.isdigit() for c in mat_khau)
    co_ky_tu_dac_biet = any(c in "S#@" for c in mat_khau)
    return co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet

mat_khau_hop_le = [mk for mk in danh_sach_mat_khau if kiem_tra_mat_khau(mk)]
print("Mật khẩu hợp lệ:", ", ".join(mat_khau_hop_le))