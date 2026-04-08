import random
valid_nums = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]
print(" Số ngẫu nhiên chia hết cho 5 và 7:", random.choice(valid_nums))