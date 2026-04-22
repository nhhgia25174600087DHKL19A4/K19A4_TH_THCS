# a) Hàm kiểm tra số nguyên tố
def kiem_tra_nguyen_to():
    n = int(input("Nhập số nguyên dương n (kiểm tra nguyên tố): "))
    if n < 2:
        print(f"{n} không phải là số nguyên tố")
        return
    
    la_nguyen_to = True
    for i in range(2, n):
        if n % i == 0:
            la_nguyen_to = False
            break
    
    if la_nguyen_to:
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")


# b) Hàm kiểm tra số hoàn hảo
def kiem_tra_hoan_hao():
    n = int(input("Nhập số nguyên dương n (kiểm tra hoàn hảo): "))
    tong_uoc = 0
    
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    
    if tong_uoc == n:
        print(f"{n} là số hoàn hảo")
    else:
        print(f"{n} không phải là số hoàn hảo")


# c) Hàm in các số đối xứng trong phạm vi 1000
def in_so_doi_xung():
    print("Các số đối xứng trong phạm vi 1000:")
    dem = 0
    for n in range(1, 1001):
        s = str(n)
        if s == s[::-1]:  # kiểm tra đối xứng
            print(f"{n:5}", end="")  # in số với độ rộng 5 ký tự
            dem += 1
            if dem % 15 == 0:  # sau 15 số thì xuống dòng
                print()

def main():
    kiem_tra_nguyen_to()
    kiem_tra_hoan_hao()
    in_so_doi_xung()
main()
