def ham_uoc_so():
    n = int(input("nhập số nguyên dương n: "))
    if n <= 0:
        print(" nhập số nguyên dương.")
        return   
    uoc_so = [i for i in range(1, n + 1) if n % i == 0]
    print(f"Các ước số của {n} là: {uoc_so}")
ham_uoc_so()