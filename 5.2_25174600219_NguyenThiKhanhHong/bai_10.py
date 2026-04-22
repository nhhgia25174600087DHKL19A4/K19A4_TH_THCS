import random
n = [x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0]
if n:
    so_ngau_nhien = random.choice(n)
    print(f"Danh sách các số thỏa mãn: {n}")
    print(f"Số ngẫu nhiên chọn được: {so_ngau_nhien}")
else:
    print("Không có số nào thỏa mãn điều kiện.")