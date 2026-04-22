from functools import reduce

def list_chan():
    chan = [x for x in range(1, 101) if x % 2 == 0]
    print("Danh sách số chẵn từ 1 đến 100:")
    print(chan)

def tong_chan():
    n = int(input("Nhập n: "))
    ds = list(range(1, n + 1))
    chan = list(filter(lambda x: x % 2 == 0, ds))
    tong = reduce(lambda a, b: a + b, chan, 0)
    print(f"Danh sách các số từ 1 đến {n}: {ds}")
    print(f"Các số chẵn trong danh sách: {chan}")
    print(f"Tổng các số chẵn = {tong}")

def bai_15():
    while True:
        print("\n" + "="*50)
        print("BÀI 15")
        print("="*50)
        print("a. Tạo list chứa toàn số chẵn thuộc [1, 100]")
        print("b. Tính tổng các số chẵn từ 1 đến n (dùng filter và reduce)")
        print("0. Thoát")
        print("-"*50)
        
        chon = input("Nhập lựa chọn (a/b/0): ").lower()
        
        if chon == "a":
            list_chan()
        elif chon == "b":
            tong_chan()
        elif chon == "0":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    bai_15()