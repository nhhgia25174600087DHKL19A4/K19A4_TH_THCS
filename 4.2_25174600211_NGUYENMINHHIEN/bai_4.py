n = input("Nhập một số: ")
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
ket_qua = []
for digit in n:
    if digit.isdigit():
        ket_qua.append(chu[int(digit)])
print("Kết quả:", " ".join(ket_qua))