def cong(a, b): return a + b
def tru(a, b): return a - b
def nhan(a, b): return a * b
def chia(a, b): return a / b if b != 0 else None
def luy_thua(a, b): return a ** b

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print(f"Tổng: {cong(a,b)}")
print(f"Hiệu: {tru(a,b)}")
print(f"Tích: {nhan(a,b)}")
if chia(a,b) is not None:
    print(f"Thương: {chia(a,b)}")
else:
    print("Không thể chia cho 0")
print(f"{a}^{b} = {luy_thua(a,b)}")