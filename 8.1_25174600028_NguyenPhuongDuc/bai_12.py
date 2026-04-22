def nhap_nhan_vien():
    ten = input("Nhập họ tên NV: ")
    que = input("Nhập quê quán: ")
    tham_nien = int(input("Thâm niên công tác (năm): "))
    return {"ten": ten, "que": que, "tham_nien": tham_nien}

def tinh_luong_nv(tham_nien):
    # Giả định: lương cơ bản 5.000.000, mỗi năm thâm niên cộng thêm 500.000
    luong_co_ban = 5000000
    phu_cap_tham_nien = tham_nien * 500000
    return luong_co_ban + phu_cap_tham_nien

def xuat_nhan_vien(nv):
    luong = tinh_luong_nv(nv['tham_nien'])
    print("-" * 30)
    print(f"Họ tên:     {nv['ten']}")
    print(f"Quê quán:   {nv['que']}")
    print(f"Thâm niên:  {nv['tham_nien']} năm")
    print(f"Tổng lương: {luong:,.0f} VND")
