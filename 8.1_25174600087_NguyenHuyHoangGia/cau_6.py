def tinh_so_ke_tiep(n):
    return n + 1
def tim_va_in_so_ke_tiep():
    so_nhap = int(input("Nhập vào một số nguyên: "))
    so_tiep = tinh_so_ke_tiep(so_nhap)
    print(f"Số kế tiếp của {so_nhap} là: {so_tiep}")
tim_va_in_so_ke_tiep()