def tinh_tong_de_quy(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + tinh_tong_de_quy(n - 1)

try:
    n_input = int(input("Nhập n: "))
    result = tinh_tong_de_quy(n_input)
    print(f"Tổng từ 1 đến {n_input} là: {result}")
except ValueError:
    print("Vui lòng nhập số nguyên.")
