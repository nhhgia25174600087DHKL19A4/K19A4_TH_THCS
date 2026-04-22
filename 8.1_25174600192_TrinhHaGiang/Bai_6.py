def value(x):
    return x + 1
def main():
    n = int(input("Nhập số nguyên bất kỳ: "))
    count = value(n)
    print(f"Số kế tiếp của {n} là: {count}")
main()
