import random

def nguyen_to(x): return x>1 and all(x%i for i in range(2,int(x**0.5)+1))

def tao_list_nguyen_to():
    n = int(input("n="))
    lst = [random.randint(2,100) for _ in range(n)]
    
   
    nguyen_to_lst = list(filter(nguyen_to, lst))
    
    print("Danh sách:", lst)
    print("Số nguyên tố:", nguyen_to_lst)
    return nguyen_to_lst

tao_list_nguyen_to()