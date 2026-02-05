n = int(input("Nhập n: "))
tong_le = 0

for i in range(1, n + 1, 2):
    tong_le += i

print(f"Tổng các số lẻ từ 1 đến {n} là: {tong_le}")
