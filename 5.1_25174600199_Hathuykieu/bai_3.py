while True:
    try:
        m = int(input("Nhập m: "))
        n = int(input("Nhập n: "))
        if 0 < m < n:
            break
        else:
            print("Lỗi: phải thỏa mãn 0 < m < n. Nhập lại!\n")
    except ValueError:
        print("Lỗi: vui lòng nhập số nguyên!\n")
danh_sach_so_chan = list(filter(lambda x: x % 2 == 0, range(m, n + 1)))
print("Các số chẵn từ", m, "đến", n, "là:")
print(danh_sach_so_chan)