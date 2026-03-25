def indian_multiply(a, b):
    # Nếu b là số chẵn
    if b % 2 == 0:
        return indian_multiply(a, b // 2) + indian_multiply(a, b // 2)
    else:
        # Nếu b là số lẻ
        if b == 1:
            return a
        return indian_multiply(a, b // 2) + a

# Nhập 2 số nguyên
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Gọi hàm và in kết quả
print("Kết quả nhân:", indian_multiply(a, b))