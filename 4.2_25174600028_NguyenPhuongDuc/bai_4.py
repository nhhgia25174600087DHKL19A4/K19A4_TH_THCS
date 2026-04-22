n = input("nhap so ")
ket_qua = ""

for chu_so in n:
    chu = ""
    if chu_so == '0': chu = "không"
    elif chu_so == '1': chu = "mot"
    elif chu_so == '2': chu = "hai"
    elif chu_so == '3': chu = "ba"
    elif chu_so == '4': chu = "bon"
    elif chu_so == '5': chu = "nam"
    elif chu_so == '6': chu = "sau"
    elif chu_so == '7': chu = "bay"
    elif chu_so == '8': chu = "tam"
    elif chu_so == '9': chu = "chin"
    
    ket_qua += chu + " "

print("ket qua ", ket_qua)