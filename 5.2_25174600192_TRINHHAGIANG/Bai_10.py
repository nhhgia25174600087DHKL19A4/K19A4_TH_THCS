import random

danh_sach_hop_le = [so for so in range(0, 201) if so % 5 == 0 and so % 7 == 0]
so_ngau_nhien = random.choice(danh_sach_hop_le)

print("Số ngẫu nhiên chia hết cho 5 và 7 từ 0 đến 200 là:", so_ngau_nhien)