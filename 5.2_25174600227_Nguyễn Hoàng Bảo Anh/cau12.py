mk = input("Nhập mật khẩu: ")

if 6 <= len(mk) <= 12:
   
    chu_thuong = chu_hoa = so = dac_biet = False
    
    for c in mk:
        if 'a' <= c <= 'z': chu_thuong = True
        if 'A' <= c <= 'Z': chu_hoa = True
        if '0' <= c <= '9': so = True
        if c in "$#@": dac_biet = True 

    if chu_thuong and chu_hoa and so and dac_biet:
        print("Mật khẩu hợp lệ!")
    else:
        print("Mật khẩu thiếu tiêu chí (chữ hoa, số hoặc ký tự đặc biệt).")
else:
    print("Mật khẩu sai độ dài (phải từ 6-12 ký tự).")