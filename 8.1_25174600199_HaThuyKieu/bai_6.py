def chuan_hoa(s):
    return " ".join(s.strip().split()).title()
def sap_xep(s):
    return " ".join(sorted(s.split()))
s = input("Nhập chuỗi: ")
s = chuan_hoa(s)
print("Chuỗi chuẩn hóa:", s)
print("Chuỗi sau khi sắp xếp:", sap_xep(s))