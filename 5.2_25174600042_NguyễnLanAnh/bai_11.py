n = int(input("Nhập n: "))
A = [int(input(f"Nhập phần tử {i+1}: ")) for i in range(n)]
print("List A:", A)
#a
chan = [x for x in A if x % 2 == 0]
print("Số chẵn:", chan)
#b
le = [x for x in A if x % 2 != 0]
print("Số lẻ:", le)
#c
duong = [x for x in A if x > 0]
print("Số dương:", duong)
#d
am = [x for x in A if x < 0]
print("Số âm:", am)
#e
bp = [x**2 for x in A]
print("Bình phương:", bp)