def liet_ke_uoc_so(n):
    print("Các ước số của {} là:".format(n))
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print() 
def bai_10():
    print("--- Chương trình tìm ước số ---")
    while True:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        print("Vui lòng nhập n > 0!")
    liet_ke_uoc_so(n)
bai_10()