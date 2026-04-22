nums = [int(x) for x in input("Nhập dãy số cách nhau bởi dấu cách: ").split()]
for num in nums:
    assert num % 2 == 0, f"Lỗi: Phát hiện số lẻ {num} trong danh sách!"
print("Tất cả đều là số chẵn.")