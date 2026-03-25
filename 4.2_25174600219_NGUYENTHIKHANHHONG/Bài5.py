a_gốc = int(input("Nhập số nguyên a: "))
b_gốc = int(input("Nhập số nguyên b: "))
a, b = abs(a_gốc), abs(b_gốc)
temp_a, temp_b = a, b
while temp_b != 0:
    so_du = temp_a % temp_b
    temp_a = temp_b
    temp_b = so_du

ucln = temp_a
if ucln == 0:
    bcnn = 0
else:
    bcnn = abs(a_gốc * b_gốc) // ucln
print(f"\nUCLN({a_gốc}, {b_gốc}) = {ucln}")
print(f"BCNN({a_gốc}, {b_gốc}) = {bcnn}")
ucln_for = 1
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        ucln_for = i
        break