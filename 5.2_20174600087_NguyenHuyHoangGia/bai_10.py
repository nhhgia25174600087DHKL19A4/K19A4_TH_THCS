danh_sach_thoa_man = []
for i in range(201):
    if i % 5 == 0 and i % 7 == 0:
        danh_sach_thoa_man.append(i)
so_ngau_nhien_ao = id(danh_sach_thoa_man)
vi_tri = so_ngau_nhien_ao % len(danh_sach_thoa_man)
ket_qua = danh_sach_thoa_man[vi_tri]
print("Các số thỏa mãn điều kiện là:", danh_sach_thoa_man)
print("Số được chọn ngẫu nhiên là:", ket_qua)