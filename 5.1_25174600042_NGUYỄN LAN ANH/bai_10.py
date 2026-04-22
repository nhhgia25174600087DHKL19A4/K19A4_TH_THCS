so_phan_tu = int(input("Nhap so luong phan tu: "))

tuple_ban_dau = ()

for i in range(so_phan_tu):
    gia_tri = int(input("Nhap gia tri: "))
    tuple_ban_dau = tuple_ban_dau + (gia_tri,)

print("Tuple ban dau la:", tuple_ban_dau)

tuple_so_le = ()

for phan_tu in tuple_ban_dau:
    if phan_tu % 2 != 0:
        tuple_so_le = tuple_so_le + (phan_tu,)

print("Tuple chua cac so le la:", tuple_so_le)