import random
n = int(input("Nhập n (Bài 11): "))
A = [int(input(f"Phần tử {i+1}: ")) for i in range(n)]
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("11a. Danh sách B:", B)
C = [x**2 for x in A]
print("11b. Danh sách C:", C)
div_3 = [x for x in A if x % 3 == 0]
# Lấy ngẫu nhiên k phần tử (k có thể tự định nghĩa, ở đây lấy 1/2 số lượng)
k = len(div_3) // 2 if len(div_3) > 1 else len(div_3)
D = random.sample(div_3, k) if div_3 else []
print(" Danh sách D (ngẫu nhiên chia hết cho 3):", D)