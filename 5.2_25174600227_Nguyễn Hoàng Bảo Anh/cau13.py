chuoi_vao = input("Nhập các mật khẩu: ")
danh_sach_pass = chuoi_vao.split(",")
ket_qua = []

for p in danh_sach_pass:
    p = p.strip() 
   
    if 6 <= len(p) <= 12:
        chu_thuong = chu_hoa = so = dac_biet = False
        
        for char in p:
            if 'a' <= char <= 'z': chu_thuong = True
            elif 'A' <= char <= 'Z': chu_hoa = True
            elif '0' <= char <= '9': so = True
            elif char in "$#@": dac_biet = True
        
        if chu_thuong and chu_hoa and so and dac_biet:
            ket_qua = ket_qua + [p]


print(",".join(ket_qua))