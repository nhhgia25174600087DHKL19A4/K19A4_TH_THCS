n = int(input("Nhập vào một số nguyên dương n: "))
if n > 0:
    print(f"Các số từ {n} đến {n**2} là:")
    for i in range(n, n**2 + 1):
            print(i, end=" ")
else:
    print("Vui lòng nhập một số nguyên lớn hơn 0.")
print("Lỗi: Bạn phải nhập vào một số nguyên.")