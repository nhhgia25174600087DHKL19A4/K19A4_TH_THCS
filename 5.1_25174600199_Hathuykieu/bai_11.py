test_list = [(4,5), (7,6), (1,0), (3,4)]
search_tup = [(3,4), (8,9), (7,6), (1,2)]
co = []
khong = []
for t in search_tup:
    if t in test_list:
        co.append(t)
    else:
        khong.append(t)
print("Có trong test_list:", co)
print("Không có:", khong)