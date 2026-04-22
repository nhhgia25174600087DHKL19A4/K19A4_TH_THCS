def bai15a():
    lst_chan = []
    for i in range(1, 101):
        if i % 2 == 0:
            lst_chan.append(i)
    print("List số chẵn từ 1 đến 100:")
    print(lst_chan)
    return lst_chan
def my_reduce_sum(lst):
    tong = 0
    for x in lst:
        tong += x
    return tong
#b
def bai15b():
    n = int(input("Nhập n: "))
    lst = [i for i in range(1, n+1)]
    print("Danh sách từ 1 đến n:", lst)

    # lọc số chẵn (thay cho filter)
    chan = []
    for x in lst:
        if x % 2 == 0:
            chan.append(x)

    tong = my_reduce_sum(chan)
    print("Các số chẵn:", chan)
    print("Tổng các số chẵn trong danh sách:", tong)

def main():
    print("Bài 15:")
    bai15a()
    bai15b()
main()
