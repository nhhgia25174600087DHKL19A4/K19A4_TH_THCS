n = input("Nhập số: ")
chu_so = ["không", "một", "hai", "ba", "bốn", 
          "năm", "sáu", "bảy", "tám", "chín"]
for ch in n:
    print(chu_so[int(ch)], end=" ")