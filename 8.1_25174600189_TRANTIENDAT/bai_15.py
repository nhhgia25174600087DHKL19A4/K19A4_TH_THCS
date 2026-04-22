# a)
def tao_list_chan():
    lst = []
    for i in range(1, 101):
        if i % 2 == 0:
            lst.append(i)
    return lst

print(tao_list_chan())

# b)
from functools import reduce

def tong_chan(lst):
    chan = list(filter(lambda x: x % 2 == 0, lst))

    tong = reduce(lambda a, b: a + b, chan, 0)

    return tong

def main():
    n = int(input("Nhập n: "))
    
    lst = []
    for i in range(1, n + 1):
        lst.append(i)

    print("Danh sách:", lst)
    print("Tổng số chẵn:", tong_chan(lst))

main()