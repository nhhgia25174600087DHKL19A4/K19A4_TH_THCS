from functools import reduce
def tao_list_chan():
    list_chan = []
    for i in range(1, 101):
        if i % 2 == 0:
            list_chan.append(i)
    print(list_chan)
def tinh_tong_chan_voi_filter_reduce():
    n = int(input("\nb) Nhập số nguyên n: "))
    list_goc = list(range(1, n + 1))
    list_chan = list(filter(lambda x: x % 2 == 0, list_goc))
    if list_chan:
        tong = reduce(lambda x, y: x + y, list_chan)
    else:
        tong = 0
    print(f"Danh sách từ 1 đến {n}: {list_goc}")
    print(f"Các số chẵn được lọc: {list_chan}")
    print(f"Tổng các số chẵn: {tong}")
tao_list_chan()
tinh_tong_chan_voi_filter_reduce()