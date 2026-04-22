def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def cau_a():
    n = int(input("Câu a - Nhập số nguyên dương n: "))
    if kiem_tra_nguyen_to(n):
        print(f"-> {n} là số nguyên tố.\n")
    else:
        print(f"-> {n} không phải là số nguyên tố.\n")


# CÂU B: KIỂM TRA SỐ HOÀN HẢO

def kiem_tra_hoan_hao(n):
    if n < 2:
        return False
    tong_uoc = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            tong_uoc += i
            
    return tong_uoc == n

def cau_b():
    n = int(input("Câu b - Nhập số nguyên dương n: "))
    if kiem_tra_hoan_hao(n):
        print(f"-> {n} là số hoàn hảo.\n")
    else:
        print(f"-> {n} không phải là số hoàn hảo.\n")


# CÂU C: TÌM SỐ ĐỐI XỨNG

def kiem_tra_doi_xung(n):
    so_ban_dau = n
    so_dao_nguoc = 0
    
    while n > 0:
        chu_so_cuoi = n % 10                      
        so_dao_nguoc = (so_dao_nguoc * 10) + chu_so_cuoi 
        n = n // 10                               
        
    return so_ban_dau == so_dao_nguoc

def cau_c():
    print("Câu c - Các số đối xứng trong phạm vi 1000 là:")
    dem = 0 
    for i in range(1000):
        if kiem_tra_doi_xung(i):
            print(f"{i:<5}", end="")
            dem += 1
            if dem % 15 == 0:
                print() 
    print("\n")

if __name__ == "__main__":
    cau_a()
    cau_b()
    cau_c()