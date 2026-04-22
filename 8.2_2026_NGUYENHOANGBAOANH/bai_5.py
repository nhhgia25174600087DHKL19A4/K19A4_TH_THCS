import random

def kiem_tra_chan():
    n = int(input("n="))
    lst = [random.randint(1,100) for _ in range(n)]
    
    # Lambda kiểm tra chẵn
    la_chan = list(map(lambda x: x%2==0, lst))
    
    print("Danh sách:", lst)
    print("Chẵn (True/False):", la_chan)
    return la_chan

kiem_tra_chan()