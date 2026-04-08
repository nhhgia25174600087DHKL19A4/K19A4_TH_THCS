n = int(input("Nhập số lượng phần tử n: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
print("a. Tổng các phần tử:", sum(a))
positives = [x for x in a if x > 0]
print(f"b. Số lượng số dương: {len(positives)}, Tổng số dương: {sum(positives)}")
first_neg_idx = next((i for i, x in enumerate(a) if x < 0), -1)
print("c. Vị trí phần tử âm đầu tiên:", first_neg_idx)
last_pos_idx = next((i for i in range(len(a)-1, -1, -1) if a[i] > 0), -1)
print("d. Vị trí phần tử dương cuối cùng:", last_pos_idx)
if a:
    max_val = max(a)
    last_max_idx = max(i for i, x in enumerate(a) if x == max_val)
    print(f"e. GTLN: {max_val}, Vị trí xuất hiện cuối cùng: {last_max_idx}")