n = int(input("Nhập n: "))
if  n < 2:
    print("Không phải số nguyên tố ")
else:
    la_SNT = True
    for i in range(2, n):
        if n % i == 0:
            la_SNT = False
            break
    if la_SNT:
        print("Là số nguyên tố")
    else:
        print("Không phải số nguyên tố")        
              