import random
so_thoa_man = [i for i in range(201) if i % 5 == 0 and i % 7 == 0]

if so_thoa_man:
    print(random.choice(so_thoa_man))