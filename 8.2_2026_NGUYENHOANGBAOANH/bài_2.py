import random

def tao_list_binh_phuong():
    n = int(input("n="))
    lst = [random.randint(1,100) for _ in range(n)]
    
 
    binh_phuong = list(map(lambda x: x*x, lst))
    
    print("Gốc:", lst)
    print("Bình phương:", binh_phuong)
    return binh_phuong

tao_list_binh_phuong()